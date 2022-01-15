import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

header = ['bcg_raw', 'bcg_iir', 'bcg_norm','ppg_raw', 'ppg_iir', 'ppg_norm']
rdr = pd.read_csv('./ppg_bcg_norm.txt',  names=header)

raw_data = rdr['bcg_raw']
iir_data = rdr['bcg_iir']
norm_data = rdr['bcg_norm']

plt.subplot(1,3,1)
plt.plot(raw_data)
plt.xlim(100, 300)
#plt.ylim(0,3.3)

plt.subplot(1,3,2)
plt.plot(iir_data)
plt.xlim(100+15, 300+15)
#plt.ylim(-1.65,1.65)

plt.subplot(1,3,3)
plt.plot(norm_data)
plt.xlim(100+15, 300+15)
#plt.ylim(-1.65,1.65)

plt.show()