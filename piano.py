# piano.py
import pygame as py
from constants import *
from pygame.sysfont import SysFont

class Piano:
    def __init__(self, screen, sound_manager):

        self.sound_manager = sound_manager

        self.screen = screen
        self.key_colors = {key: BLACK if 8 <= key <= 12 or 16 <= key <= 17 else WHITE for key in range(13)}  # Cambia KEY_MAPPING.values() a range(19)
        self.font1 = py.font.SysFont('Segoe UI', 22, bold=True)  # Crea una fuente para el texto
        self.font2 = py.font.SysFont('Segoe UI', 30, bold=True)
        self.key_release_timers = {}
        self.inner_key_colors = {key: color3 for key in range(13)}  # Cambia KEY_MAPPING.values() a range(19)

        # WAVEFORM IMAGE
        self.my_image = py.image.load('resources/graphs/waveform_a4.png')
        self.sound_manager = sound_manager
        self.waveform_image = None  # Añade este atributo para guardar la imagen del waveform

        # ICONS FOR BUTTONS
        self.plus_img = py.image.load('resources/icons/plus.png')
        self.minus_img = py.image.load('resources/icons/minus.png')
        self.scale_img = py.image.load('resources/icons/scale.png')
        self.scale2_img = py.image.load('resources/icons/scale2.png')
        self.reverb_img = py.image.load('resources/icons/reverb.png')
        self.save_img = py.image.load('resources/icons/save.png')
        self.record_img = py.image.load('resources/icons/record.png')

        # Define las variables para el tamaño y la posición de los rectángulos interiores
        self.inner_width_factor = 0.35
        self.inner_height_factor = 0.2
        self.inner_x_pos_factor = 0.34
        self.inner_y_pos_factor = 0.15

        self.inner_width1_factor = 0.8
        self.inner_height1_factor = 0.8
        self.inner_x1_pos_factor = 0.1
        self.inner_y1_pos_factor = 0.1

    def update_inner_key_color(self, key_index, color):
        if 8 <= key_index <= 12:  # Cambia 12 a 18 para agregar 6 teclas más
            self.inner_key_colors[key_index] = color
        else:
            self.inner_key_colors[key_index] = color

    
    def draw(self, scale):
        self.screen.fill(BG_COLOR)

        py.draw.rect(self.screen, KEY_BG_COLOR, (95, 335, 800, 235))
        
        for i, pos in enumerate(KEY_POSITIONS):
            py.draw.rect(self.screen, self.key_colors[i], pos)
            # Dibuja un rectángulo adicional en el centro

            inner_pos1 = (pos[0] + pos[2] * self.inner_x1_pos_factor, pos[1] + pos[3] * self.inner_y1_pos_factor, pos[2] * self.inner_width1_factor, pos[3] * self.inner_height1_factor)
            py.draw.rect(self.screen, color1, inner_pos1)

            inner_pos = (pos[0] + pos[2] * self.inner_x_pos_factor, pos[1] + pos[3] * self.inner_y_pos_factor, pos[2] * self.inner_width_factor, pos[3] * self.inner_height_factor)
            py.draw.rect(self.screen, self.inner_key_colors[i], inner_pos)

        for i, pos in enumerate(KEYB_POSITIONS):
            py.draw.rect(self.screen, self.key_colors[i+8], pos)
            # Dibuja un rectángulo adicional en el centro

            inner_pos1 = (pos[0] + pos[2] * self.inner_x1_pos_factor, pos[1] + pos[3] * self.inner_y1_pos_factor, pos[2] * self.inner_width1_factor, pos[3] * self.inner_height1_factor)
            py.draw.rect(self.screen, color2, inner_pos1)

            inner_pos = (pos[0] + pos[2] * self.inner_x_pos_factor, pos[1] + pos[3] * self.inner_y_pos_factor, pos[2] * self.inner_width_factor, pos[3] * self.inner_height_factor)
            py.draw.rect(self.screen, self.inner_key_colors[i+8], inner_pos)  # Cambia i a i+8
        
        for i, pos in enumerate(KEYBA_POSITIONS):
            py.draw.rect(self.screen, self.key_colors[i+10], pos)
            # Dibuja un rectángulo adicional en el centro

            inner_pos1 = (pos[0] + pos[2] * self.inner_x1_pos_factor, pos[1] + pos[3] * self.inner_y1_pos_factor, pos[2] * self.inner_width1_factor, pos[3] * self.inner_height1_factor)
            py.draw.rect(self.screen, color2, inner_pos1)
            
            inner_pos = (pos[0] + pos[2] * self.inner_x_pos_factor, pos[1] + pos[3] * self.inner_y_pos_factor, pos[2] * self.inner_width_factor, pos[3] * self.inner_height_factor)
            py.draw.rect(self.screen, self.inner_key_colors[i+10], inner_pos)  # Cambia i a i+10
    
        # RECT OF EFFECTS AND VOLUMES
        py.draw.rect(self.screen, WHITE, (67.8, 65, 335, 115), 3)
        py.draw.rect(self.screen, WHITE, (67.8, 192, 335, 115), 3 )
        py.draw.rect(self.screen, (220, 197, 196), (78, 202, 314.5, 95))

        # IMG OF WAVEFORM
        # IMG OF WAVEFORM
        if self.sound_manager.effect:
            waveform_filename = f'resources/graphs/waveform_a{scale}_{self.sound_manager.effect}.png'
        else:
            waveform_filename = f'resources/graphs/waveform_a{scale}.png'
        self.waveform_image = py.image.load(waveform_filename)

        # Dibujar la imagen del waveform en la pantalla
        self.screen.blit(self.waveform_image, (105,205))  # Ajusta las coordenadas según sea necesario
    
        # TEXT OF EFFECTS AND VOLUMES
        octave = self.font1.render(f'Oct', True, font_title_color)
        self.screen.blit(octave, (135, 95))

        scales = self.font2.render(f'C{scale}', True, (255, 255, 255))
        self.screen.blit(scales, (145, 120))  # Cambia las coordenadas según sea necesario    

        vol = self.font1.render(f'Vol', True, font_title_color)
        self.screen.blit(vol, (85, 95))
        
        volume = self.font2.render(str(int(self.sound_manager.volume * 10)), True, (255, 255, 255))
        self.screen.blit(volume, (95, 120))

        rev = self.font1.render(f'Effect', True, font_title_color)
        self.screen.blit(rev, (195, 95))

        rev_state = self.font2.render(str(self.sound_manager.effect) , True, (255, 255, 255))
        self.screen.blit(rev_state, (205, 120))

        status = self.font1.render(f'Status', True, font_title_color)
        self.screen.blit(status, (295, 95))

        saved = self.font2.render(f'Saved', True, (255, 255, 255))
        self.screen.blit(saved, (310, 120))

        #BUTTONS EFFECTS AND VOLUMES

        pos3=(490, 75, 105,105)
        py.draw.rect(self.screen, WHITE, pos3 )
        inner_pos3 = (pos3[0] + pos3[2] * self.inner_x1_pos_factor, pos3[1] + pos3[3] * self.inner_y1_pos_factor, pos3[2] * self.inner_width1_factor, pos3[3] * self.inner_height1_factor)
        py.draw.rect(self.screen, color1, inner_pos3)

        self.screen.blit(self.scale2_img, (495,85))

        pos3=(550, 223, 95,95)
        py.draw.rect(self.screen, WHITE, pos3 )
        inner_pos3 = (pos3[0] + pos3[2] * self.inner_x1_pos_factor, pos3[1] + pos3[3] * self.inner_y1_pos_factor, pos3[2] * self.inner_width1_factor, pos3[3] * self.inner_height1_factor)
        py.draw.rect(self.screen, color1, inner_pos3)

        self.screen.blit(self.reverb_img, (560,235))
        
        pos4=(600, 75, 105,105)
        py.draw.rect(self.screen, WHITE, pos4 )
        inner_pos4 = (pos4[0] + pos4[2] * self.inner_x1_pos_factor, pos4[1] + pos4[3] * self.inner_y1_pos_factor, pos4[2] * self.inner_width1_factor, pos4[3] * self.inner_height1_factor)
        py.draw.rect(self.screen, color1, inner_pos4)

        self.screen.blit(self.scale_img, (608,85))
        
        pos5=(740, 75, 105,105)
        py.draw.rect(self.screen, WHITE, pos5 )
        inner_pos5 = (pos5[0] + pos5[2] * self.inner_x1_pos_factor, pos5[1] + pos5[3] * self.inner_y1_pos_factor, pos5[2] * self.inner_width1_factor, pos5[3] * self.inner_height1_factor)
        py.draw.rect(self.screen, color1, inner_pos5)

        self.screen.blit(self.minus_img, (755,88))

        pos6=(850, 75, 105,105)
        py.draw.rect(self.screen, WHITE, pos6 )
        inner_pos6 = (pos6[0] + pos6[2] * self.inner_x1_pos_factor, pos6[1] + pos6[3] * self.inner_y1_pos_factor, pos6[2] * self.inner_width1_factor, pos6[3] * self.inner_height1_factor)
        py.draw.rect(self.screen, color1, inner_pos6)

        self.screen.blit(self.plus_img, (865,88))

        pos7=(650, 223, 95,95)
        py.draw.rect(self.screen, WHITE, pos7 )
        inner_pos7 = (pos7[0] + pos7[2] * self.inner_x1_pos_factor, pos7[1] + pos7[3] * self.inner_y1_pos_factor, pos7[2] * self.inner_width1_factor, pos7[3] * self.inner_height1_factor)
        py.draw.rect(self.screen, color1, inner_pos7)

        self.screen.blit(self.save_img, (665,240))

        pos8=(750, 223, 95,95)
        py.draw.rect(self.screen, WHITE, pos8 )
        inner_pos8 = (pos8[0] + pos8[2] * self.inner_x1_pos_factor, pos8[1] + pos8[3] * self.inner_y1_pos_factor, pos8[2] * self.inner_width1_factor, pos8[3] * self.inner_height1_factor)
        py.draw.rect(self.screen, color1, inner_pos8)

        self.screen.blit(self.record_img, (765,240))

        py.draw.rect(self.screen, WHITE, (480, 65, 235, 125), 3)

        py.draw.rect(self.screen, WHITE, (730, 65, 235, 125), 3)

        py.draw.rect(self.screen, WHITE, (540, 213, 315, 115), 3)

    def update_key_color(self, key_index, color):
        if 8 <= key_index <= 12:
            self.key_colors[key_index] = color
        else:
            self.key_colors[key_index] = color