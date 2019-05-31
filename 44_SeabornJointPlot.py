#Day 44: Misc. Seaborn 
#Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
example_four = sns.load_dataset('flights')



sns.set(style='darkgrid')
im = sns.load_dataset('flights')
sns.jointplot(x = 'year',y = 'passengers', data=im, kind="scatter",color="lime")

plt.show()
