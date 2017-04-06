
# coding: utf-8

# In[82]:

import numpy as np
import pandas as pd
import csv
import calendar
from pandas import DataFrame

Collisions = pd.read_csv('vehicle_collisions.csv')

d_trim = {'MONTH':[],'MANHATTAN':[],'NYC':[],'PERCENTAGE':[]}


for a in range(1,13):
    
    year=Collisions[(Collisions['BOROUGH'] =="MANHATTAN") & (Collisions['DATE'].apply(lambda x:x.split("/")[2]) == "16") ]
    new_york=((Collisions['DATE'].apply(lambda x:x.split("/")[2]) == "16") & (Collisions['DATE'].apply(lambda x:x.split("/")[0]) == str(a))).sum()
    manhattan=(year['DATE'].apply(lambda x:x.split("/")[0]) == str(a)).sum()
    percentage=(manhattan/new_york).round(2)
    
    d_trim['MONTH'].append(calendar.month_name[int(a)])
    d_trim['MANHATTAN'].append(manhattan)
    d_trim['NYC'].append(new_york)
    d_trim['PERCENTAGE'].append(percentage)
        

        
df = DataFrame(d_trim, columns=['MONTH','MANHATTAN','NYC','PERCENTAGE'])
df.to_csv('Que1Part1.csv')
df.head()      


# In[ ]:




# In[ ]:



