#Write your code below this line 👇
def findLen(str): 
  counter = 0    
  for i in str: 
        counter += 1
  return counter 
str = input("What is your name? ")
print(findLen(str)) 