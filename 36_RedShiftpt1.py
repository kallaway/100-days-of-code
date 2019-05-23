#Day 36: Initiate Red Shift / Blue Shift Idea



import matplotlib.pyplot as plt 
#import pandas as pd
import numpy as np

red = np.arange(0, 10, .1);
blue = np.arange(0, 10, .1)
amp = np.sin(1/red)
AMP = np.sin(blue)
plt.figure('Work in Progress - Red Shift / Blue Shift')
plt.plot(red, amp, label='Red Shift', color = 'deeppink')
plt.plot(blue, AMP, label='Blue Shift', color = 'darkblue')
plt.title('Doppler Effect')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(color = 'black', linestyle = '--', linewidth = 1)
plt.axhline(y=0, color='black')
plt.show()
