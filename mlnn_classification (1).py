#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[1]:


import matplotlib.pyplot as plt


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# In[2]:


import numpy as np


# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook

# In[3]:


import sklearn


# In[4]:


import sklearn.datasets


# In[5]:


import matplotlib


# In[ ]:


#Display plots inline and changes default figure size
get_ipython().run_line_magic('matplotlib', 'inline')

matplotlib.rcParams['figure.figsize'] = (10.0, 8.0)


# In[ ]:


#%% 2
np.random.seed(3)
X, y = sklearn.datasets.make_moons(200, noise=0.20)
plt.scatter(X[:,0], s=40, c=y, cmap=plt.cm.Spectral)


# In[ ]:




