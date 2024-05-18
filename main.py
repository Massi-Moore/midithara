# main.py
import pygame as py
import serial
import threading
from piano import Piano
from sound import SoundManager
from constants import *
from serial.tools import list_ports
import time

py.init()

def find_arduino_port():
    ports = list_ports.comports()
    for port in ports:
        try:
            ser = serial.Serial(port.device, 9600, timeout=1)
            time.sleep(0.5)  
            while True:
                line = ser.readline().decode('utf-8').strip()
                if line == "Arduino Piano":
                    ser.write("Arduino Found".encode('utf-8'))  
                    return ser
                elif not line:
                    break
            ser.close()
        except serial.SerialException:
            pass
    return None

BLACK_KEYS = {8, 9, 10, 11, 12}
current_scale_index = 1
volume = 1

def change_key_color(piano, key_index, color, delay):
    piano.update_key_color(key_index, Key_Light)
    piano.update_inner_key_color(key_index, green)  # Agrega esta línea
    py.time.wait(delay)
    color = BLACK if key_index in BLACK_KEYS else WHITE
    piano.update_key_color(key_index, color)
    piano.update_inner_key_color(key_index, color3)  # Agrega esta línea

def read_serial(piano, sound_manager):
    global current_scale_index
    global volume
    global ser
    global serial_available

    ser = find_arduino_port()
    if ser is None:
        print("No se encontró el Arduino")
        serial_available = False
    else:
        print("Arduino encontrado en el puerto", ser.port)
        serial_available = True

    while True:
        try:
            if ser is not None and ser.in_waiting:
                serial_input = ser.readline().decode('ascii').strip()
                if serial_input.isdigit():
                    key_index = int(serial_input)
                    if key_index in KEY_MAPPING:
                        threading.Thread(target=change_key_color, args=(piano, key_index, Key_Light, 350)).start()
                        sound_manager.play_sound(key_index)
                    elif key_index == 17:
                        current_scale_index = (current_scale_index + 1) % len(SCALES)
                        sound_manager.set_scale(SCALES[current_scale_index])
                    elif key_index == 18:
                        volume = max(0, volume - 0.1)
                        sound_manager.set_volume(volume)
                    elif key_index == 19:
                        volume = min(1, volume + 0.1)
                        sound_manager.set_volume(volume)
                    elif key_index == 16:
                        sound_manager.toggle_effect(SCALES[current_scale_index])

        except (UnicodeDecodeError, serial.SerialException):
            print("Se perdió la conexión con el Arduino")
            ser = None
            serial_available = False

        if not serial_available:
            ser = find_arduino_port()
            if ser is not None:
                print("Arduino encontrado en el puerto", ser.port)
                serial_available = True
            else:
                time.sleep(1)  # Espera un segundo antes de intentar de nuevo

def main():
    screen = py.display.set_mode((WIDTH, HEIGHT))
    py.display.set_caption('Midithara')
    
    sound_manager = SoundManager(SCALES[current_scale_index])
    piano = Piano(screen, sound_manager)
    global BLACK_KEYS

    serial_thread = threading.Thread(target=read_serial, args=(piano, sound_manager))
    serial_thread.daemon = True  # Hace que el hilo sea un hilo daemon
    serial_thread.start()

    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                if ser is not None:
                    ser.close()  # Cierra la conexión serial
            elif event.type == py.KEYDOWN:
                if event.key in KEY_MAPPING:
                    key_index = KEY_MAPPING[event.key]
                    threading.Thread(target=change_key_color, args=(piano, key_index, Key_Light, 350)).start()
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
