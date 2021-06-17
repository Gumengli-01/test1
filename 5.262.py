# -*- coding: utf-8 -*-
"""
Created on Wed May 26 08:36:57 2021

@author: GML
"""
from thinkdsp import read_wave

wave = read_wave('aaa.wav')
wave.normalize()
wave.make_audio()
wave.plot()