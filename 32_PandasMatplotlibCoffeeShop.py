#Day 32: Pandas cont. Today and tomorrow I will be going back over the data from Day 20: Coffee Shop Closing 
#Time. 

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np
import math
import inline

df = pd.read_csv('coffeeshop_totalsales.csv', index_col='Hour')
print(df)
print(" ")
print(df.info())
print(" ")
print(df.shape)
print(" ")

x = df.iloc[:]
print(x)
print(" ")
temp_df = df.append(df)
print(temp_df.shape)
print(" ")
temp_df = temp_df.drop_duplicates()
print(temp_df.shape)
print(" ")
 
def avg_profit_mult(hour):
	total = sum(hour) * .6
	return total
	
hour = [[6.99, 4.95, 8.55, 3.99, 4.95, 4,99, 7.50, 11.99, 5.50, 4.95, 4.95, 7.50, 6.99, 3.99], 
[5.99, 4.95, 3.99, 11.55, 7.50, 7.50, 7.50, 5.50, 4.95, 3.99, 3.99],
[3.99, 4.95, 11.55, 5.50, 4.95, 5.99, 5.99], [4.95, 11.95, 3.99, 3.99], [3.99, 4.95, 4.95], 
[4.95, 7.50], [3.99]] 

def printprof(hour):													#iterative
	for n in range(1,8):
		prof = round(avg_profit_mult(hour[n]),2)
		if prof <= 10.00:
			return n
			break

close = printprof(hour)													#calls function

for i in range(1,8):													
	if close == i:
		print("\nOPTIMAL CLOSING TIME:  " + str(i + 4) + " PM " )			#n index + 4 is our optimal closing time

print(" ")        
plt.figure("Optimal Closing Time")
plt.plot()
plt.xlabel("Hour")
plt.ylabel("Sales in $")
plt.legend()
plt.show()
