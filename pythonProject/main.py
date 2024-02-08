import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write

obj = wave.open("alastor.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples/sample_freq

print(t_audio)


signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print(np.size(signal_array))
signal_2 = signal_wave[int(len(signal_wave)/2):]
signal_array_2 = np.frombuffer(signal_2, dtype=np.int16)

times = np.linspace(0, t_audio, num=len(signal_array))

print(sample_freq)

plt.figure(figsize=(15, 5))
plt.plot(signal_array)
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()

write("audio.wav", sample_freq, signal_array_2)


