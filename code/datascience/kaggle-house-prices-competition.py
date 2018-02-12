
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


# In[12]:


train_df = pd.read_csv('data/kaggle/house-prices/train.csv', index_col='Id')
test_df = pd.read_csv('data/kaggle/house-prices/test.csv',index_col='Id')


# In[13]:


train_df.head()


# In[14]:


train_df.columns.values


# In[15]:


target = 'SalePrice'

