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

fig, ax = plt.subplots()

x = np.arange(0,2*CHUNK,2)
line, = ax.plot(x,np.random.randn(CHUNK))
ax.set_ylim(0,255)
ax.set_xlim(0,CHUNK)

while True:
    data = stream.read(CHUNK)

    data_int = np.array(struct.unpack(str(2 * CHUNK)+ 'B', data), dtype='b')[::2] + 127 # This is unpacking the data into an int with length = 2*chunck in bytes
    # b is an integer from 0 to 255
    # the + 127 will make it so the values larger than 255 will wrap around the graph
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()



