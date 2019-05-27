#Day 40: Data Process Part 3: Let's import the data, use some basic 
#sort functions, export the CSV, and worry about the custom sorts later

import pandas as pd
from pandas import DataFrame

raw_data = pd.read_csv("country_population.csv")

population1 = raw_data.sort_values('2016')
sort_one = population1.to_csv(r'C:\Users\D\python_work\sort1.csv')

population2 = raw_data.sort_values('2016', ascending=False)
sort_two = population2.to_csv(r'C:\Users\D\python_work\sort2.csv')

population3 = raw_data.sort_values('2016',na_position='first')
sort_three = population3.to_csv(r'C:\Users\D\python_work\sort3.csv')

population4 = raw_data.sort_values(['1960','2016'])
sort_four = population4.to_csv(r'C:\Users\D\python_work\sort4.csv')
