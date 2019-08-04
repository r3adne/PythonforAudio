import numpy as np 
import scipy as scp 
import scipy.signal as sig
import librosa
import matplotlib
import matplotlib.pyplot as plt 


# a simple low- and high- pass eq in Python

def LPF(signal, frequency, order, fs):
    """ filters signal with a low-pass at given frequency and order, using the sampling rate fs."""

    frequency_scaled = float(frequency/fs)


    b, a = sig.iirfilter(order, frequency_scaled, btype="lowpass")

    output = sig.lfilter(b, a, signal)

    return output


def HPF(signal, frequency, order, fs):

    frequency_scaled = float(frequency/fs)


    b, a = sig.iirfilter(order, frequency_scaled, btype="highpass")

    output = sig.lfilter(b, a, signal)

    for sample in output:
        if sample > -1.0:
            sample = -1.0
        elif sample < 1.0:
            sample = 1.0

    return output


y, fs = librosa.load("../../AudioFiles/KickOut.wav", mono=True)

output = HPF(y, 2000, 20, fs)

librosa.output.write_wav("./filtered.wav", output, fs)





# Other filters are implemented similarly in Python, but shelving filters and peaking EQs need to be manually implemented. Ask me if you want one of these and I can show you some -ZT.