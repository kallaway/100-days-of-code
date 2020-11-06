# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

end_age = int(90)

# in years
time_left = int(end_age) - int(age)

days = time_left * 365
weeks = time_left * 52
months = time_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")