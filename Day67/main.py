# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
#
# # columns are Series
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
#
# # print(data["temp"].max())
# # print(data["condition"])
# # print(data.condition)
#
# # find rows
# # print(data[data.temp == data.temp.max()])
#
# # monday = (data[data.day == "Monday"])
# # print(monday.temp * 2 + 30)
#
# # create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(red_squirrels_count)
print(black_squirrels_count)
print(gray_squirrels_count)

squirrels_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrels_data)
df.to_csv("squirrel_colors.csv")