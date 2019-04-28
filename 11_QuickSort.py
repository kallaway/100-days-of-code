n = input("Please enter the of amount of numbers that you would like in your list. ")
n = int(n)

arr = []

for i in range(0,n):																	#this for loop generates n random numbers for our sort
	rand = randint(1,100)																#random integer between 1 - 100
	arr.append(rand)																	  #puts new element at the end
	
n = len(arr)	
	

print("   ")
print(arr)
i = 0


 
while i < n-1: 
	mover = arr[i]
	kicker = arr[-2]
	pivot = arr[-1]
	if mover >= pivot:
		
		mover_out = arr.pop(i)
		pivot_out = arr.pop(-1)
		kicker_out = arr.pop(-1)
		n = len(arr)
		arr.insert(n+1,mover_out)
		n = len(arr)
		arr.insert(n-1,pivot_out)
		n = len(arr)
		arr.insert(i, kicker_out)
		
		# ~ pivot = arr[-1]
		# ~ mover = arr[i]
		# ~ kicker = arr[-2]
		#left = arr[pivot:]
		#right = arr[:pivot]
		break
	i = i + 1

print("  ")		

print(arr)
	
	
	
