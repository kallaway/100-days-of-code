
# coding: utf-8

# ## Linear Programming
# 
# 1. https://www.youtube.com/watch?v=7yZ5xxdkTb8
# 2. http://benalexkeen.com/linear-programming-with-python-and-pulp-part-1/
# 

# In[ ]:


import numpy as np

import pulp
import pandas as pd
import re 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# x > 0
x = np.linspace(0, 20, 2000)
# y >= 2
y1 = (x*0) + 2
# 2y <= 25 - x
y2 = (25-x)/2.0
# 4y >= 2x - 8 
y3 = (2*x-8)/4.0
# y <= 2x - 5 
y4 = 2 * x -5


# In[3]:


plt.plot(x, y1, label=r'$y\geq2$')
plt.plot(x, y2, label=r'$2y\leq25-x$')
plt.plot(x, y3, label=r'$4y\geq 2x - 8$')
plt.plot(x, y4, label=r'$y\leq 2x-5$')
plt.xlim((0, 16))
plt.ylim((0, 11))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
y5 = np.minimum(y2, y4)
y6 = np.maximum(y1, y3)
plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[4]:


# Now the same thing as pulp
lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=2, cat='Continuous')
# Objective function
lp_problem += 4 * x + 3 * y, "Z"

# Constraints
lp_problem += 2 * y <= 25 - x
lp_problem += 4 * y >= 2 * x - 8
lp_problem += y <= 2 * x - 5


# In[5]:


lp_problem


# In[6]:


lp_problem.solve()
pulp.LpStatus[lp_problem.status]


# In[7]:


for variable in lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))


# In[8]:


print(pulp.value(lp_problem.objective))


# In[9]:


books_df = pd.read_csv('../reading/goodread_books.csv')
books_df = books_df.sample(50)


# In[10]:


books_df.head()


# In[11]:


sns.distplot(books_df['rating'])


# In[12]:


sns.distplot(books_df.num_pages.dropna())


# In[13]:


# create the LP object
# Maximization problem we want to maximize the number of books we read in 100 hours
prob = pulp.LpProblem('RecommendedBooks', pulp.LpMaximize)


# In[14]:


#I would not like to read a book more than 1200 pages
books_df = books_df.dropna(subset=['num_pages'])


# In[15]:


books_df.shape


# In[16]:


books_df = books_df[books_df.num_pages <= 1200]


# In[17]:


books_df.shape


# In[18]:


sns.distplot(books_df.num_pages.dropna())


# In[19]:


decision_variables = []
for rownumber in books_df.index:
    variable = str('x' + str(rownumber))
    variable = pulp.LpVariable(str(variable), lowBound = 0, upBound = 1, cat= 'Integer')
    decision_variables.append(variable)
print("Total number of decision_variables: " + str(len(decision_variables)))


# In[20]:


#create optimization function
total_books = ""
for i, book in enumerate(decision_variables):
    total_books += book

prob += total_books
print("Optimization function: " + str(total_books))


# In[21]:


total_hours_to_read = 100
pages_per_hour = 60
total_pages_can_read = total_hours_to_read * pages_per_hour


# In[22]:


prob


# In[23]:


#create constrains - there are only 365 days

total_pages_needs_to_read = ""
for rownum, row in books_df.iterrows():
    for i, schedule in enumerate(decision_variables):
        if rownum == i:
            formula = row['num_pages']*schedule
            total_pages_needs_to_read += formula

prob += (total_pages_needs_to_read == total_pages_can_read)


# In[24]:


prob


# In[25]:


print(prob)
prob.writeLP("RecommendedBooks.lp" )


# In[28]:


pulp.LpSolverDefault.msg = 1


# In[29]:


optimization_result = prob.solve()


# In[26]:


#now run optimization
optimization_result = prob.solve()
assert optimization_result == pulp.LpStatusOptimal
print("Status:", LpStatus[prob.status])
# print("Optimal Solution to the problem: ", value(prob.objective))
print ("Individual decision_variables: ")
for v in prob.variables():
	print(v.name, "=", v.varValue)

