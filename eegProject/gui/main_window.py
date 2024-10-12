import sys
from resources import *
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from eeg_io.receiver import Receiver
import threading
from gui.plot_canvas import PlotCanvas
from processing.filter import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('resources/main_window_UI.ui', self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_startIcon = True

        self.receiver = Receiver()
        self.receiver.msg.connect(self.show_msg)

        self.serial_reading_thread = None
        self.packet_updating_thread = None
        self.reader_thread = None

        self.visualWidget = self.findChild(QWidget, "visualWidget")
        self.plot_canvas = PlotCanvas(self.visualWidget, dpi=100)
        layout = QVBoxLayout(self.visualWidget)
        layout.addWidget(self.plot_canvas)

        self.checkBox_notch_filter.stateChanged.connect(self.update_ui)
        self.checkBox_filter.stateChanged.connect(self.update_ui)
        self.radioButton_low.clicked.connect(self.update_ui)
        self.radioButton_high.clicked.connect(self.update_ui)
        self.radioButton_band.clicked.connect(self.update_ui)
        self.radioButton_delta.clicked.connect(self.update_ui)
        self.radioButton_alpha.clicked.connect(self.update_ui)
        self.radioButton_beta.clicked.connect(self.update_ui)
        self.radioButton_gamma.clicked.connect(self.update_ui)
        self.radioButton_theta.clicked.connect(self.update_ui)
        self.radioButton_mu.clicked.connect(self.update_ui)
        self.radioButton_filter.clicked.connect(self.update_ui)

        self.notch_freq = 50
        self.notch_q_factor = 35
        self.filter_low_freq = 0
        self.filter_high_freq = 0
        self.filter_order = 4
        self.fs = 250

    def pushButton_clicked(self):
        if self.pushButton_startIcon:
            self.start_receving()
            self.pushButton.setIcon(QtGui.QIcon("resources/images/stop.png"))
            self.pushButton_startIcon = False
            for item in self.groupBox_link.findChildren(QWidget):
                if item != self.pushButton:
                    item.setEnabled(False)

        else:
            self.stop_receving()
            self.pushButton.setIcon(QtGui.QIcon("resources/images/start.png"))
            self.pushButton_startIcon = True
            for item in self.groupBox_link.findChildren(QWidget):
                item.setEnabled(True)

    def start_receving(self):
        self.timer.start(500)
        print('Start receiving...')
        self.receiver.PORT = self.comboBox_port.currentText()
        self.receiver.BAUD_RATE = int(self.comboBox_baudrate.currentText())
        if self.serial_reading_thread is None or not self.serial_reading_thread.is_alive():
            self.serial_reading_thread = threading.Thread(target=self.receiver.run_serial_reading_thread)
            self.serial_reading_thread.daemon = True
            self.serial_reading_thread.start()

        if self.packet_updating_thread is None or not self.packet_updating_thread.is_alive():
            self.packet_updating_thread = threading.Thread(target=self.receiver.run_packet_updating_thread)
            self.packet_updating_thread.daemon = True
            self.packet_updating_thread.start()

    def stop_receving(self):
        print('Stop receiving...')
        self.timer.stop()
        self.receiver.stop_threads()
        if self.serial_reading_thread and self.serial_reading_thread.is_alive():
            self.receiver.stop_threads()
            self.serial_reading_thread.join()
        if self.packet_updating_thread and self.packet_updating_thread.is_alive():
            self.receiver.stop_threads()
            self.packet_updating_thread.join()

    def update_ui(self):
        if self.checkBox_notch_filter.isChecked():
            for item in self.groupBox_notch.findChildren((QLabel, QComboBox, QSpinBox)):
                item.setEnabled(True)
        else:
            for item in self.groupBox_notch.findChildren((QLabel, QComboBox, QSpinBox)):
                item.setEnabled(False)

        if self.checkBox_filter.isChecked():
            for item in self.groupBox_filter.findChildren((QLabel, QComboBox, QDoubleSpinBox, QRadioButton)):
                item.setEnabled(True)
            if self.radioButton_filter.isChecked():
                if self.radioButton_low.isChecked():
                    self.label_low.setEnabled(False)
                    self.spinBox_filter_low_freq.setEnabled(False)
                elif self.radioButton_high.isChecked():
                    self.label_high.setEnabled(False)
                    self.spinBox_filter_high_freq.setEnabled(False)
                return
            self.radioButton_band.setChecked(True)
            for item in self.groupBox_filter_freq.findChildren((QLabel, QDoubleSpinBox)):
                item.setEnabled(False)
            for item in self.widget_filter_type.findChildren(QRadioButton):
                item.setEnabled(False)
            if self.radioButton_delta.isChecked():
                self.spinBox_filter_low_freq.setValue(0.5)
                self.spinBox_filter_high_freq.setValue(4.0)
            if self.radioButton_theta.isChecked():
                self.spinBox_filter_low_freq.setValue(4.0)
                self.spinBox_filter_high_freq.setValue(8.0)
            if self.radioButton_alpha.isChecked():
                self.spinBox_filter_low_freq.setValue(8.0)
                self.spinBox_filter_high_freq.setValue(13.0)
            if self.radioButton_beta.isChecked():
                self.spinBox_filter_low_freq.setValue(13.0)
                self.spinBox_filter_high_freq.setValue(30.0)
            if self.radioButton_gamma.isChecked():
                self.spinBox_filter_low_freq.setValue(30.0)
                self.spinBox_filter_high_freq.setValue(100.0)
            if self.radioButton_mu.isChecked():
                self.spinBox_filter_high_freq.setValue(8.0)
                self.spinBox_filter_low_freq.setValue(12.0)
        else:
            for item in self.groupBox_filter.findChildren((QLabel, QComboBox, QDoubleSpinBox, QRadioButton, QSpinBox)):
                item.setEnabled(False)

    def show_msg(self, msg):
        self.label_msg.setText(msg)

    def update_plot(self):
        try:
            data = self.receiver.read_4channel_data()
            if data is None:
                return
            selected_channels = []
            selected_graphs = []
            if self.checkBox_channel1.isChecked():
                selected_channels.append('channel1')
            if self.checkBox_channel2.isChecked():
                selected_channels.append('channel2')
            if self.checkBox_channel3.isChecked():
                selected_channels.append('channel3')
            if self.checkBox_channel4.isChecked():
                selected_channels.append('channel4')
            if self.checkBox_time.isChecked():
                selected_graphs.append('Time Domain')
            if self.checkBox_freq.isChecked():
                selected_graphs.append('Frequency Domain')
            if self.checkBox_spectrogram.isChecked():
                selected_graphs.append('Spectrogram')
            if self.checkBox_psd.isChecked():
                selected_graphs.append('PSD')
            if self.checkBox_notch_filter.isChecked():
                self.notch_freq = int(self.comboBox_notch_freq.currentText())
                self.notch_q_factor = self.spinBox_notch_q_factor.value()
                data = notch_filter_fir(data, self.notch_freq, self.notch_q_factor, self.fs)
            if self.checkBox_filter.isChecked():
                self.filter_low_freq = self.spinBox_filter_low_freq.value()
                self.filter_high_freq = self.spinBox_filter_high_freq.value()
                self.filter_order = self.spinBox_filter_order.value()
                self.fs = int(self.comboBox_fs.currentText())
                type = 'band'
                cutoff = [self.filter_low_freq, self.filter_high_freq]
                if self.radioButton_low.isChecked():
                    type = 'low'
                    cutoff = self.filter_high_freq
                if self.radioButton_high.isChecked():
                    type = 'high'
                    cutoff = self.filter_low_freq
                data = fir_filter(data, cutoff,  self.fs, self.filter_order, type)
            self.plot_canvas.plot(selected_channels, selected_graphs, data, self.fs)
        except Exception as e:
            print(e)
