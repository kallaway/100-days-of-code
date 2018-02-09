
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

# In[3]:


import numpy as np


# In[4]:


ar = np.array([1,2,3,4,5])
# Print out memory address
print(ar.data)

# Print out the shape of `my_array`
print(ar.shape)

# Print out the data type of `my_array`
print(ar.dtype)

# Print out the stride of `my_array`
print(ar.strides)


# In[5]:


st_ar = np.array(['aaasdf','ab','gdf'], dtype=np.string_)
# Print out memory address
print(st_ar.data)

# Print out the shape of `my_array`
print(st_ar.shape)

# Print out the data type of `my_array`
print(st_ar.dtype)

# Print out the st. Note that it takes the bytes required to store the longest string
print(st_ar.strides)


# In[6]:


np.ones((2,3,1,3),dtype=np.string_)


# In[7]:


np.full((2,2),7)


# In[12]:


# Create an array of evenly-spaced values like a range function
np.arange(10,65,5)


# In[13]:


# Create an array of evenly-spaced values
np.linspace(1,9,9)


# In[14]:


np.eye(21,6)


# In[15]:


np.identity(10) 


# **NOTE:** When working with larger dataset following functions can be handy to understand the limitations

# In[16]:


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

# 1. to make sure that the broadcasting is successful, the dimensions of your arrays need to be compatible. Two dimensions are compatible when they are equal. 

# In[17]:


# During addition the dimensions should be same NxM + NxM or NxM + Mx1 
x = np.ones((3,4))
print(x.shape)
print(x)
y = np.random.random((4,))
print(y)

print(x + y)


# In[18]:


x = np.ones((3,4))
print(x.shape)
y = np.arange(4)
print(y.shape)

print(x - y)


# In[19]:


x = np.ones((3,4))
print(x)
y = np.random.random((5,1,4))
print(y)

print(x + y)


# **The maximum size along each dimension of x and y is taken to make up the shape of the new, resulting array.**

# In[20]:


y = np.ones((5,1,4))
print("STD: {}".format(np.std(y)))
print("MEAN: {}".format(np.mean(y)))


# In[21]:


x = np.zeros((3,5))
z = np.zeros((3,5))


# In[22]:


print(x)
print(z)


# In[23]:


print(np.array_equal(x,y))
print(np.array_equal(x,z))


# In[24]:


scalar = np.arange(1,50)
ones = np.ones((49,10,49))
ar = np.multiply(scalar, ones)


# In[25]:



ar


# In[31]:


#QUICK Review if subsetting
print("element at index 1", ar[1])

# Select the 
print("element at row 1 column 2", ar[1][2])


print("element at row 1 column 2", ar[1,2])


# In[38]:


print(ar[1,1,2])
print("row 0 and 1, column 1", ar[0:2,1])


# In[42]:


ar_transpose = ar.T
print(ar_transpose.shape)

