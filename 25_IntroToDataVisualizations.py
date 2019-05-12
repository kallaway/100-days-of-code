#Day 25: More Statistics Using matplotlib for a line chart, bar chart, histogram, and scatter plot
#More information available at: [https://matplotlib.org/]

import matplotlib.pyplot as plt											#imports matplotlib module
import numpy as np														      #imports numpy module

line = plt.figure(1)													      #1st figure will be a standard line, or plot, chart
x = [0,1,2,3,4,5,6,7,8,9,10,11]											#will use these throughout the application
y = [3.94,3.50,3.72,3.51,3.56,3.63,3.67,3.75,3.77,3.62,3.57,3.53]		#these are monthly corn closes, per bushel
plt.plot(x,y,label='Corn',color='firebrick')				#defines the chart: x, y axes, label, color of plot
plt.title('Monthly Closing Price of Corn\nLine Chart')					    #title at the top
plt.xlabel("Months")													      #x-axis
plt.ylabel("Corn Price/Bushel")											#y-axis
plt.legend()															          #prints a legend when dealing with more data


bar = plt.figure(2)														      #2nd figure is a bar chart
plt.bar(x,y,label='Corn', color='limegreen')				#defines x, y axes, label, and color of bars
plt.title('Monthly Closing Price of Corn\nBar Chart')					      #title at the top
plt.xlabel("Months")													      #x-axis
plt.ylabel("Corn Price/Bushel")											#y-axis
plt.legend()															          #prints a legend when dealing with more data


histogram = plt.figure(3)												    #3rd figure
bins = [3.50,3.55,3.60,3.65,3.70,3.75,3.80,3.85,3.90,3.95]				  #bins: groups of data falling within a certain range of values
plt.hist(y,bins,histtype='bar',rwidth=0.6,color='darkslateblue')		#histogram with bins, type, width, and color
plt.title("Monthly Closing Price of Corn\nHistogram")					      #title at the top
plt.xlabel("Corn Price/Bushel")											#x-axis
plt.ylabel("Frequency")													    #y-axis



scatter = plt.figure(4)													    #4th figure			
plt.scatter(x,y,color='red', marker='+')						#x, y axes, color, and the style of marker for the points
plt.title("Monthly Closing Price of Corn\nScatter Plot")				    #title at the top
plt.xlabel("Months")													      #x-axis
plt.ylabel("Corn Price/Bushel")											#y-axia
plt.show()																          #put this at bottom of program to assure data shows on multiple charts
