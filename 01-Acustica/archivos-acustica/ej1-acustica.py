#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np
import matplotlib.pyplot as pyplot
import scipy.io.wavfile

contador = 0

# Definimos una función senoidal simple.
def ondasimple(t, f):
  A = 1.0    # amplitud
  # f = 500.0  # frequencia
  Phi = 0.0  # fase
  return A * np.sin(2 * np.pi * f * t + Phi)

def generar_onda(frec):
  # Generamos 16000 puntos a 16kHz.
  ts = np.arange(16000.0) / 16000.0
  # Armamos una onda senoidal discretizada.
  onda = []
  for t in ts:
    onda.append(ondasimple(t, frec))
  onda = np.array(onda)
  global contador
  contador += 1
  return [ts, onda]

def guardar(onda, archivo):
  # La guardamos como wav.
  wavdata = np.array(onda * 10000.0, dtype=np.int16)
  scipy.io.wavfile.write(archivo + '.wav', 16000, wavdata)

def graficar(ts, onda, archivo):
  # Graficamos la onda.
  pyplot.clf()
  pyplot.plot(ts[0:100], onda[0:100])
  pyplot.savefig(archivo + '.png')

def procesar_onda(frec, archivo):
  ts_onda = generar_onda(frec)
  guardar(ts_onda[1], archivo)
  graficar(ts_onda[0], ts_onda[1], archivo)

# Ejemplo:
procesar_onda(500.0, 'mionda')

# Ejercicios:
#
# 1. Generar un archivo wav para cada nota musical Do, Re, Mi,
#    Fa, Sol, La, Si. Consultar las frecuencias en
#    http://www.phy.mtu.edu/~suits/notefreqs.html
#    Tomar como referencia La = 440Hz.
#
# DO
procesar_onda(261.63, 'do')
# RE
procesar_onda(293.66, 're')
# MI
procesar_onda(329.63, 'mi')
# FA
procesar_onda(349.23, 'fa')
# SOL
procesar_onda(392.00, 'sol')
# LA
procesar_onda(440.0, 'la')
# SI
procesar_onda(493.88, 'si')

# 2. Buscar la frecuencia más aguda y más grave que pueden percibir.
#
# 3. Percepcion relativa. Escuchar la diferencia entre dos tonos graves
#    separados por 100Hz (ej: 200 y 300Hz) y dos tonos agudos separados
#    también por 100Hz (ej: 1200 y 1300Hz).
#
# 4. Crear una onda cuadrada a 500 Hz, modificando ondasimple(t) de modo
#    que devuelva solamente 1 o -1. Generar un wav y comparar con una
#    senoidal de la misma frecuencia.
#
# 5. Repetir el punto anterior para 100Hz y para 1000Hz. ¿En algún caso
#    suenan parecidas las ondas senoidales y cuadradas? (Más allá de las
#    diferencias de volumen).

