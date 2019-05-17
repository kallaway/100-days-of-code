#Day 30: Introduction to Pandas: Using data from Days 4 and 24 to create 
#csv export with the data

class statistics:
	def statisexport():
		import matplotlib.pyplot as plt			#some modules to use
		import pandas as pd						
		from random import seed					
		from random import randint 
		from pandas import DataFrame
		import math
		import statistics
		
		input("Press enter to calculate of list of 10 random numbers.")
	
		ran_set = []
	
		for i in range(1,11):					#random numbers
			val = randint(1, 1000)
			ran_set.append(val)
	
		
		print(ran_set)							#set of random numbers
		df = DataFrame(ran_set)
		Day_30 = df.to_csv(r'C:\Users\D\python_work\Day_30.csv')
		input("Now, let's see some statistics about this set.")
		
		raw_data = sorted(ran_set)				#sorted set least to greatest
		x = [1,2,3,4,5,6,7,8,9,10]
		print(raw_data)
		print(df)
		
		plt.figure('Some Random Numbers from 1-1000')
		plt.plot(x, ran_set,label='Numbers from 1-1000',linewidth='4',color='indigo')
		plt.show()
		
		
		maximum = max(raw_data)
		minimum = min(raw_data)
		rang = maximum - minimum				#range
		avg = statistics.mean(raw_data)
		med = statistics.median(raw_data)
		vari = statistics.variance(raw_data)
		std = statistics.stdev(raw_data)
	
		input("This set of random numbers has a range of " + str(rang) + ", a mean of " + str(avg) + ", a median of " + str(med) + 
		", a variance of " + str(round(vari, 2)) + ", and a standard deviation of " + str(round(std, 2)) + ".")
	

statistics.statisexport()


