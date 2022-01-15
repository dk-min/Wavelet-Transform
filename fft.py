import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Fs = 100 #Sampling Freq is 100Hz
Ts = 1/Fs

header = ['bcg_raw', 'bcg_iir', 'bcg_norm','ppg_raw', 'ppg_iir', 'ppg_norm'] #index
rdr = pd.read_csv('./ppg_bcg_norm.txt',  names=header)

raw_data = rdr['bcg_raw']
iir_data = rdr['bcg_iir']
norm_data = rdr['bcg_norm']

y = iir_data

n = len(y) 					# length of the signal
k = np.arange(n)
T = n/Fs
freq = k/T 					# two sides frequency range
freq = freq[range(int(n/2))] 			# one side frequency range

Y = np.fft.fft(y)/n 				# fft computing and normalization
Y = Y[range(int(n/2))]

fig, ax = plt.subplots(2, 1)
ax[0].plot(k, y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].grid(True)
ax[1].plot(freq, abs(Y), 'r', linestyle=' ', marker='^') 
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[1].vlines(freq, [0], abs(Y))
ax[1].grid(True)
plt.show()