# main.py
import pygame as py
import serial
import threading
from piano import Piano
from sound import SoundManager
from constants import *

py.init()

try:
    ser = serial.Serial('COM3', 9600)  # Asegúrate de reemplazar 'COM3' con el puerto correcto
    serial_available = True
except serial.SerialException:
    serial_available = False# Asegúrate de reemplazar 'COM3' con el puerto correcto

BLACK_KEYS = {8, 9, 10, 11, 12}

def change_key_color(piano, key_index, color, delay):
    piano.update_key_color(key_index, GREEN)
    py.time.wait(delay)
    color = BLACK if key_index in BLACK_KEYS else WHITE
    piano.update_key_color(key_index, color)

def read_serial(piano, sound_manager):
    while True:
        if ser.in_waiting:
            try:
                serial_input = ser.read().decode('ascii').strip()
                if serial_input.isdigit():
                    key_index = int(serial_input)
                    if key_index in KEY_MAPPING:
                        threading.Thread(target=change_key_color, args=(piano, key_index, GREEN, 500)).start()
                        sound_manager.play_sound(key_index)
                elif serial_input == 'p':  # Mensaje de liberación
                    for key in KEY_MAPPING.values():
                        color = BLACK if key in BLACK_KEYS else WHITE
                        threading.Thread(target=change_key_color, args=(piano, key_index, color, 500)).start()
            except UnicodeDecodeError:
                pass  # Ignora los errores de decodificación

# ... el resto de tu código ...

def main():
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption('Midithara')

    current_scale_index = 1  # Inicia en la escala 4
    piano = Piano(screen)
    sound_manager = SoundManager(SCALES[current_scale_index])
    BLACK_KEYS = {8, 9, 10, 11, 12}

    if serial_available:
        threading.Thread(target=read_serial, args=(piano, sound_manager)).start()

    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.KEYDOWN:
                if event.key == py.K_m:  # Detiene todos los sonidos cuando se presiona 'M'
                    sound_manager.stop_sounds()
                elif event.key == py.K_n:  # Cambia la escala cuando se presiona 'N'
                    current_scale_index = (current_scale_index + 1) % len(SCALES)
                    sound_manager.set_scale(SCALES[current_scale_index])  # Cambia la escala
                elif event.key in KEY_MAPPING:
                    key_index = KEY_MAPPING[event.key]
                    threading.Thread(target=change_key_color, args=(piano, key_index, GREEN, 500)).start()
                    sound_manager.play_sound(key_index)
            elif event.type == py.KEYUP:
                if event.key in KEY_MAPPING:
                    key_index = KEY_MAPPING[event.key]
                    color = BLACK if key_index in BLACK_KEYS else WHITE
                    piano.update_key_color(key_index, color)
                    
        piano.draw(SCALES[current_scale_index])  # Pasa la escala actual al método draw
        py.display.update()

    sound_manager.stop_sounds()
    py.quit()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()