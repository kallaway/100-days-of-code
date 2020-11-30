#Remember to use the random module 👇
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
side = random.randint(0,1)
if side == 1:
  print("Heads")
else:
  print("Tails")