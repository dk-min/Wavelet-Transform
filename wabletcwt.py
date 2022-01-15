import numpy as np
import matplotlib.pyplot as plt

import obspy
from obspy.imaging.cm import obspy_sequential
from obspy.signal.tf_misfit import cwt

import pandas as pd

Fs = 100 #Sampling Freq is 100Hz
Ts = 1/Fs

header = ['bcg_raw', 'bcg_iir', 'bcg_norm','ppg_raw', 'ppg_iir', 'ppg_norm'] #index
rdr = pd.read_csv('.\ppg_bcg_norm.txt',  names=header)

raw_data = rdr['bcg_raw']
iir_data = rdr['bcg_iir']
norm_data = rdr['bcg_norm']

t = np.linspace(0, Ts * len(raw_data), len(raw_data))
f_min = 0.1
f_max = 50

scalogram = cwt(raw_data, Ts, 6, f_min, f_max)

fig = plt.figure()
ax = fig.add_subplot(211)

x, y = np.meshgrid(
    t,
    np.logspace(np.log10(f_min), np.log10(f_max), scalogram.shape[0]))

ax.pcolormesh(x, y, np.abs(scalogram), cmap=obspy_sequential)
ax.set_xlabel("Time")
ax.set_ylabel("Frequency [Hz]")
ax.set_yscale('log')
ax.set_ylim(f_min, f_max)

bx = fig.add_subplot(212)
bx.plot(t, raw_data)
plt.show()