#Day 47: Let's look at most of the main Seaborn plots, using the 
#exercise.csv dataset from [https://github.com/mwaskom/seaborn-data]

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

exercise_data = pd.read_csv("exercise.csv")         #exercise spreadsheet

#LMPlot
lmplot = sns.lmplot(x='id',y='pulse',data=exercise_data)

#BarPlot
plt.figure("Barplot")
barplot = sns.barplot(x='id',y='pulse',data=exercise_data)
plt.xticks(size=8)

#KDEPlot
plt.figure()
x = exercise_data.pulse
KDE = sns.kdeplot(x, shade=True, color='green')

#ScatterPlot
plt.figure()
scatterplot=sns.scatterplot(x='pulse',y='time',data=exercise_data, 
color='purple')

#DistPlot
plt.figure()
a = exercise_data.pulse
distplot = sns.distplot(a, color='limegreen')

#LinePlot
plt.figure()
lineplot = sns.lineplot(x='pulse',y='id',data=exercise_data, color='red')

#RelPlot
relplot = sns.relplot(x='pulse',y='id',data=exercise_data)

#CatPlot
catplot = sns.catplot(x='diet',y='id',hue='pulse',data=exercise_data)

#BoxPlot
plt.figure()
boxplot = sns.boxplot(x='diet',y='pulse',data=exercise_data)

#ViolinPlot
plt.figure()
violin = sns.violinplot(x='diet',y='pulse',hue='id', inner='quart', 
data=exercise_data)

#HeatMap
plt.figure()
p_e_data = exercise_data.pivot('time','id','pulse')
exercise_heatmap = sns.heatmap(p_e_data)

#JointPlot
sns.set(style='white')
jointplot = sns.jointplot(x='pulse',y='id',data=exercise_data, 
kind='hex', color='darkblue')

#StripPlot
plt.figure()
stripplot = sns.stripplot(x='id',y='pulse',data=exercise_data)

#BoxenPlot
plt.figure()
boxen = sns.boxenplot(x='id',y='time',data=exercise_data,scale='exponential')

#ResidPlot
plt.figure()
residplot = sns.residplot(x='id',y='pulse',data=exercise_data)

#SwarmPlot
plt.figure("Swarm Plot")
swarm = sns.swarmplot(x='pulse',y='time',data=exercise_data)

#PairPlot
inp = exercise_data
pairplot = sns.pairplot(inp)

plt.show()

