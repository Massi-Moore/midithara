import pygame
import os

# Dimensiones de la ventana y colores
WIDTH = 1000
HEIGHT = 500 
bg = (38, 20, 32)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Coordenadas y dimensiones de cada tecla
key_width = 100
key_height = 300
key_gap = 10
key_positions = [(100 + i * (key_width + key_gap), 200, key_width, key_height) for i in range(7)]

# Asignación de teclas de piano a teclas del teclado
key_mapping = {
    pygame.K_a: 0,
    pygame.K_s: 1,
    pygame.K_d: 2,
    pygame.K_f: 3,
    pygame.K_g: 4,
    pygame.K_h: 5,
    pygame.K_j: 6
}

# Estado inicial de las teclas (todas en blanco)
key_colors = {key: white for key in key_mapping.values()}

# Cargar los sonidos de las notas
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(128)  # Ajusta el número de canales según sea necesario
notes_folder = 'notes'
notes_filenames = ['a4.wav', 'f4.wav', 'g4.wav', 'e4.wav', 'b4.wav', 'c4.wav', 'd4.wav']
notes_sounds = [pygame.mixer.Sound(os.path.join(notes_folder, filename)) for filename in notes_filenames]

# Ajustar el volumen de los sonidos
for sound in notes_sounds:
    sound.set_volume(0.5)  # Puedes ajustar este valor según tus preferencias

piano = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Midithara')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key in key_mapping:
                key_index = key_mapping[event.key]
                key_colors[key_index] = red
                notes_sounds[key_index].play()
        elif event.type == pygame.KEYUP:
            if event.key in key_mapping:
                key_index = key_mapping[event.key]
                key_colors[key_index] = white

    piano.fill(bg)
    for i, pos in enumerate(key_positions):
        pygame.draw.rect(piano, key_colors[i], pos)

    pygame.display.update()

pygame.mixer.quit()  # Liberar recursos de sonido
pygame.quit()
