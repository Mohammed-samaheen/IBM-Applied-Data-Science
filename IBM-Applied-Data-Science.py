#!/usr/bin/env python
# coding: utf-8

# ### Capstone Project Notebook

# The following Notebook will be used to get, clean, visualize and analyze data and information related to the completion of the IBM Capstone Project.

# In[13]:


import pandas as pd
import numpy as np


# In[14]:


print("Hello Capstone Project Course!")


# In[15]:


import sys
from notebook import transutils as _
from notebook.services.contents.filemanager import FileContentsManager as FCM

try:
    notebook_fname = sys.argv[1].strip('.ipynb')
except IndexError:
    print("Usage: create-notebook <notebook>")
    exit()

