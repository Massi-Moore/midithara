import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import fftconvolve

# Configuración de la señal
frecuencia = 220  # Frecuencia en Hz
duracion = 3 / 440  # Duración en segundos para 3 ondas
muestras_por_segundo = 44100  # Número de muestras por segundo

# Generar el tiempo y la señal
tiempo = np.linspace(0, duracion, int(duracion * muestras_por_segundo))
señal = np.sin(2 * np.pi * frecuencia * tiempo)

# Crear un impulso de reverberación simple
reverb_impulse = np.zeros(muestras_por_segundo)
reverb_impulse[::muestras_por_segundo//10] = 1
reverb_impulse /= reverb_impulse.sum()

# Aplicar la reverberación a la señal mediante la convolución
señal_reverb = fftconvolve(señal, reverb_impulse, mode='same')

# Graficar la señal original y la señal con reverberación
plt.figure(figsize=(3,0.8), facecolor=(220/255, 197/255, 196/255))  # Ajustar el tamaño de la figura
plt.plot(tiempo, señal, color=(129/255, 70/255, 80/255), alpha=0.5, label='Original')
plt.plot(tiempo, señal_reverb, color=(129/255, 70/255, 80/255), label='Reverb')
plt.grid(True)
plt.axis('off')  # Eliminar los ejes
plt.savefig('waveform_a3_reverb.png', dpi=100, bbox_inches='tight', transparent=True, facecolor=(220/255, 197/255, 196/255))
plt.show()