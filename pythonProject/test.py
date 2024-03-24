import numpy as np
import pyaudio as pa
import struct
import matplotlib.pyplot as plt
from scipy.fft import rfft
from colorsys import hls_to_rgb

FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # in Hz
CHUNK = 1024

p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, [ax1,ax2] = plt.subplots(nrows=2, ncols=1)
x = np.arange(0,CHUNK,1)
line, = ax1.plot(x, np.zeros(CHUNK),'r')
ax1.set_ylim(-6000,6000)
ax1.set_xlim(0,CHUNK)
fig.show()
first_integer = []
color_choose = []
# print(f"\033[38;2;0;100;12mHello!\033[0m")

while True:
    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    line.set_ydata(dataInt)

    fig.canvas.draw()
    fig.canvas.flush_events()

    real_time_rfft = rfft(dataInt)
    ax2.clear()
    ax2.plot(np.abs(real_time_rfft))
    ax2.set_ylim(0,100000)
    ax2.set_xlim(0,(CHUNK/2))

    color_choose.clear()
    for i in range(36):
        color_choose.append(i*max((real_time_rfft[(i*10):((i+1)*10)])))
    color_argmax = np.argmax(color_choose)

    # print(color_argmax)
    color_argmax = int(np.interp(color_argmax, (0, 25), (0, 360)))
    # print(color_argmax)

    rgb_list = hls_to_rgb(color_argmax/360,.5,.8)
    # print(rgb_list)
    rgb_list = list(rgb_list)

    for i in range(3):
        rgb_list[i] = int(np.interp(rgb_list[i], (0, 1), (0, 255)))
    # print(rgb_list)
    def change_color_text(text, r, g, b):
        textcolor = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
        return textcolor

    text = str(chr(9608))

    print(change_color_text(text,rgb_list[0],rgb_list[1],rgb_list[2]), end="")

