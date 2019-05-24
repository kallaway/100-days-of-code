import matplotlib.pyplot as plt
import numpy as np

input()

print("Light waves tending towards the red end of the visible spectrum have a lower frequency than those near the blue end of the spectrum.") 
print("This, considering cosmic proportions of scale, results in the fact that galaxies moving away from us (most) will appear red to the ")
print("human eye, whereas galaxies moving towards us (Andomeda for instance) will appear blue. The same effect occurs when measuring sound.")
input("Let's see why.")





plt.figure('Doppler Effect')                    #Doppler Effect: Red Shift/        
                                                #Blue Shift

red = np.arange(0, 10, .1)
blue = np.arange(0, 20, .1)
ramp = np.sin(red)
bamp = np.sin(blue)

red_shift = plt.subplot(2,1,1)                  #Top Plot
plt.title('Red Shift / Blue Shift')
plt.ylabel('Amplitude')
#plt.grid(color = 'black', linestyle = '--', linewidth = .5)
plt.annotate('', xy=(6,.5), xytext = (4,.5), arrowprops=dict(arrowstyle="->")) 
plt.plot(red, ramp, color='crimson')
plt.axis('off')
plt.axhline(y=0, color='black')

blue_shift = plt.subplot(2,1,2)                 #Bottom Plot
plt.xlabel('Wavelength')
plt.ylabel('Amplitude')
#plt.grid(color = 'black', linestyle = '--', linewidth = .5)
plt.annotate('', xy=(8,.5), xytext = (12,.5), arrowprops=dict(arrowstyle="->"))
plt.plot(blue, bamp, color='dodgerblue')
plt.axis('off')
plt.axhline(y=0, color='black')

plt.show()                                      #Presents Graph
