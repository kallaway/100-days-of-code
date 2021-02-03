# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
if size == "S":
  total += 15
elif size == "M":
    total += 20
else: 
    total += 25

if add_pepperoni == "Y":
  if size == "S":
      total += 2
  else: 
      total += 3

if extra_cheese == "Y":
      total += 1

print(f"Your total cost is ${total}")