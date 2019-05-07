#Day 20: Iterative and Recursive Functions-Function to determine closing time based on average profit / hour of business in a coffee shop
import math 

def avg_profit_mult(hour):
	total = sum(hour) * .6
	return total
	
hour = [[6.99, 4.95, 8.55, 3.99, 4.95, 4,99, 7.50, 11.99, 5.50, 4.95, 4.95, 7.50, 6.99, 3.99], [5.99, 4.95, 3.99, 11.55, 7.50, 7.50, 7.50, 5.50, 4.95, 3.99, 3.99],
[3.99, 4.95, 11.55, 5.50, 4.95, 5.99, 5.99], [4.95, 11.95, 3.99, 3.99], [3.99, 4.95, 4.95], [4.95, 7.50], [3.99]] 

def printprof(hour):													#iterative
	for n in range(1,8):
		prof = round(avg_profit_mult(hour[n]),2)
		if prof <= 10.00:
			return n
			break

close = printprof(hour)													#calls function

for i in range(1,8):													
	if close == i:
		print("OPTIMAL CLOSING TIME:  " + str(i + 4) + " PM " )			#n index + 4 is our optimal closing time

input()

n = len(hour)-1

def profit_recursion(hour):												#recursive												
	
	global n															#calls one global variable
	if (sum(hour[n]) * .6) > 10:										#base case
		return n + 1
	else:																#recursive case
		n = n-1
		return profit_recursion(hour)

close = profit_recursion(hour)											#calls function

for i in range(1,8):
	if close == i:
		print("OPTIMAL CLOSING TIME:  " + str(i + 4) + " PM " )			#n index + 4 is our optimal closing time		

input()
