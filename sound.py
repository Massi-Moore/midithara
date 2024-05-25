# sound.py
import os
import pygame as py
from constants import *
import pyaudio
import wave

CHUNK = 4096
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "sample.wav"

class SoundManager:

    def record_audio(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def __init__(self, scale, effect=None):
        py.mixer.init()
        py.mixer.set_num_channels(128)
        self.effect = effect
        self.effect_on = False  # Agregar el atributo 'effect_on'
        self.volume = 1
        self.set_scale(scale, effect)
        self.set_volume(1)  # Configura el volumen inicial

    def set_scale(self, scale, effect=None):
        self.effect = effect if effect is not None else self.effect
        if self.effect:
            self.notes_folder = f'notes/piano/{self.effect}/{scale}'
            self.notes_filenames = [f'{note}{scale}_{self.effect}.wav' for note in NOTES_FILENAMES]
        else:
            self.notes_folder = f'notes/piano/{scale}'
            self.notes_filenames = [f'{note}{scale}.wav' for note in NOTES_FILENAMES]
        self.notes_sounds = [py.mixer.Sound(os.path.join(self.notes_folder, filename)) for filename in self.notes_filenames]

    def toggle_effect(self, scale):
        if self.effect:
            self.effect = None
            self.effect_on = False
        else:
            self.effect = 'Reverb'
            self.effect_on = True
        self.set_scale(scale)
        
    def play_sound(self, key_index):
        if 0 <= key_index < len(self.notes_sounds):
            self.notes_sounds[key_index].play()
        else:
            pass
 
    def stop_sounds(self):
        py.mixer.quit()

    def set_volume(self, volume):
        self.volume = volume
        for sound in self.notes_sounds:
            sound.set_volume(volume)