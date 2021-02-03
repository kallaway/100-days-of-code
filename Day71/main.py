weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}


print(weather_f)

# iterate over a pandas dataframe
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#     print(student_data_frame)
#
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)