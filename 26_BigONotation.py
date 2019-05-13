#Day 26: Big O Notation Graphed

import numpy as np
import matplotlib.pyplot as plt
import math

x = [0,1,2,3,4,5,6,7]                                       #x inputs
yexp = []                                                   #v y outputs as time growth defined in each list v
yqud = []
ylin = []
ylog = []
ycst = []
for num in range(0,len(x)):
    num = math.pow(2,num)
    yexp.append(num)
for num in range(0,len(x)):
    num = num**2
    yqud.append(num)
for num in range(0,len(x)):
    ylin.append(num)
for num in range(0,len(x)):
    if num == 0:
        ylog.append(num)
    else:
        num = math.log(x[num],2)
        ylog.append(num)
for num in range(0,len(x)):
    num = 1
    ycst.append(num)
    
plt.figure('Big O Notation')                                #outputs to matplotlib
plt.plot(x,yexp, label='Exponential  O(2^n)', linewidth='3', color='red')
plt.plot(x,yqud, label='Quadratic  O(n^2)', linewidth='3', color='orange')
plt.plot(x,ylin, label='Linear  O(n)', linewidth='3', color='blue')
plt.plot(x,ylog, label="Logarithmic  (log n)", linewidth='3', color='purple')
plt.plot(x,ycst, label='Constant  O(1)', linewidth='3', color='green')
plt.xlabel('Elements in Search')
plt.ylabel('Time')
plt.title('Time Increase as Sample Size Increases', color='teal')
plt.legend()
plt.show()
