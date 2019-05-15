

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import cv2 as cv

Q = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170]
PS = []
PD = []

for num in Q:
    pslist = num
    PS.append(pslist)
for numb in Q:
	pdlist = max(Q)-numb
	PD.append(pdlist)
		
	
img =  cv.imread("world_map.jpg")
img = cv.resize(img, (175,175))

plt.figure('Supply and Demand',figsize=(10.36,8))
plt.xkcd()

plt.imshow(img)
plt.title('World Supply and Demand for Our Widget \n2018')
plt.plot(Q,PS,label='Supply',linewidth='3',color='maroon')
plt.plot(Q,PD,label='Demand',linewidth='3', color='forestgreen')

plt.xlabel('Quantity')
plt.ylabel('Price')
plt.legend()
plt.gca().invert_yaxis()
plt.annotate('equilibrium', xy=(80,80), arrowprops=dict(arrowstyle='->'))
plt.show()
