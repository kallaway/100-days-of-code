
# coding: utf-8

# ## Linear Programming
# 
# 1. https://www.youtube.com/watch?v=7yZ5xxdkTb8
# 2. http://benalexkeen.com/linear-programming-with-python-and-pulp-part-1/
# 

# In[1]:


import numpy as np

import pulp
import pandas as pd
import re 
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


pulp.pulpTestAll()


# In[3]:


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


# In[4]:


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


# In[5]:


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


# In[6]:


lp_problem


# In[7]:


lp_problem.solve()
pulp.LpStatus[lp_problem.status]


# In[8]:


for variable in lp_problem.variables():
    print("{} = {}".format(variable.name, variable.varValue))


# In[9]:


print(pulp.value(lp_problem.objective))


# In[10]:


books_df = pd.read_csv('../reading/goodread_books.csv')
# books_df = books_df.sample(50)


# In[11]:


books_df.head()


# In[12]:


sns.distplot(books_df['rating'])


# In[13]:


sns.distplot(books_df.num_pages.dropna())


# In[14]:


# create the LP object
# Maximization problem we want to maximize the number of books we read in 100 hours
prob = pulp.LpProblem('RecommendedBooks', pulp.LpMaximize)


# In[15]:


#I would not like to read a book more than 1200 pages
books_df = books_df.dropna(subset=['num_pages', 'title', 'rating', 'genres'])


# In[16]:


books_df.shape


# In[18]:


books_df = books_df[(books_df.num_pages <= 1200) & 
                    (books_df.num_pages > 20) &
                    (books_df.rating > 3.5) &
                    (books_df.num_ratings > 10000) &
                    (books_df.num_review > 1000) &
                    (~books_df.genres.str.contains('children'))
                   ]


# In[19]:


books_df.shape


# In[20]:


sns.distplot(books_df['rating'])


# In[21]:


sns.distplot(books_df.num_pages.dropna())


# In[22]:


decision_variables = {}
for rownumber, row in books_df.iterrows():
    variable = str('x' + str(rownumber))
    variable = pulp.LpVariable(str(variable), lowBound = 0, upBound = 1, cat= 'Integer')
    decision_variables[rownumber] = variable
print("Total number of decision_variables: " + str(len(decision_variables)))


# In[23]:


#create optimization function
total_books = ""
for i, book in decision_variables.items():
    total_books += book * books_df.loc[i, 'rating']

prob += total_books
print("Optimization function: " + str(total_books))


# In[24]:


total_hours_to_read = 100
pages_per_hour = 60
total_pages_can_read = total_hours_to_read * pages_per_hour


# In[25]:


prob


# In[26]:


#create constrains - there are only 365 days

total_pages_needs_to_read = ""
for rownum, row in books_df.iterrows():
    formula = row['num_pages']* decision_variables[rownum]
    total_pages_needs_to_read += formula

prob += (total_pages_needs_to_read == total_pages_can_read)


# In[27]:


print(prob)
prob.writeLP("RecommendedBooks3.lp" )


# In[28]:


pulp.LpSolverDefault.msg = 1


# In[29]:


#now run optimization
optimization_result = prob.solve()
assert optimization_result == pulp.LpStatusOptimal
print("Status of the solution:", pulp.LpStatus[prob.status])
print("Number of books in the suggested list: ", pulp.value(prob.objective))


# In[30]:


var_name = []
var_value = []

for v in prob.variables():
    var_name.append(v.name)
    var_value.append(v.varValue)
df = pd.DataFrame({'row_num': var_name, 'value': var_value})


# In[ ]:



   


# In[31]:


df.shape


# In[32]:


df['row_num'] = df.row_num.str.replace('x', '').astype(int)


# In[33]:


df = df[df.value == 1]


# In[34]:


df.shape


# In[35]:


result_df = books_df.loc[df.row_num.tolist()].copy()


# In[36]:


result_df.shape[0]


# In[37]:


sns.distplot(result_df.num_pages)


# In[38]:


sns.distplot(result_df.rating)


# In[39]:


result_df = result_df.sort_values(ascending=False, by=['rating', 'num_ratings'])


# In[40]:


result_df.to_csv('./v3_reading_list.csv', index=False)


# In[41]:


result_df.url.head(10).tolist()

