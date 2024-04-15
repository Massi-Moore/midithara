# piano.py
import pygame as py
from constants import *

class Piano:
    def __init__(self, screen):
        self.screen = screen
        self.key_colors = {key: BLACK if 8 <= key <= 12 else WHITE for key in KEY_MAPPING.values()}
        self.font = py.font.Font(None, 50)  # Crea una fuente para el texto
        self.key_release_timers = {}

    def draw(self, scale):
        self.screen.fill(BG_COLOR)
        for i, pos in enumerate(KEY_POSITIONS):
            py.draw.rect(self.screen, self.key_colors[i], pos)
        for i, pos in enumerate(KEYB_POSITIONS):
            py.draw.rect(self.screen, self.key_colors[i+8], pos)
        for i, pos in enumerate(KEYBA_POSITIONS):
            py.draw.rect(self.screen, self.key_colors[i+10], pos)

        py.draw.rect(self.screen, (52, 115, 85), (65, 20, 300, 100))
        py.draw.rect(self.screen, (59, 140, 102), (70, 25, 290, 90))
        
        # Dibuja la escala actual en la pantalla
        img = self.font.render(f'A{scale}', True, (255, 255, 255))
        self.screen.blit(img, (100, 50))  # Cambia las coordenadas según sea necesario
            
    def update_key_color(self, key_index, color):
        if 8 <= key_index <= 12:
            self.key_colors[key_index] = color
        else:
            self.key_colors[key_index] = color

