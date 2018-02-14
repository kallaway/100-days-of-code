
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


train_df = pd.read_csv('data/kaggle/house-prices/train.csv', index_col='Id')
test_df = pd.read_csv('data/kaggle/house-prices/test.csv',index_col='Id')


# In[3]:


train_df.head()


# In[4]:


train_df.columns.values


# ### Data Analysis and understanding
# 
# This kernel in kaggles seems to be relevant to the problem I have picked up and an opportunity to learn a lot.
# https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python

# Variables analysis @ https://docs.google.com/spreadsheets/d/1GEHcJFNE-pE-UZscw0GGjjkCAZnsmrJnoz1L5j4K09U/edit?usp=sharing

# Analysing Salesprice, our dependent target variable

# In[5]:


train_df['SalePrice'].describe()


# In[6]:


sns.distplot(train_df['SalePrice']);


# Descriptive Stats 
# Skewness and Kurtosis
# https://www.r-bloggers.com/measures-of-skewness-and-kurtosis/

# In[8]:


print("Skewness: %f" % train_df['SalePrice'].skew())
print("Kurtosis: %f" % train_df['SalePrice'].kurt())


# In[10]:


var = 'GrLivArea'
data = pd.concat([train_df['SalePrice'], train_df[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));


# In[11]:


var = 'LotArea'
data = pd.concat([train_df['SalePrice'], train_df[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));


# In[12]:


var = 'MasVnrArea'
data = pd.concat([train_df['SalePrice'], train_df[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));


# In[13]:


var = '3SsnPorch'
data = pd.concat([train_df['SalePrice'], train_df[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));


# In[14]:


var = 'TotalBsmtSF'
data = pd.concat([train_df['SalePrice'], train_df[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));


# In[15]:


var = 'OverallQual'
data = pd.concat([train_df['SalePrice'], train_df[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000);


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
