
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pylab as pylab
get_ipython().run_line_magic('matplotlib', 'inline')
pylab.rcParams[ 'figure.figsize' ] = 10 , 8


# In[2]:


happiness_2017 = pd.read_csv('./data/2017.csv')
happiness_2016 = pd.read_csv('./data/2016.csv')
happiness_2015 = pd.read_csv('./data/2015.csv')


# In[3]:


def world_corr(data):
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, cbar=True, cmap="RdYlGn")


# In[4]:


world_corr(happiness_2015)


# In[5]:


world_corr(happiness_2016)


# In[6]:


world_corr(happiness_2017)


# ##### Wow, the factors affecting happiness hasn't changed much in 3 years. 
