import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        print(temperatures)

