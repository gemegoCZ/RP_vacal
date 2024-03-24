import numpy as np
import pyaudio as pa
import struct
import matplotlib.pyplot as plt
from colorsys import hls_to_rgb
from colorama import Fore

FORMAT = pa.paInt16
CHANNELS = 1
SAMPLE_RATE = 44100 # in Hz
CHUNK = 1024 * 2

p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = SAMPLE_RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig,ax = plt.subplots()
x = np.arange(0,CHUNK,1)
line, = ax.plot(x, np.random.rand(CHUNK),'r')
ax.set_ylim(-6000,6000)
ax.ser_xlim = (0,CHUNK)
fig.show()
first_integer = []
# print(f"\033[38;2;0;100;12mHello!\033[0m")

def change_color_text (text,r,g,b):
    textcolor = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    return textcolor

while True:
    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    line.set_ydata(dataInt) #len(dataInt) = CHUNK
    print(len(dataInt))

    fig.canvas.draw()
    fig.canvas.flush_events()
    # print(dataInt)
    first_integer = list(dataInt[:8])
    first_integer.append(255)
    # print("first_integer" + str(first_integer))






    def convert_to_rgb(first_integer):
        # Normalize the integer data to the range [0, 255]
        normalized_data = np.interp(first_integer, (min(first_integer), max(first_integer)), (0, 255))

        # Convert the normalized data to uint8 type (0-255)
        rgb_data = np.uint8(normalized_data)

        # For grayscale, RGB values will be the same for all channels
        return np.stack(rgb_data)

    rgb_data = convert_to_rgb(first_integer)
    print("rgb_date" + str(rgb_data))
    text = str(chr(9608))
    # print(len(rgb_data))

    if len(rgb_data)>=3:
        r = rgb_data[3]
        g = rgb_data[4]
        b = rgb_data[5]
        print(change_color_text(text,r,g,b), end="")
