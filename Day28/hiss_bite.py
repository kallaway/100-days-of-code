#Write your code below this row 👇

# want to be able to include any two integers
# will use 5 and 9
for number in range(1, 101):
  # note to self: include the and condition first
  if number % 5 == 0 and number % 9 == 0:
    print("Hiss Bite. (Hey, I warned you!)")
  elif number % 5 == 0:
    print("Hiss. (Yikes!)")
  elif number % 9 == 0:
    print("Bite. (Ouch!!)")
  else:
    print(number)