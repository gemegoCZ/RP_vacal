import time

from moviepy.editor import AudioFileClip
from pydub import AudioSegment
from playsound import playsound
from scipy.io.wavfile import write
import wave
import matplotlib.pyplot as plt
import numpy as np
import os

src = "alastor.mp3"

src_wav = AudioSegment.from_file(src)
src_wav.export("between.wav", format="wav")

for i in range(3):
    Audio = AudioFileClip("between.wav")
    newAudio = Audio.subclip(i, i+1)
    newAudio.write_audiofile("test" + str(i) + ".wav")
    print(i)

    obj = wave.open("test" + str(i) + ".wav", "rb")

    sample_freq = obj.getframerate()
    n_samples = obj.getnframes()
    signal_wave = obj.readframes(-1)

    obj.close()

    t_audio = n_samples / sample_freq

    print(t_audio)

    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    print(np.size(signal_array))

    times = np.linspace(0, t_audio, num=len(signal_array))

    print(sample_freq)

    plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.title("Audio Signal")
    plt.ylabel("Signal wave")
    plt.xlabel("Time (s)")
    plt.xlim(0, t_audio)
    plt.show()

    os.remove("test" + str(i) + ".wav")

Audio = None
newAudio = None
time.sleep(4)
os.remove("between.wav")

# playsound("between.wav")
print("konec")



