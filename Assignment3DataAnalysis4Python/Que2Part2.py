
# coding: utf-8

# In[26]:

import re
import numpy as np
import pandas as pd


ec=pd.read_csv('employee_compensation.csv')

emp_cal=ec[ec['Year Type'] == 'Calendar']

emp_sort=emp_cal.sort_values(by='Employee Identifier')

emp_sort.set_index('Employee Identifier',inplace=True)


# In[28]:

employee_salary=employee_cal.groupby(['Employee Identifier']).agg({'Salaries': np.sum,'Overtime': np.sum})


# In[31]:

employee_time=employee_salary[employee_salary['Overtime']/employee_salary['Salaries']>(5/100)]

emp_clean=xyz[xyz.index.isin(employee_time.index)]

emp_calendar1= emp_clean.groupby('Job Family').agg({'Total Benefits': np.average,'Total Compensation':np.average})

emp_calendar1['Percentage']=emp_calendar1['Total Benefits']/emp_calendar1['Total Compensation']

emp_calendar1.to_csv('Que2_Part2.csv')

emp_calendar1.head()


# In[ ]:




# In[ ]:



