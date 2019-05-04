#Day 17: Standard Numbers to Binary and Hex
#Finding a base 2 (binary) number manually is simply a matter of repeatedly dividing the number by 2, saving each remainder, and reversing the order. 
#Similarly, finding a base 16 (hexadecimal) number if found by repeatedly dividing the number by 16, and saving each remainder, making sure to assign values 
#from 10-15 as 'a' to 'f', and reversing the order. 
from time import sleep
import math 

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
input()

n = input("Number: ")

n = int(n)																#converts string input to int

b = bin(n)																#standard python base 2 method

h = hex(n)																#standard python base 16 method

print(" ")
print(b)
print(" ")
print(h)
print(" ")


class manual_calc:
	def slowbin(n):														#function to manually calculate Base 2 / Binary Code					
		while n > 0:
			m = n%2
			print(str(n) + "       " + str(m))
			n = n//2
			sleep(1)

	def slowhex(n):														#function to manually calculate Base 16 / Hexadecimal 
		while n > 0:
			m = n%16
			if m != 0:
				if m == 10:
					m = 'a'
				if m == 11:
					m = 'b'
				if m == 12:
					m = 'c'
				if m == 13:
					m = 'd'
				if m == 14:
					m = 'e'
				if m == 15:
					m = 'f'
		
			print(str(n) + "        " + str(m).format('>'))
			n = math.floor(n/16)
			sleep(1)
manual_calc.slowbin(n)													#call slowbin()
print("   ")
manual_calc.slowhex(n)													#call slowhex()
print("   ")
print(n)
input()

###additional practice with min() and max() functions
data_array = [3, 6, 9, 12, 1]
print(data_array)
print(max(data_array))
print(min(data_array))
