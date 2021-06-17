from wave import Wave_read
from thinkdsp import SawtoothSignal
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal


square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)

wave = square
wave.apodize()
wave.make_audio()
wave.write(filename='6.9.3.wav')
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')


plt.show()