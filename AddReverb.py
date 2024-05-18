from pedalboard import Pedalboard,Reverb
import pedalboard
import soundfile as sf
import numpy as np
import sounddevice as sd
import os


# Load the audio file
audio_file = "notes/piano/5/T5.wav"
audio_data, sr = sf.read(audio_file)
pedalboard= Pedalboard()
reverb= Reverb()
reverb.room_size = 0.5
reverb.wet_level= 1.0
pedalboard.append(reverb)
effected= pedalboard(audio_data, sample_rate=sr)

output_file_path = os.path.splitext(audio_file)[0] + "_reverb.wav"
sf.write(output_file_path, effected, sr)

sd.play(effected, sr)
sd.wait()