#Day 16: Heap Sort Part 2
#Heap Sort separates the array elements into nodes, with index 0 (for algorithm purposes, index + 1, or i = 1) representing the top node, or parent. The rest
#of the nodes are represented as a binomial tree, with the variable i representing the root, or top parent, the expression i//2 representing each parent, the
#expression 2i representing each left child, and the formula 2i + 1 representing the right child. A good youtube video on this is available in a lecture by
#Srini Devadas of MIT available here: [https://www.youtube.com/watch?v=B7hVxCmfPtM]
import math
from time import sleep 

def heapify(data_array, length, i):										#The famous "heapify" method
	
	largest = i															#Largest value should float to top then swap with lowest node, pop, and remove node
	
	left = 2 * i + 1													#left side child													
	
	right = 2 * i + 2													#right side child
	
	if left < length and data_array[i] < data_array[left]:				#|	left and right sides of the equation, accounting for index |#	
		largest = left													#|															   |#
																		#|															   |#
	if right < length and data_array[largest] < data_array[right]:		#|															   |#
		largest = right													#|															   |#
																		#|															   |#
	if largest != i:													#V															   V#
		data_array[i], data_array[largest] = data_array[largest], data_array[i]
		
		heapify(data_array, length, largest)
		
def heapsort(data_array):												#Here's where we perform sort
	
	length = len(data_array)
	
	for i in range(length, -1, -1):
		heapify(data_array, length, i)
	
	for i in range(length-1, 0, -1):
		data_array[i], data_array[0] = data_array[0], data_array[i]
		heapify(data_array, i, 0)

data_array = [4, 89, 1, 34, 88, 12, 34]									#inputs

#print(data_array)
print("Your original list is: \n\t" +str(data_array))
# ~ num = input("How many numbers would you like to enter? ")
# ~ real_num = int(num)
# ~ data_array = []
# ~ for counter in range(1,real_num + 1):
	# ~ enter = input("Please enter the number " + str(counter) + " number into the your list.")
	# ~ data_array.append(enter)

# ~ print(data_array)




input()
print
print("   ")
print("   ")
print("   ")
heapsort(data_array)													#generates output
print("Using Heap Sort, your number inputs have been converted to the following: \n\t" +str(data_array))
