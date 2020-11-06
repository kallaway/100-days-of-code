print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    age = int(input("How old are you?\n"))
    if age < 12:
        print("Your ticket cost is $5.00")
    elif age <= 18:
    
        print("Your ticket cost is $7.00")
    else: 
        print("Your ticket cost is $12.00")
  
else:
  print("Get out of here shorty!")