import pygame as py

# Dimensiones de la ventana y colores
WIDTH = 1000
HEIGHT = 625 
BG_COLOR = (45,39,55)
KEY_BG_COLOR = (63,59,73)
WHITE = (187,109,123)
BLACK = (129,70,80)
Key_Light = (215, 131, 131)
color3=(241,219,218)
green=(173,252,200)

font_title_color=(117,117,124)

# Coordenadas y dimensiones de cada tecla
KEY_WIDTH = 85
KEY_HEIGHT = 85
KEY_GAP = 10
KEY_POSITIONS = [(120 + i * (KEY_WIDTH + KEY_GAP), 450, KEY_WIDTH, KEY_HEIGHT) for i in range(8)]
color1=(232,182,194)


KEYB_WIDTH = 85
KEYB_HEIGHT = 85
KEYB_GAP = 10
KEYB_POSITIONS = [(180 + i * (KEYB_WIDTH + KEYB_GAP), 359, KEYB_WIDTH, KEYB_HEIGHT) for i in range(2)]
KEYBA_POSITIONS = [(460 + i * (KEYB_WIDTH + KEYB_GAP), 359, KEYB_WIDTH, KEYB_HEIGHT) for i in range(3)]
color2=(162,87,101)


# Asignación de teclas de piano a teclas del teclado
KEY_MAPPING = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    py.K_a: 0,
    py.K_s: 1,
    py.K_d: 2,
    py.K_f: 3,
    py.K_g: 4,
    py.K_h: 5,
    py.K_j: 6,
    py.K_k: 7,
    py.K_e: 8,
    py.K_r: 9,
    py.K_t: 10,
    py.K_y: 11,
    py.K_u: 12,
}

# Directorio de los sonidos de las notas
SCALES = ['3', '4', '5']
NOTES_FILENAMES = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'T',  'db', 'eb', 'gb', 'ab', 'bb']