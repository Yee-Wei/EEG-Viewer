import threading
import time
import pandas as pd
import serial
import yaml
import logging
import queue
import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal


class Receiver(QObject):

    msg = pyqtSignal(str)

    def __init__(self, config_path='./config/config.yaml'):
        super(Receiver, self).__init__()
        config = yaml.safe_load(open(config_path, encoding='utf-8'))

        self.PORT = config['serial']['port']
        self.BAUD_RATE = config['serial']['baud_rate']

        self.serial_connection = None

        self.CHECK_INDICES = config['data_processing']['check_indices']
        self.HEADS = config['data_processing']['heads']
        self.PACKET_SIZE = config['data_processing']['packet_size']
        self.VALID_DATA_INDICES = config['data_processing']['valid_data_indices']
        self.BYTE_NUM = config['data_processing']['byte_num']

        self.RAW_BUFFER_SIZE = config['data_processing']['raw_buffer_size']
        self.BUFFER_SIZE = config['data_processing']['buffer_size']
        self.raw_buffer = queue.Queue(maxsize=self.RAW_BUFFER_SIZE)

        self.packet_buffer = []
        self.frame_drop_count = 0

        logging.basicConfig(
            filename=config['logging']['log_file_path'],
            level=logging.getLevelName(config['logging']['level']),
            format='%(asctime)s %(levelname)s %(message)s'
        )

        self.running = False

        self.time_start = time.time()
        self.time_record = time.time()
        self.count = 0
        self.fs_measured = 0


    def connect(self):
        self.running = True
        try:
            self.serial_connection = serial.Serial(self.PORT, self.BAUD_RATE, timeout=1)
            self.serial_connection.set_buffer_size(rx_size=8192, tx_size=8192)
            self.msg.emit(f"Connected to {self.PORT} at {self.BAUD_RATE}.")
            logging.info(f"Connected to {self.PORT} at {self.BAUD_RATE}.")
        except serial.SerialException as e:
            self.msg.emit(f"Failed to connect to {self.PORT} at {self.BAUD_RATE}.")
            logging.error(f"Failed to connect to {self.PORT}: {e}")
            raise

    def close(self):
        self.running = False
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            self.msg.emit(f"Disconnected from {self.PORT}.")
            logging.info(f"Disconnected from {self.PORT}.")

    def read_from_serial(self):
        if self.serial_connection and self.serial_connection.is_open:
            try:
                if self.serial_connection.in_waiting > 100:
                    line = self.serial_connection.read(100).hex()  # 十六进制字节流，这样解码才不会乱码
                    for i in range(0, len(line), 2):
                        d = int(line[i] + line[i+1], 16)
                        self.raw_buffer.put(d)
                        if self.count == 0:
                            self.time_start = time.time()
                        self.count += 1
                        curtime = time.time()
                        if curtime - self.time_start > 1 and self.time_record - self.time_start < 1:
                            self.fs_measured = self.count
                            self.msg.emit(f"实测采样率为：{self.fs_measured // self.PACKET_SIZE }")
                            self.count = 0
                        self.time_record = curtime


            except serial.SerialException as e:
                logging.error(f"Failed to read packet from {self.PORT}: {e}")

    def update_packets(self):
        if self.raw_buffer.qsize() < self.PACKET_SIZE:
            time.sleep(0.01)
            return

        for i in range(len(self.HEADS)):
            if not self.raw_buffer.get() == self.HEADS[i]:
                if len(self.packet_buffer) > 0:
                    self.frame_drop_count += 1
                    print(f"frame drop occurred, {self.frame_drop_count}")
                return

        packet = self.HEADS.copy()
        for i in range(len(self.HEADS), self.PACKET_SIZE):
            packet.append(self.raw_buffer.get())
        if not self.validate_data(packet):
            print("invalid packet")
            return

        hex_string = ''.join(str(format(e, '02x')) for e in packet)
        logging.info(f"valid packet: {hex_string}")
        if len(self.packet_buffer) == self.BUFFER_SIZE:
            self.packet_buffer.pop(0)
        self.packet_buffer.append(hex_string)

    def run_serial_reading_thread(self):
        self.connect()
        while self.running:
            self.read_from_serial()
        logging.info(f"Finished reading from {self.PORT}")

    def run_packet_updating_thread(self):
        while self.running:
            self.update_packets()
        logging.info("Finished updating packets")

    def stop_threads(self):
        self.close()
        self.raw_buffer.queue.clear()
        self.packet_buffer.clear()

    def calculate_checksum(self, data):
        """
        Calculate the checksum of the data
        :param data: valid data from a packet
        :return: list(check), the length of output is determined by the nums of the preset checks
        """
        checks = []
        checksum1 = 0
        checksum2 = 0
        for d in data:
            checksum1 += d
            checksum2 += checksum1
        checks.append(checksum1 & 0xFF)
        checks.append(checksum2 & 0xFF)
        if len(checks) != len(self.CHECK_INDICES):
            raise ValueError("check nums mismatch")
        return checks

    def validate_data(self, packet):
        """
        Checks if the packet is valid according to the check nums of the packet.
        :param packet: list(int) ndarray(int)
        :return: bool: true if the packet is valid, false otherwise
        """
        if len(packet) != self.PACKET_SIZE:
            print('Invalid packet size')
            return False
        data = packet[: self.CHECK_INDICES[0]]
        checks = self.calculate_checksum(data)
        for i in range(len(checks)):
            if checks[i] != packet[self.CHECK_INDICES[i]]:
                return False
        return True

    def read_4channel_data(self):
        if len(self.packet_buffer) == 0:
            return None
        packets = self.packet_buffer.copy()
        data = []
        for packet in packets:
            data.append(self.packet2data(packet))
        return np.array(data)

    def packet2data(self, packet):
        if len(packet) != self.PACKET_SIZE * 2:
            logging.warning('Packet size is wrong')
            return
        data_hex_string = packet[self.VALID_DATA_INDICES[0] * 2: (self.VALID_DATA_INDICES[1] + 1) * 2]
        data = []
        num = self.BYTE_NUM * 4
        for i in range(0, len(data_hex_string), num):
            data.append(int(data_hex_string[i: i+num], 16))
        return np.array(data)




