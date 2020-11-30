import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
how_many = len(names)
random_choice = random.randint(0, how_many - 1)
buyer = names[random_choice] 

# can use choice() function also, instead
# buyer = random.choice(names)

print(buyer + " is going to buy the meal today!")