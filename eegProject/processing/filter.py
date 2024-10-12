from scipy.signal import lfilter, firwin, butter


def notch_filter_fir(signal, center_freq, q_factor, fs, numtaps=101):
    nyq = 0.5 * fs
    bandwidth = center_freq / q_factor
    low = (center_freq - 0.5 * bandwidth) / nyq
    high = (center_freq + 0.5 * bandwidth) / nyq
    taps = firwin(numtaps, [low, high], pass_zero=False)
    filtered_signal = lfilter(taps, 1, signal)
    return filtered_signal


def fir_filter(signal, cutoff, fs, numtaps, btype):
    nyq = 0.5 * fs
    if isinstance(cutoff, list):
        cutoff = [e / nyq for e in cutoff]
    else:
        cutoff = cutoff / nyq
    pass_zero = False
    if btype == 'low':
        pass_zero = True
    taps = firwin(numtaps, cutoff, pass_zero=pass_zero)
    filtered_data = lfilter(taps, 1, signal)
    return filtered_data


def butter_filter(signal, cutoff, fs, order, btype):
    nyq = 0.5 * fs
    if isinstance(cutoff, list):
        cutoff = [e / nyq for e in cutoff]
    else:
        cutoff = cutoff / nyq
    b, a = butter(order, cutoff, btype)
    filtered_signal = lfilter(b, a, signal)
    return filtered_signal
