#Day 33: Python Coffee Shop Part 3

import pandas as pd                                                   #pandas for spreadsheet input
import matplotlib.pyplot as plt                                       #matplotlib for chart
from pandas import DataFrame                                          #in case we need df


coffee_shop = pd.read_csv('coffeeshop_totalsales.csv')                #sales in our coffee shop
print(coffee_shop)                                                    #prints it out
print(" ")
print(" ")
print("Optimal Closing Time")                                         #Title in Jupyter        

plt.figure("Optimal Closing Time")                                    #Title from console
plt.plot(coffee_shop.Hour, coffee_shop.Sales, label='Sales/hour', color='green')
plt.hlines(10/.6, 0, 6, colors='red')                                 #plot y value and a horizontal y line
plt.xlabel("Hour")                                                    #x-axis
plt.ylabel("Sales in $")                                              #y-axia
plt.legend()                                                          #legend for the chart
plt.show()                                                            #shows chart output
