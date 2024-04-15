import pygame

# Dimensiones de la ventana y colores
WIDTH = 1000
HEIGHT = 500 
BG_COLOR = (120, 39, 68)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (215, 131, 131)

# Coordenadas y dimensiones de cada tecla
KEY_WIDTH = 100
KEY_HEIGHT = 440
KEY_GAP = 10
KEY_POSITIONS = [(65 + i * (KEY_WIDTH + KEY_GAP), 260, KEY_WIDTH, KEY_HEIGHT) for i in range(8)]

KEYB_WIDTH = 75
KEYB_HEIGHT = 200
KEYB_GAP = 35
KEYB_POSITIONS = [(135 + i * (KEYB_WIDTH + KEYB_GAP), 260, KEYB_WIDTH, KEYB_HEIGHT) for i in range(2)]
KEYBA_POSITIONS = [(463 + i * (KEYB_WIDTH + KEYB_GAP), 260, KEYB_WIDTH, KEYB_HEIGHT) for i in range(3)]

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
    pygame.K_a: 0,
    pygame.K_s: 1,
    pygame.K_d: 2,
    pygame.K_f: 3,
    pygame.K_g: 4,
    pygame.K_h: 5,
    pygame.K_j: 6,
    pygame.K_k: 7,
    pygame.K_e: 8,
    pygame.K_r: 9,
    pygame.K_t: 10,
    pygame.K_y: 11,
    pygame.K_u: 12,
    pygame.K_v: 13,
    pygame.K_c: 14,
}

# Directorio de los sonidos de las notas
SCALES = ['3', '4', '5']
NOTES_FILENAMES = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'T',  'db', 'eb', 'gb', 'ab', 'bb']