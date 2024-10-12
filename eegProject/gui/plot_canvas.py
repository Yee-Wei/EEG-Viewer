from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import yaml
from scipy import signal
from matplotlib.lines import Line2D
from matplotlib.text import Text

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, dpi=100, config='./config/config.yaml'):
        self.fig = Figure(dpi=dpi)

        super(PlotCanvas, self).__init__(self.fig)
        self.setParent(parent)

        config = yaml.safe_load(open(config, encoding='utf-8'))
        self.channels = config['data_processing']['channels']
        self.fs = config['data_processing']['sampling_rate']
        self.period = config['data_processing']['slice_interval']

        self.text_size = 10
        self.margin_left = 0.15
        self.margin_other = 0.1
        self.y_cor_record = 0

    def plot(self, selected_channels, selected_graphs, data, fs):
        self.fig.clear()
        ncols = len(selected_graphs)
        nrows = len(selected_channels)
        figwidth, figheight = self.fig.get_size_inches()
        if ncols == 0 or nrows == 0:
            self.draw()
            return
        axs = self.fig.subplots(nrows, ncols)
        if not isinstance(axs, np.ndarray):
            axs = np.array([axs])
            axs = axs[np.newaxis, :]
        else:
            if len(selected_channels) == 1:
                axs = axs[np.newaxis, :]
            if len(selected_graphs) == 1:
                axs = axs[:, np.newaxis]
        wratio = (1 - self.margin_left - ncols * self.margin_other) / ncols
        hratio = (1 - (nrows + 1) * self.margin_other) / nrows
        hratio_new = hratio
        self.y_cor_record = 0
        for i, channel in enumerate(selected_channels):
            data_channel = self.get_channel_data(data, channel)
            y0 = (nrows - i) * self.margin_other + (nrows - 1 - i) * hratio
            for j, graph in enumerate(selected_graphs):
                x0 = self.margin_left + j * wratio + j * self.margin_other
                if j == 0 and figwidth * wratio < figheight * hratio:
                    hratio_new = figwidth * wratio / figheight
                    y0 = y0 + (hratio - hratio_new) * 0.5
                axs[i, j].set_position([x0, y0, wratio, hratio_new])


                if graph == 'Time Domain':
                    axs[i, j].plot(data_channel)
                    axs[i, j].set_title(graph, fontsize=self.text_size)
                    axs[i, j].set_xlabel('Time [n]', fontsize=self.text_size)
                    axs[i, j].set_ylabel('Amplitude [V]', fontsize=self.text_size)

                elif graph == 'Frequency Domain':
                    fft = np.fft.fft(data_channel)
                    freqs = np.fft.fftfreq(len(data[:, i]), 1 / self.fs)
                    axs[i, j].plot(freqs[:len(freqs) // 2], np.abs(fft[:len(freqs) // 2]))
                    axs[i, j].set_title(graph, fontsize=self.text_size)
                    axs[i, j].set_xlabel('Frequency (Hz)', fontsize=self.text_size)
                    axs[i, j].set_ylabel('Amplitude', fontsize=self.text_size)

                elif graph == 'Spectrogram':
                    f, t_stft, Zxx = signal.stft(data_channel, fs=self.fs, nperseg=64)
                    axs[i, j].pcolormesh(t_stft, f, np.abs(Zxx), shading='gouraud')
                    axs[i, j].set_title(graph, fontsize=self.text_size)
                    axs[i, j].set_xlabel('Time [ns]', fontsize=self.text_size)
                    axs[i, j].set_ylabel('Frequency [Hz]', fontsize=self.text_size)

                elif graph == 'PSD':
                    f, Pxx = signal.welch(data_channel, fs, nperseg=64)
                    axs[i, j].semilogy(f, Pxx)
                    axs[i, j].set_title(graph, fontsize=self.text_size)
                    axs[i, j].set_xlabel('Frequency [Hz]', fontsize=self.text_size)
                    axs[i, j].set_ylabel('PSD', fontsize=self.text_size)

            if i != 0 and nrows != 1:
                line = Line2D([0, 1], [y0 + hratio_new + 0.4 * (self.y_cor_record-y0-hratio_new), y0 + hratio_new + 0.4 * (self.y_cor_record-y0-hratio_new)], color='gray', linestyle='-', linewidth=0.3, transform=self.fig.transFigure)
                self.fig.add_artist(line)
            self.y_cor_record = y0

            text = Text(x=0.04, y=y0+hratio_new, text=channel, fontsize=self.text_size, ha='center', va='center', transform=self.fig.transFigure)
            self.fig.add_artist(text)

        # self.fig.tight_layout(h_pad=5, pad=2)
        # self.fig.subplots_adjust(left=0.1)

        self.draw()

    def get_channel_data(self, data, channel):
        if channel == 'channel1':
            return data[:, 0]
        elif channel == 'channel2':
            return data[:, 1]
        elif channel == 'channel3':
            return data[:, 2]
        return data[:, 3]

    def resizeEvent(self, event):
        super(PlotCanvas, self).resizeEvent(event)
        self.update_text_size(event.size().width(), event.size().height())

    def update_text_size(self, width, height):
        self.text_size = max(10, width / 125)






