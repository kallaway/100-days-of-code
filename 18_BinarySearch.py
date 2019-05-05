#Day 18: Binary Search
#"Divide and Conquer"-Cut the list in half, check whether the value is = , < ,
#or >, then take appropriate action, working through the values until you find
#the number.

from random import randint
import statistics

#Generate a list of random numbers and print them.

arr = []

for var in range(1,101):
    
    arr.append(var)
    
print(arr)
#Ask user to pick one of the numbers and internally sort the numbers.
n = len(arr)-1

print(arr[n//2])
pick = input("Please enter a number between 1-100 and let the computer search for it.")
pick = int(pick)
guess = n//2
print(guess)
print(pick)
input()

def binary_search(pick, guess):                                             #this is the part I need to work on
    while pick == guess or pick != guess:
        if pick == guess:
            print("You got it. We found " + str(pick) + ".")
            input()
        else:
            if pick < guess:
                guess = guess//2
            if pick > guess:
                guess = guess + (guess//4)
    


binary_search(pick, guess)        

#Output search result
