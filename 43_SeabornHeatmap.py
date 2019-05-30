#Day 43: Heat Map Cont. 
#Here we have the corrected heatmap and clustermap scripts
#

import seaborn as sns
import numpy as np
#import fastcluster 

#read the csv

ans = sns.load_dataset('anscombe')

anspiv = ans.pivot('dataset', 'y', 'x')
#heatmap = sns.heatmap(anspiv, square=True, linecolor='purple')
heat = sns.heatmap(anspiv)

print(' ')

#clusterpiv = ans.pivot('y', 'x')
data = ans.pop('dataset')
cluster = sns.clustermap(ans)
