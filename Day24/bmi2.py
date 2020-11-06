# 🚨 Don't change the code below 👇
height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in pounds: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2

#English conversion = bmi * 703
bmi_english = round(bmi * 703)

if bmi_english < 18.5:
  print(f"Your BMI is {bmi_english}, you are underweight.")
elif bmi_english < 25:
  print(f"Your BMI is {bmi_english}, you have a normal weight.")
elif bmi_english < 30:
  print(f"Your BMI is {bmi_english}, you are slightly overweight.")
elif bmi_english < 35:
  print(f"Your BMI is {bmi_english}, you are obese.")
else:
  print(f"Your BMI is {bmi_english}, you are clinically obese.")