import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate

from thinkdsp import SinSignal

signal = SinSignal(freq=440)
duration = signal.period * 30.25
wave = signal.make_wave(duration)
spectrum = wave.make_spectrum()
wave.apodize()
wave.make_audio()
wave.write(filename='3.1.wav')

spectrum.plot(high=880)
decorate(xlabel='Frequency (Hz)')


for window_func in [np.bartlett, np.blackman, np.hamming, np.hanning]:
    wave = signal.make_wave(duration)
    wave.ys *= window_func(len(wave.ys))

    spectrum = wave.make_spectrum()
    spectrum.plot(high=880, label=window_func.__name__)

decorate(xlabel='Frequency (Hz)')

plt.show()