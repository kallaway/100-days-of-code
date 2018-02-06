
# coding: utf-8

# ## Numpy Learning
# 
# This is my attempt to learn numpy from ground up instead of just learning on the go.
# 
# 
# ### Notes
# 
# [Beginning read](https://www.datacamp.com/community/tutorials/python-numpy-tutorial#gs.h3DvLnk)
# - numpy array is comparable to python lists. (Munpy = Numeric Python)
# - At structural level, an array is basically a combination of a memory address, a data type, a shape and strides.
#     - The strides are the number of bytes that should be skipped in memory to go to the next element. If your strides are (10,1), you need to proceed one byte to get to the next column and 10 bytes to locate the next row.
# - Axis numbering
#     - axis = 0 is rows
#     - axis = 1 is columns
#     - axis = 2 is the next dimension in 3d array (you get the idea)
# - There are different datatypes we can explicitly pass while creating `np.array`. [Reffer to this cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
# - to load data directly
#     - `genfromtxt()`
#     - `loadtxt()` (least preffered)
#     - or read pandas and convert to np array (imho)
# - Functions for IO are listed in [DOCs here](https://docs.scipy.org/doc/numpy/reference/routines.io.html)
# - When working with operations on datasets with different dimension, you have to use *Broadcasting*. Numpy Boradcasting
# 
# 
# 

# In[1]:


import numpy as np


# In[2]:


ar = np.array([1,2,3,4,5])
# Print out memory address
print(ar.data)

# Print out the shape of `my_array`
print(ar.shape)

# Print out the data type of `my_array`
print(ar.dtype)

# Print out the stride of `my_array`
print(ar.strides)


# In[7]:


st_ar = np.array(['aaasdf','ab','gdf'], dtype=np.string_)
# Print out memory address
print(st_ar.data)

# Print out the shape of `my_array`
print(st_ar.shape)

# Print out the data type of `my_array`
print(st_ar.dtype)

# Print out the st. Note that it takes the bytes required to store the longest string
print(st_ar.strides)


# In[17]:


np.ones((2,3,1,3),dtype=np.string_)


# In[18]:


np.full((2,2),7)


# In[21]:


# Create an array of evenly-spaced values like a range function
np.arange(10,65,5)


# In[24]:


# Create an array of evenly-spaced values
np.linspace(1,9,9)


# In[27]:


np.eye(21,6)


# In[39]:


np.identity(10) 


# **NOTE:** When working with larger dataset following functions can be handy to understand the limitations

# In[42]:


# Print the number of `my_array`'s dimensions
print(ar.ndim)

# Print the number of `my_array`'s elements
print(ar.size)

# Print information about `my_array`'s memory layout
print(ar.flags)

# Print the length of one array element in bytes
print(ar.itemsize)

# Print the total consumed bytes by `my_array`'s elements
print(ar.nbytes)


# ### NumPy Broadcasting 
# 
# (very important in practical datascience)
