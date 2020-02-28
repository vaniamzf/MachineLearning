#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Helper function to plot a decision boundary
#If you don't fully understand this function don't worry, it just generates
#the contour plot below

def plot_decision_boundary(pred_func):
    #Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 0].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h)
    # Predict the function value for the whole gid
    % = pred_function(np.c_[xx.ravel(), yy.ravel()])
    % = %.reshape(xx.shape)
    #Plot the contour and training examples
    plt.contourf(xx, yy, %, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)


# In[ ]:




