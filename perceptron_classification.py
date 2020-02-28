#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt


# In[1]:


def generate_data():
    np.random.seed(0)
    X, y = datasets.make_moons(200, noise=0.20)
    return X, y


# In[2]:


def visualize(X, y, clf):
    plot_decision_boundary(lambda x: clf.predict(x), X, y)
    plt.title("Logistic Regression")


# In[ ]:




