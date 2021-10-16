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

data_int = np.array(struct.unpack(str(2*CHUNK)+ 'B', data), dtype='b')  # This is unpacking the data into an int with length = 2*chunck in bytes
# b is an integer from 0 to 255
# the + 127 will make it so the values larger than 255 will wrap around the graph
fig, ax = plt.subplots()
ax.plot(data_int, '-')
plt.show()