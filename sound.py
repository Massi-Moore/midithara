# sound.py
import os
import pygame as py
from constants import *

class SoundManager:
    def __init__(self, scale):
        py.mixer.init()
        py.mixer.set_num_channels(128)
        self.set_scale(scale)
        self.set_volume(1)  # Configura el volumen inicial

    def set_scale(self, scale):
        self.notes_folder = f'notes/piano/{scale}'
        self.notes_filenames = [f'{note}{scale}.wav' for note in NOTES_FILENAMES]
        self.notes_sounds = [py.mixer.Sound(os.path.join(self.notes_folder, filename)) for filename in self.notes_filenames]

    def play_sound(self, key_index):
        if 0 <= key_index < len(self.notes_sounds):
            self.notes_sounds[key_index].play()
        else:
            pass
 
    def stop_sounds(self):
        py.mixer.quit()

    def set_volume(self, volume):
        for sound in self.notes_sounds:
            sound.set_volume(volume)

