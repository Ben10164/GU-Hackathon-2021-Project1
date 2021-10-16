import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

CHUNK = 1024 * 4  # This is the chunk size
FORMAT = pyaudio.paInt16  # This is a blank 16-bit binary string
CHANNELS = 1  # Mono sound
RATE = 44100  # 44.1 Khz

fig, ax = plt.subplots(1, figsize=(15, 7))

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, output=True, frames_per_buffer=CHUNK)

x = np.arange(0, 2*CHUNK, 2)

line, = ax.plot(x, np.random.randn(CHUNK))

ax.set_ylim(0, 255)
ax.set_xlim(0, CHUNK)

plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

# showing the plot
plt.show(block=False)

while True:

    # binary data
    data = stream.read(CHUNK)

    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = ((np.array(data_int, dtype='b')[::2]) / 2) + 128
    # the / 2 is just to make the waveform half the size
    # although this makes the graph not accurate, it is more visually appealing

    line.set_ydata(data_np)
    fig.canvas.draw()
    fig.canvas.flush_events()
