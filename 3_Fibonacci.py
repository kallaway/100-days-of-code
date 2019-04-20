#Day 3 - Fibonacci in the while loop

input()										                #waits for enter key

number = input("Please enter a number ")	#enter any number	

A = 0										                  #initializes Fib sequence
B = 1
C = 1
D = B + C 

print(B)									                #1
print(C)									                #1
print(D)									                #2

while D < int(number):						        #Fibonacci sequence
	A = B
	B = C
	C = D 
	D = C + B
	print(D)
	
input()										                #waits for enter key
