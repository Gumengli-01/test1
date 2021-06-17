from wave import Wave_read
from thinkdsp import SawtoothSignal
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import TriangleSignal

def Spectrum1(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0]=0
    #spectrum.hs*=100


wave = TriangleSignal(freq=440).make_wave(duration=0.5)
wave.make_audio()


spectrum = wave.make_spectrum()
spectrum.plot(high=10000, color='gray')
Spectrum1(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)

decorate(xlabel='Frequency (Hz)')

filtered = spectrum.make_wave()
filtered.make_audio()
wave.write(filename='6.9.6.wav')
plt.show()