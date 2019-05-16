#Day 29 Pie Charts, Percentages, Subplots
#Pie charts show a percentage of the whole when displayed
#Data courtesy of [http://gs.statcounter.com/os-market-share]

import matplotlib.pyplot as plt
from pylab import *

OSlabels='Android','Windows','iOS','OSX','Unknown','Linux'              #this sets our labels for the charts
market_share=[39.89,35.41,13.28,7.35,3.23,.84]                          #*note: Unknown changed to 3.23 to account for                
colors=['blue','limegreen','khaki','mediumorchid','bisque','pink']               #difference in values

mobile = 39.89 + 13.28
desktop = 35.41 + 7.35 + 3.23 + .84

TYPElabels ='Mobile','Desktop'
market_shareType = [mobile, desktop]
colorsType = ['lightblue','lightgreen']

wedgeoutline ={"edgecolor": "black","linewidth": 1,"linestyle": "solid", "antialiased": True}
class Statistical_Data:
    pass

plots = arange(0.0,17.0,1)                                              #size of the plots

plt.figure("OS Use by %, 2019")                                         #main window

histogram = subplot(2,2,1)                                              #top left
bins = [10,20,30,40,50]
plt.hist(market_share,bins,edgecolor='black',histtype='bar',rwidth=1,color='limegreen')
plt.xlabel("Market Share")
plt.ylabel("Frequency")
plt.title('Histogram')

    
pie = subplot(2,2,2)                                                    #top right
plt.pie(market_share,wedgeprops=wedgeoutline,labels=OSlabels,colors=colors,autopct='%1.1f',startangle=135)
plt.axis('equal')
plt.title('Market Share by OS and Type')

subplot(2,2,3)                                                          #bottom left
plt.figure("OS Use by %, 2019")
bins = [10,20,30,40,50]
plt.hist(market_share,bins,edgecolor='black',histtype='bar',rwidth=1,color='limegreen',orientation='horizontal')
plt.xlabel("Market Share")
plt.ylabel("Frequency")
#plt.title('Histogram')

subplot(2,2,4)                                                          #bottom right
plt.pie(market_shareType,wedgeprops=wedgeoutline,labels=TYPElabels,colors=colorsType,autopct='%1.1f',startangle=135)
plt.axis('equal')
#plt.title('Market Share')
plt.tight_layout()
plt.axis('equal')
plt.show()
