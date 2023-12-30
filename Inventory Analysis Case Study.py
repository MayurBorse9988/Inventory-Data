#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

import os
for dirname, _, filenames in os.walk('‪C:/Users/shahu/Downloads/InventryData'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[23]:


purches = pd.read_csv("C:/Users/shahu/Downloads/InventryData/SalesFINAL12312016.csv")
InvFinal = pd.read_csv("C:/Users/shahu/Downloads/InventryData/PurchasesFINAL12312016.csv")
sales = pd.read_csv("C:/Users/shahu/Downloads/InventryData/BegInvFINAL12312016.csv")
BegInv = pd.read_csv("C:/Users/shahu/Downloads/InventryData/EndInvFINAL12312016.csv")
PurchasePrice = pd.read_csv("C:/Users/shahu/Downloads/InventryData/InvoicePurchases12312016.csv")
PurchasesFinal = pd.read_csv("C:/Users/shahu/Downloads/InventryData/2017PurchasePricesDec.csv")
purches.head(5)


# In[24]:


InvFinal.head(5)


# In[25]:


sales.head(5)


# In[26]:


BegInv.head(5)


# In[27]:


PurchasePrice.head(5)


# In[28]:


PurchasesFinal.head(5)


# In[29]:


purches.head(5)


# In[30]:


purches.isnull().sum()


# In[31]:


purches.info()


# In[36]:


purches.head(2)


# In[39]:


sales.head(5)


# In[ ]:





# In[ ]:




