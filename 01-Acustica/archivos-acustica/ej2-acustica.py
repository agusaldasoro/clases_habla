#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np
import matplotlib.pyplot as pyplot
import scipy.io.wavfile
import pylab

def ondasimple(t, f):
  return np.sin(2 * np.pi * f * t)

# Armamos una onda senoidal discretizada con f=100Hz.
def onda_senoidal(ts, frecuencia):
    mionda = []
    for t in ts:
      mionda.append(ondasimple(t, frecuencia))
    mionda = np.array(mionda)
    return mionda

# Graficamos la onda.
def graficar(ts, onda, filename):
    pyplot.clf()
    pyplot.plot(ts[0:500], onda[0:500])
    pyplot.savefig('ejercicio2/' + filename + '.png')

# La guardamos como wav.
def guardar(onda, filename):
    wavdata = np.array(onda * 10000.0, dtype=np.int16)
    scipy.io.wavfile.write('ejercicio2/' + filename + '.wav', 16000, wavdata)

# Mostramos su espectrograma.
def espectrograma(onda, filename):
    pyplot.clf()
    sgram = pylab.specgram(onda, Fs=16000.0)
    pyplot.savefig('ejercicio2/' + filename + '_espectrograma.png')

# Combinamos ambas ondas periódicas simples, para formar una onda periódica compuesta.
def generar_onda_compuesta(frecuencia1, frecuencia2, filename):
    # Generamos 16000 puntos a 16kHz.
    ts = np.arange(16000.0) / 16000.0
    onda = onda_senoidal(ts, frecuencia1) + onda_senoidal(ts, frecuencia2)
    graficar(ts, onda, filename)
    guardar(onda, filename)
    espectrograma(onda, filename)


# Ejemplo:
generar_onda_compuesta(1000, 100, 'ejemplo')

# Ejercicios:
#
# 1. Crear una onda de ruido blanco y mostrar su espectrograma.
#    Ayuda: Usar 'random.uniform(-1, 1)' del módulo random.
#
# 2. Crear una senoidal simple y combinarla con ruido blanco. Mostrar su
#    espectrograma.
#
# 3. Crear una senoidal simple con frecuencia ascendente y mostrar su
#    espectrograma.
#
# 4. Combinar dos senoidales con frecuencias 1000 y 100Hz con distintas
#    fases (ej: 0 y pi), y comparar las formas de onda. ¿Tiene algún efecto
#    perceptual el cambio de fase?
#
# 5. Crear dos senoidales simples con la misma frecuencia pero distintas
#    fases, de modo que al combinarlas se anulen.
#    http://en.wikipedia.org/wiki/Active_noise_control
