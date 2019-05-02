#Day 15: Heap Sort
#The Heap Sort has an average coding time, low memory requirement, and is consistantly fast. Other algorithms, such as the quick
#sort, might outperform it, but also might underperform it under some circumstances. Therefore, we can be sure that if we run a
#Heap Sort, our data will be sorted with predictable good performance.
from time import sleep                                          #import sleep module to use when seeing what each thing does
import math                                                     #for math functionsdata_array = []
data_array = []                                                 #declares the array                                          
query = 0                                                       #our input variable

while query != 'E':                                             #'E' breaks the loop
    query = input("Give me some numbers. Press E to escape.")   #Give me numbers
    data_array.append(query)                                    #Add them to the end of the list

length = len(data_array)                                        #here's the length of the array
ind = length - 1                                                #ind variable turns it to the index
del data_array[ind]                                             #let's get rid of 'E'
print(data_array)                                               #this is it so far

print("  ")
print("  ")
print("Let's use our user data to sort using the heap sort.")

i = 1

def heapify(data_array, length):                                #famous heapify method
    p = (length//2)-1                                           #finds parent node
    while p>=0:                                                 #if the parent is an index greater than 0
        shifter(data_array, p, length)                          #calls the shift function
        p -= 1
def shifter(data_array, i, length):                             #let's creater a shifter down function
    left = 2 * i + 1                                            #L = 2i but add 1 for index
    right = 2 * i + 2                                           #R = 2i+1 and add 1 for index
    largest = i                                                 #parent = i = 1
    if left <= length - 1 and data_array[left] > data_array[i]: #if conditions are met...
        largest = left
    if right <= length - 1 and data_array[right] > data_array[largest]:
        largest = right
    if largest != i:
        data_array[i], data_array[largest] = data_array[largest], data_array[i] #swap
        shifter(data_array, largest, length)
shifter(data_array, i, length)
heapify(data_array, length)
