
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


# In[2]:


train_df = pd.read_csv('data/kaggle/house-prices/train.csv', index_col='Id')
test_df = pd.read_csv('data/kaggle/house-prices/test.csv',index_col='Id')


# In[3]:


train_df.head()


# In[4]:


train_df.columns.values


# In[5]:


target = 'SalePrice'
target_series = train_df[target]


# In[6]:


train_df = train_df.drop('SalePrice', axis=1)


# In[7]:


train_df['training_set'] = True
test_df['training_set'] = False
full_df = pd.concat([train_df, test_df])


# In[8]:


full_df = full_df.interpolate()
full_df = pd.get_dummies(full_df)


# In[9]:


train_df = full_df[full_df['training_set']].drop('training_set', axis=1)
test_df = full_df[~full_df['training_set']].drop('training_set', axis=1)
train_df.head()


# In[10]:


rf = RandomForestRegressor(n_estimators=100, n_jobs=-1)
rf.fit(train_df, target_series)


# In[12]:


predictions = rf.predict(test_df)


# In[13]:


my_submission = pd.DataFrame({'Id': test_df.index, 'SalePrice': predictions})


# In[14]:


my_submission.to_csv('data/kaggle/house-prices/submission.csv', index=False)


# In[15]:


my_submission.shape


# Inspired by (https://towardsdatascience.com/machine-learning-zero-to-hero-everything-you-need-in-order-to-compete-on-kaggle-for-the-first-time-18644e701cf1)[https://towardsdatascience.com/machine-learning-zero-to-hero-everything-you-need-in-order-to-compete-on-kaggle-for-the-first-time-18644e701cf1]
