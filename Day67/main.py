import pandas

# data = pandas.read_csv("weather_data.csv")

# columns are Series
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)


# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

# find rows
# print(data[data.temp == data.temp.max()])

# monday = (data[data.day == "Monday"])
# print(monday.temp * 2 + 30)

# create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")