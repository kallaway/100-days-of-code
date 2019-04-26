Day 9: Sorting Algorithms-BubbleSort
#Ideas from Coding Blocks Youtube Channel Episode 84: Algorithms You Should Know
#https://www.youtube.com/watch?v=5R80MfMxtx4&list=PLWWyzc5ehM92EyZYAL5e5i2zfVqeXY0DA&index=13&t=0s

#--------------------------------------------------------------------------------------------------------------------+
#1 Bubble Sort: iterates through list, swapping each if in incorrect order
#  easiest to implement and understand but very inefficient  
#  time to code=fast; time to run=slow; memory required=average

from time import sleep  

sample = [9,7,11,5,20,7,14,19,12,10,4,7,19,9,17,20,10,4,6,10]					#this is a set of random numbers between 1-20
n = len(sample)																	                      #number of elements in the sample, in this case 20

print(sample)																	                        #beginning value

def bubble(sample):																                    #defines bubble() method
	for x in range(n-1,0,-1):													                  #start with 19, end with 0, increment down by 1
		for i in range(x):														                    #i counts 
			if sample[i]>sample[i+1]:											                  #performing iterations
				tempvalue=sample[i]
				sample[i] = sample[i+1]
				sample[i+1] = tempvalue 										                  #loop restarts until the value is met
				print(sample)													                        #prints current list
				sleep(1)														                          #pauses for 1 second
print(" ")
print(" ")				
print("BUBBLE SORT")
print(" ")
				
bubble(sample)
																				                              #calls bubble() function
print(sample)
																				                              #prints final sample
input()

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
sample = [9,7,11,5,20,7,14,19,12,10,4,7,19,9,17,20,10,4,6,10]
	

            
n = len(sample)																	                      #number of elements in the sample, in this case 20

print(sample)																	                        #beginning value

def bubble(sample):																                    #defines bubble() method
	for x in range(n-1,0,-1):													                  #start with 19, end with 0, increment down by 1
		for i in range(x):														                    #i counts 
			if sample[i]>sample[i+1]:											                  #performing iterations
				tempvalue=sample[i]												
				sample[i] = sample[i+1]
				sample[i+1] = tempvalue 										                  #loop restarts until the value is met 
				
	
print(" ")
print(" ")				
print("BUBBLE SORT")
print(" ")				
bubble(sample)																	                      #calls bubble() function
print(sample)			
	
#--------------------------------------------------------------------------------------------------------------------+
