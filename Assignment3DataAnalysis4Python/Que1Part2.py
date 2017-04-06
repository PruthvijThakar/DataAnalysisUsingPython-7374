
# coding: utf-8

# In[50]:

import numpy as np
import pandas as pd
import csv,ast
import calendar
from pandas import DataFrame


# In[59]:


vc= pd.read_csv('vehicle_collisions.csv')

new_vc = vc[['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']].copy()

d_trim = {'BOROUGH':[],'ONE_VEHICLE_INVOLVED':[],'TWO_VEHICLES_INVOLVED':[],'THREE_VEHICLES_INVOLVED':[],'MORE_VEHICLES_INVOLVED':[]}


        
for borough in(new_vc[new_vc['BOROUGH'].notnull()]['BOROUGH'].unique()):
    manhattan=new_vc[new_vc['BOROUGH'] == borough]
    total=pd.isnull(manhattan)
    oneveh=((total['VEHICLE 1 TYPE'] == ast.literal_eval('False'))& (total['VEHICLE 2 TYPE'] == ast.literal_eval('True'))).sum()
    twoveh=((total['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (total['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (total['VEHICLE 3 TYPE'] == ast.literal_eval('True'))).sum()
    threeveh=((total['VEHICLE 1 TYPE'] == ast.literal_eval('False')) & (total['VEHICLE 2 TYPE'] == ast.literal_eval('False')) & (total['VEHICLE 3 TYPE'] == ast.literal_eval('False')) & (total['VEHICLE 4 TYPE'] == ast.literal_eval('True'))).sum()
    extraveh=len(total)-(oneveh+twoveh+threeveh)

    d_trim['BOROUGH'].append(borough)
    d_trim['ONE_VEHICLE_INVOLVED'].append(oneveh)
    d_trim['TWO_VEHICLES_INVOLVED'].append(twoveh)
    d_trim['THREE_VEHICLES_INVOLVED'].append(threeveh)
    d_trim['MORE_VEHICLES_INVOLVED'].append(extraveh)

            
df = DataFrame(d_trim, columns=['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED'])
df.to_csv('Que1Part2.csv')
print(df.head())


# In[ ]:



