import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024 * 4 # This is the chunk size
FORMAT = pyaudio.paInt16 # This is a blank 16-bit binary string
CHANNELS = 1 # Mono sound
RATE = 44100 # 44.1 Khz

p = pyaudio.PyAudio()

stream  = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,output=True,frames_per_buffer=CHUNK)

data = stream.read(CHUNK)