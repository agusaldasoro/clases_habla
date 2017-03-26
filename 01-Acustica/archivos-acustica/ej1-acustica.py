#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np
import matplotlib.pyplot as pyplot
import scipy.io.wavfile


# Definimos una función senoidal simple.
def ondasimple(t, frecuencia):
  A = 1.0    # amplitud
  Phi = 0.0  # fase
  return A * np.sin(2 * np.pi * frecuencia * t + Phi)

# Definimos una función senoidal simple.
def ondacuadrada(t, frecuencia):
  A = 1.0    # amplitud
  Phi = 0.0  # fase
  modT = t % frecuencia
  signo = -1.0 if modT > 0.5 else 1.0
  print(signo)
  return signo

def generar_onda(frec, cuadrada=False):
  # Generamos 16000 puntos a 16kHz.
  ts = np.arange(16000.0) / 16000.0
  # Armamos una onda senoidal discretizada.
  onda = []
  for t in ts:
    if cuadrada:
        onda.append(ondacuadrada(t, frec))
    else:
        onda.append(ondasimple(t, frec))
  onda = np.array(onda)
  return [ts, onda]

# La guardamos como wav.
def guardar(onda, archivo):
  wavdata = np.array(onda * 10000.0, dtype=np.int16)
  scipy.io.wavfile.write('ejercicio1/' + archivo + '.wav', 16000, wavdata)

# Graficamos la onda.
def graficar(ts, onda, archivo):
  pyplot.clf()
  pyplot.plot(ts[0:100], onda[0:100])
  pyplot.savefig('ejercicio1/' + archivo + '.png')

# Generar, graficar y guardar onda
def procesar_onda(frec, archivo, cuadrada=False):
  ts_onda = generar_onda(frec, cuadrada)
  guardar(ts_onda[1], archivo)
  graficar(ts_onda[0], ts_onda[1], archivo)

# Ejemplo:
procesar_onda(500.0, 'ejemplo')

# Ejercicios:
# 1. Generar un archivo wav para cada nota musical Do, Re, Mi,
#    Fa, Sol, La, Si. Consultar las frecuencias en
#    http://www.phy.mtu.edu/~suits/notefreqs.html
#    Tomar como referencia La = 440Hz.
procesar_onda(261.63, 'do')
procesar_onda(293.66, 're')
procesar_onda(329.63, 'mi')
procesar_onda(349.23, 'fa')
procesar_onda(392.00, 'sol')
procesar_onda(440.0, 'la')
procesar_onda(493.88, 'si')

# 2. Buscar la frecuencia más aguda y más grave que pueden percibir.
# Grave (mas grave se escucha raro)
procesar_onda(10, 'grave')
procesar_onda(799790, 'agudo')

# 3. Percepcion relativa. Escuchar la diferencia entre dos tonos graves
#    separados por 100Hz (ej: 200 y 300Hz) y dos tonos agudos separados
#    también por 100Hz (ej: 1200 y 1300Hz).
procesar_onda(200, 'grave1')
procesar_onda(300, 'grave2')
procesar_onda(1200, 'agudo1')
procesar_onda(1300, 'agudo2')

# 4. Crear una onda cuadrada a 500 Hz, modificando ondasimple(t) de modo
#    que devuelva solamente 1 o -1. Generar un wav y comparar con una
#    senoidal de la misma frecuencia.

# procesar_onda(300, 'cuadrada', True)

# 5. Repetir el punto anterior para 100Hz y para 1000Hz. ¿En algún caso
#    suenan parecidas las ondas senoidales y cuadradas? (Más allá de las
#    diferencias de volumen).
