#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
Data = pd.read_csv("./Downloads/Hamoye/FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding='latin-1')
Data.to_csv("./Downloads/Hamoye/FoodBalanceSheets_E_Africa_NOFLAG.csv", index=False)

Data.describe(include = 'all')


# In[ ]:




