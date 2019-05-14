#Day 27: matplotlib and plotting supply and demand graph with equilibrium

import pytesseract
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import cv2 as cv
eq = 5
Q = [0,100,200,300,400,500,600,700,800,900,1000]
PS = []
PD = []

for num in Q:
    pslist = num
    PS.append(pslist)
for num in Q:
    pdlist = max(Q)-num
    PD.append(pdlist)
img =  cv.imread("world.jpg")  

plt.figure('Supply and Demand',figsize=(10.36,7.66))
#plt.imshow(img)
plt.plot(Q,PS,label='Supply',linewidth='3',color='red')
plt.plot(Q,PD,label='Demand',linewidth='3', color='green')

plt.xlabel('Quantity')
plt.ylabel('Price')
plt.legend()

plt.annotate('equilibrium', xy=(500,500), arrowprops=dict(arrowstyle='->'))
plt.show()
