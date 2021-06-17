from thinkdsp import SawtoothSignal
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal

signal = SquareSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
segment.plot()
decorate(xlabel='Time (s)')



wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()
wave.write(filename='6.9.2.wav')


spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()