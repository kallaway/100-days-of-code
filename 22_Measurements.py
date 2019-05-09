#Day 22: Measuring execution time, code complexity, and memory usage for a given script
import time
from time import sleep
import math
#from decimal import *
import psutil 
import os

# ~ Decimal(30) / Decimal(5)
# ~ getcontext().prec = 15

n = int(input("Enter a number: "))
forloop_array = []
listcomp_array = []




begin = time.time()
for num in range(1,n+1):
	x = num**4
	forloop_array.append(x)
	#sleep(1)
finish = time.time()
timed = finish - begin
print(forloop_array) 
print("Time to execute: " + str(timed))


#filepath = "C:\Users\D\python_work\Day_22_Measurements.py"
begin = time.time()
listcomp_array = [num**4 for num in range(1,n+1)]
finish = time.time()
timed = finish - begin	
print(listcomp_array)	
print("Time to execute: " + str(timed))

mem = os.getpid()
print(mem)
print(psutil.cpu_times)
proc = psutil.Process().memory_full_info()
#usage = os.memoryview()
print(proc)
#length = len(open(filepath).readlines())


input()
