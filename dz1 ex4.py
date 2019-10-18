#!/usr/bin/env python
# coding: utf-8

# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,121)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(2*x))

