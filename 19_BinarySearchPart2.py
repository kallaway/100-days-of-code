#Day 19: Binary Search Continued

import statistics
from time import sleep

arr = []

for var in range(1,11):													#1-10, remember, last element will be one less
    
    arr.append(var)														#add each value to end of list in order
    

print(arr)																#show user the list

pick = input("Please enter a number between 1-100 and let the computer search for it.")
pick = int(pick)														#pick a number




def binary_search(pick, arr):											#function
	left, right = 0, len(arr)-1											#moves in on it starting at both sides, len(arr)-1 should be last value
	while left <= right:												#while we are iterating through the list...			
		middle = left + (right - left)//2
		middle_value = arr[middle]						
		if middle_value == pick:
			return arr[middle]											#if correct right return to main program the answer
		elif middle_value < pick:
			left = middle + 1											#if pick is on the right move the left over
		else:
			right = middle - 1											#if pick is on the left move the right over
	return -1															#out-of-range

result = binary_search(pick, arr)

input()
if result >= 0:
    print("The number " + str(result) + " has been found in our list.")	#has been found
else:
    print("Your number, " + str(pick) + " has not been found on our list.")	
																		#has not been found
 
