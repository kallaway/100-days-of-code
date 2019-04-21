#Day 4: Statistics
from random import seed					      #random module
from random import randint 
import statistics 

input()

for i in range(1,11):					        #random numbers
	
	if i == 1:
		var1 = randint(1, 1000)
	if i == 2:
		var2 = randint(1, 1000)
	if i == 3:
		var3 = randint(1,1000)
	if i == 4:
		var4 = randint(1,1000)
	if i == 5:
		var5 = randint(1,1000)
	if i == 6:
		var6 = randint(1,1000)
	if i == 7:
		var7 = randint(1,1000)
	if i == 8:
		var8 = randint(1,1000)
	if i == 9:
		var9 = randint(1,1000)
	if i == 10:
		var10 = randint(1,1000)
										                  #list of the numbers
ran_set = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10]

print(ran_set)							          #set of random numbers

raw_data = sorted(ran_set)				    #sorted set least to greatest

print(raw_data)

maximum = max(raw_data)
minimum = min(raw_data)
rang = maximum - minimum				      #range

avg = statistics.mean(raw_data)
med = statistics.median(raw_data)
#mod = statistics.mode(raw_data)		  #probably no mode out of 10 random values between 1-1000
vari = statistics.variance(raw_data)
std = statistics.stdev(raw_data)

print("This set of random numbers has a mean of " + str(avg) + ", a median of " + str(med) + 
", a variance of " + str(vari) + ", and a standard deviation of " + str(std) + ".")
