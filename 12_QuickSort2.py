#Day 12: The Quick Sort Part 2
#
from random import randint 
from time import sleep

n = input("Please enter the of amount of numbers that you would like in your list. ")
n = int(n)

count = n - 1																			#index of the last number in the array

arr = []

for i in range(0,n):																	#this for loop generates n random numbers for our sort
	rand = randint(1,100)																#random integer between 1 - 100
	arr.append(rand)																	#puts new element at the end
	
n = len(arr)
print(arr)																				#let's start by seeing what our list looks like
input()

																					
p = n - 1
m = 0
k = -2
for i in range(0,n):
	print(arr)
	if m == k:
		break
	k = p - 1				# m              k    p
	pivot = arr[p]			#54 , 79 , 77 , 91 , 36
	mover = arr[m]			#91 , 79 , 77 , 36 , 54
	kicker = arr[k]			
	#sleep(20)
	#print(arr)
	if pivot < mover:
		pop_mover = arr.pop(m)
		#print(arr)s
		arr.insert(p,pop_mover)
		#print(arr)
		pop_kicker = arr.pop(k-1)
		#print(arr)
		arr.insert(m,pop_kicker)
		 
		p = p - 1
		m = m + 1
		
	else:
		m = m + 1
		
left = [x for x in arr if x < pivot]
right = [x for x in arr if x > pivot]
print(left)
print(right)		
		
		
		
		

print(arr)
