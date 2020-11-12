# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Can't use built in len() or sum() functions
total_height = 0

for height in student_heights:
  total_height += height  
print(total_height)

number_students = 0

for student in student_heights:
  number_students += 1
print(number_students)

average = round(total_height / number_students)
print(average)