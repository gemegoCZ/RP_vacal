from moviepy.editor import AudioFileClip
from pydub import AudioSegment
import pydub
from playsound import playsound
from pathlib import Path
import os

os.chdir("C:\\Users\\markoid\\PycharmProjects\\RP_vacal\\pythonProject")
print(os.getcwd())
print(os.path.exists("alastor.mp3"))

def check_file_permissions(file_path):
    if os.access(file_path, os.R_OK):
        print(f"Read permission is granted for file: {file_path}")
    else:
        print(f"Read permission is not granted for file: {file_path}")

    if os.access(file_path, os.W_OK):
        print(f"Write permission is granted for file: {file_path}")

    else:
        print(f"Write permission is not granted for file: {file_path}")

    if os.access(file_path, os.X_OK):
        print(f"Execute permission is granted for file: {file_path}")
    else:

        print(f"Execute permission is not granted for file: {file_path}")

file_path = "alastor.mp3"
check_file_permissions(file_path)

src = "C:\\Users\\markoid\\PycharmProjects\\RP_vacal\\pythonProject\\alastor.mp3"

src_wav = AudioSegment.from_file(src)
src_wav.export("between.wav", format="wav")

# src_wav = "alastor.wav"

for i in range(3):
    Audio = AudioFileClip(src_wav)
    newAudio = Audio.subclip(i, i+1)
    newAudio.write_audiofile("test" + str(i) + ".wav")
    print(i)
    # playsound("test" + str(i) + ".wav")
    os.remove("test" + str(i) + ".wav")

print("konec")
