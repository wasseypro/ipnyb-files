#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Comparing features of Dataframe 1 and Dataframe 2


# In[2]:


import numpy as np
import pandas as pd
import filecmp 


# In[13]:


# Creating Dataframe
df1=pd.read_csv('e:/Datasets/train.csv')
df2=pd.read_csv('e:/Datasets/test.csv')


# In[14]:


df1.info(),df2.info()


# In[5]:


df2.info()


# In[6]:


df3=pd.concat([df1,df2], axis=1)


# In[7]:


df3.info()


# In[ ]:




