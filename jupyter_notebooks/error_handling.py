
# coding: utf-8

# 
# 
# 
# 

# an overview of errors in Python 3

# # raise Exception
# 
# https://docs.python.org/3/tutorial/errors.html
# 
# https://realpython.com/python-exceptions/
# 
# To see what an exception is, let's create a problem

# In[1]:


a    # this variable is not initialized


# In[2]:


raise Exception('stop the program!')


# In[3]:


if 5 != 3:
    raise Exception('stop the program!')


# # try except

# In[9]:


input("Please enter a number: ")


# In[11]:


x = int(input("Please enter a number: "))

print('x=',x)


# In[13]:


try:
    x = int(input("Please enter a number: "))
    print('\n\ngot it')
except ValueError as er:
    print("\n\nThat is not a valid number.")
    print(er)


# # assert
# 
# a testable claim
# 
# https://wiki.python.org/moin/UsingAssertionsEffectively<BR>
# https://www.geeksforgeeks.org/python-assert-keyword/

# In[14]:


my_var = 5

assert my_var is 5


# The statement is true so no output is produced.
# 
# More commonly, assert is used to verify type for a variable

# In[15]:


assert type(my_var) is int


# What happens if we make a claim that ends up being false?

# In[16]:


assert my_var is 3


# It is helpful to include a statement about why the assertion failure occurred

# In[17]:


assert my_var is 3, "unexpected value for %r" % my_var


# In[18]:


if my_var != 3: print("unexpected value for %r" % my_var)


# In[19]:


if my_var != 3: raise Exception("unexpected value for %r" % my_var)


# # isinstance()
# 
# type checking

# In[20]:


isinstance(my_var,int)


# In[21]:


isinstance(my_var,list)


# # type hinting
# 
# https://www.bernat.tech/the-state-of-type-hints-in-python/
# https://veekaybee.github.io/2019/07/08/python-type-hints/

# In[22]:


def funky(my_var):
    """ 
    This function adds two to the input variable
    """
    return my_var + 2


# In[23]:


funky(5)


# In[24]:


funky('hello')


# In[25]:


def funky2(my_var: int) -> int:
    """ 
    This function adds two to the input variable
    """
    return my_var + 2


# In[26]:


funky2(5)


# In[ ]:


funky2('hello')


# https://stackoverflow.com/questions/58976685/type-check-jupyter-notebooks-with-mypy
"""
jupyter nbconvert --to script error_handling.ipynb

mypy error_handling.py
"""
# including mypy as cell magic:
#     
# https://gist.github.com/knowsuchagency/f7b2203dd613756a45f816d6809f01a6
