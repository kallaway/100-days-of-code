
# coding: utf-8

# In[8]:


from itertools import permutations, product


# In[9]:


# cartesian products of two lists (iterators)
list(product([1,2,3],[1,2]))

# No so directly useful in my day to day work


# In[10]:


# creating permutation with number of elements
print(list(permutations('abc',2)))


# In[11]:


# print all possible permutations of size  of the string in lexicographic sorted order.
from itertools import permutations
inp = input().split(' ')
perms = (''.join(t) for t in permutations(sorted(inp[0]), int(inp[1])))
print('\n'.join(perms))

