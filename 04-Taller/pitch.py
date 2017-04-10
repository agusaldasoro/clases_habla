#!/usr/bin/env python
# coding=utf-8
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np


def autocorr(x):
    """
    Compute the autocorrelation of the signal, based on the properties of the
    power spectral density of the signal.
    """
    xp = x - np.mean(x)
    f = np.fft.fft(xp)
    p = np.array([np.real(v)**2 + np.imag(v)**2 for v in f])
    pi = np.fft.ifft(p)
    return np.real(pi)[:x.size / 2] / np.sum(xp**2)


def freq_from_autocorr(signal, sample_rate, show_plot=False):
    corr = autocorr(signal)
    max_index = 1
    for i in range (1, corr.size):
        if corr[i]>corr[max_index]:
            max_index = i
    frequency = 1/(max_index/sample_rate)

    if show_plot:
        plt.plot(corr, "-r", label=u"correlación")
        plt.ylim([-2, 2])
        plt.title("correlation")
        plt.legend()
    return corr[max_index]


def freq_from_zcr(signal, sample_rate):
    zeros = []
    i = 0
    while len(zeros) < 2 and i < signal.size - 1:
        if signal[i]<0 and signal[i+1]>=0:
            zeros.append(i+1)
        i += 1
    periodo = (zeros[1]-zeros[0])/sample_rate
    return 1/periodo


def track(signal, step, sample_rate, method):
    # Cada un segundo tengo sample_rate cuadros
    minimum_sample = 16000
    times = []
    pitch_track = []
    # La cantidad de cuadros que representa el pitch_step es pitch_step*sample_rate
    frame_step = int(step*sample_rate)
    frames = int(signal.size / frame_step)
    for i in range (0, frames):
        index = i*frame_step
        if signal[index:].size >= minimum_sample:
            times.append(index)
            pitch = method(signal[index:][:minimum_sample], sample_rate)
            pitch_track.append(pitch)
    return times, pitch_track


def smooth_pitch(pitch_track, window):
    # COMPLETAR
    pass
