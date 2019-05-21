#Day 34: Continuing with Pandas, today I am going to chart an import/export chart of the 10 ASEAN nations. 
#
#

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
import inline

ASEAN = {'country': ['Myanmar', 'Thailand', 'Laos', 'Cambodia', 
'Vietnam', 'Malaysia', 'Indonesia', 'Singapore', 'Brunei', 
'Philippines'], 'imports': [8.80, 37.20, 4.58, 7.05, 30.11, 42.20, 34.82, 61.89, 1.42, 21.92],
'exports': [5.26, 57.20, 2.40, 2.75, 16.94, 58.18, 35.81, 60.37, .90, 10.99]}

df = pd.DataFrame(ASEAN, index = pd.Index(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], name='letter'), 
columns = pd.Index(['country', 'imports', 'exports'], name='Import/Export'))

my_plot = df.plot(df['country'], kind='bar', legend = True)

pd.show_versions()
input()
