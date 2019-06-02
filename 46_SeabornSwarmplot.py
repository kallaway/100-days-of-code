#Day 46: Swarm Plot in Seaborn
#The Swarm Plot in Seaborn, also known as the Beeswarm is convenient to use
#for medium-size datasets. Because the point are plotted without overlap, 
#plotting big data is difficult, even though the diameter of the point CAN be \
#turned down. While we can use the standard Python numpy plot,
#Pandas is generally recommended so that the axes will be annotated. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Let's import a csv and create a dataframe from it
df_import = pd.read_csv('planets.csv')                                                        
plt.figure("Planets Spreadsheet")
sns.swarmplot(x="year",y="distance", data=df_import)
plt.xticks(rotation=75)
plt.show()
