
# coding: utf-8

# In[15]:

import numpy as np
import pandas as pd
import csv


# In[2]:

ec = pd.read_csv('employee_compensation.csv')


# In[25]:


ec = pd.read_csv('employee_compensation.csv')
ec_groupby=ec.groupby(['Organization Group','Department'])

xyz = ec_groupby.mean()
ec_sort= xyz['Total Compensation'].groupby(level=0, group_keys=False, as_index=True)
res = ec_sort.apply(lambda x: x.sort_values(ascending=False))
final=res.to_frame()
final.to_csv('Que2_Part1.csv')
print(final.head())



# In[ ]:



