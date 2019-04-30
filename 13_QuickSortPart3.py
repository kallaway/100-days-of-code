#Day 13: Quick Sort Part 3
#Some ideas and logic from Brian Faure's youtube video "Quicksort: Background and Python Code" [https://www.youtube.com/watch?v=RFyLsF9y83c]
#Pivot can be chosen in different ways: first, last, median, random

import random															                              #imports random module
from time import sleep													                        #imports sleep module
																		                                    #random or predefined?
response = input("Would you like a random sample of numbers, or would you like to use a predifined array?\nPress R for random or P for predefined.")

flag = 0																                                #correct input = 0

if response == ("R") or response == ('r'):								              #R will give us a random list of 8 numbers
	arr = random.sample(range(0,100),8)

elif response == ("P") or response == ('p'):							              #P gives us these 8 numbers
	arr = [82, 80, 57, 26, 52, 59, 62, 21]

else:
	flag = 1															#incorrect input = 1

while flag == 1:                                                        #this will loop until we have a correct input
		response = input("You have entered an incorrect number. Please enter R for random or P for predefined.")	
		if response == ("R") or response == ('r'):
			arr = random.sample(range(0,100),8)
			flag = 0
		elif response == ("P") or response == ('p'):
			arr = [82, 80, 57, 26, 52, 59, 62, 21]
			flag = 0
print(arr)																`                             #the array

def sort(arr):
	length = len(arr)													                            #length of the list
	index = length - 1													                          #index of the last number
	if length <= 1: 
		return arr														                              #this will eventually terminate the program
	left, pivots, right = [],[],[]
	p = arr[index]														                            #here's our pivot: last number in list
	
	for x in arr:														                              #for a number in the list...
		if x<p: 
			left.append(x)												                            #less than pivot, throw it in the left list
		elif x==p:
			pivots.append(x)											                            #equal to pivot(or a pivot), throw it in the middle
		else:
			right.append(x)												                            #more than pivot, throw it to the right
		print(" ")
		print(left)														                              #let's watch it in action...
		print(pivots)													                              #as the temp arrays change
		print(right)
		print(arr)
		sleep(1)														
	return sort(left) + pivots + sort(right)							                #sort() concatenates and returns all three arrays
outputarr = sort(arr)													                          #output array is the function return
print(" ")
print(outputarr)														                            #print it for the user
