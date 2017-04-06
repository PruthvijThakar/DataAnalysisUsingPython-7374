
# coding: utf-8

# In[22]:

import pandas as pd
import numpy as np
import csv
import datetime as dt

df=pd.read_csv('cricket_matches.csv')

abc = df[df['home']== df['winner']]

pqr= abc[abc['winner'] == abc['innings2']]

xyz= abc[abc['winner'] == abc['innings1']]

xyz['Score'] = xyz['innings1_runs']

f =  [abc, xyz]

df_new = pd.concat([abc,xyz])

x = df_new[['home', 'Score']]
y = x.groupby(['home'], as_index= False).mean()
y = y.dropna()
y.to_csv('Que3_Part1.csv')
print(y.head())


# In[ ]:




# In[ ]:



