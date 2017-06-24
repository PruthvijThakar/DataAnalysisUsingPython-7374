
# coding: utf-8

# In[ ]:




# In[38]:

import csv
import time
import datetime 
from datetime import datetime
get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from datetime import datetime,date,timedelta
import matplotlib as plt
from scipy import stats
import scipy
import logging


# In[39]:

log_file_name = "logger" + ".log"
logger = logging.getLogger(log_file_name)
hdlr = logging.FileHandler(log_file_name)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)


# In[5]:

dirty_data = pd.read_csv('TX_170617_WBAN_13910.csv',low_memory=False,index_col=None, header=0)


# In[7]:

dirty_data['HOURLYDRYBULBTEMPF'] = pd.to_numeric(dirty_data['HOURLYDRYBULBTEMPF'], errors='coerce')
dirty_data['HOURLYDRYBULBTEMPC'] = pd.to_numeric(dirty_data['HOURLYDRYBULBTEMPC'], errors='coerce')


# In[8]:

cols = ['HOURLYDRYBULBTEMPF', 'HOURLYDRYBULBTEMPC']
dirty_data[cols] = dirty_data[cols].ffill()


# In[9]:

dirty_data['HOURLYSKYCONDITIONS'] = dirty_data['HOURLYSKYCONDITIONS'].ffill() 


# In[10]:

dirty_data['HOURLYVISIBILITY'] = dirty_data['HOURLYVISIBILITY'].ffill() 


# In[14]:

dirty_data['REPORTTPYE'] = dirty_data['REPORTTPYE'].ffill() 


# In[15]:

dirty_data['HOURLYPRSENTWEATHERTYPE'] = dirty_data['HOURLYPRSENTWEATHERTYPE'].ffill()  


# In[23]:

dirty_data['HOURLYPRSENTWEATHERTYPE'] = dirty_data['HOURLYPRSENTWEATHERTYPE'][:96].bfill() 


# In[28]:

dirty_data['HOURLYWETBULBTEMPF'] = dirty_data['HOURLYWETBULBTEMPF'].fillna(0)


# In[29]:

dirty_data['HOURLYWETBULBTEMPC'] = dirty_data['HOURLYWETBULBTEMPC'].fillna(0)


# In[31]:

cols1=['HOURLYDewPointTempF','HOURLYDewPointTempC','HOURLYRelativeHumidity','HOURLYWindSpeed','HOURLYWindDirection']
dirty_data[cols1] = dirty_data[cols1].ffill()


# In[32]:

# df.drop(df.columns[[1, 69]], axis=1, inplace=True)

# dirty_data.drop(['MonthlyTotalHeatingDegreeDays', 'MonthlyTotalCoolingDegreeDays', 'MonthlyDeptFromNormalHeatingDD', 'MonthlyDeptFromNormalCoolingDD','MonthlyTotalSeasonToDateHeatingDD','MonthlyTotalSeasonToDateCoolingDD'], axis=1,inplace='True')


# In[35]:

dirty_data['HOURLYWindGustSpeed'] =dirty_data['HOURLYWindGustSpeed'].interpolate()


# In[37]:

cols2=['HOURLYStationPressure','HOURLYPressureTendency','HOURLYPressureChange']
dirty_data[cols2] = dirty_data[cols2].bfill()


# ### this has some missing values at the start so backward fill will be a better option then forward fill for handling missing values 

# In[41]:

dirty_data.update(dirty_data[['HOURLYPrecip','HOURLYAltimeterSetting','DAILYDeptFromNormalAverageTemp','DAILYAverageRelativeHumidity','DAILYAverageDewPointTemp','DAILYAverageWetBulbTemp']
].fillna(0))


# In[42]:

cols3=['DAILYMaximumDryBulbTemp','DAILYMinimumDryBulbTemp','DAILYAverageDryBulbTemp','DAILYHeatingDegreeDays','DAILYCoolingDegreeDays']
dirty_data[cols3] = dirty_data[cols3].bfill()


# In[43]:

dirty_data.update(dirty_data[['DAILYPrecip','DAILYSnowfall','DAILYSnowDepth','DAILYAverageStationPressure','DAILYAverageSeaLevelPressure','DAILYAverageWindSpeed','DAILYPeakWindSpeed','PeakWindDirection','DAILYSustainedWindSpeed','DAILYSustainedWindDirection','MonthlyMaximumTemp','MonthlyMinimumTemp','MonthlyMeanTemp','MonthlyAverageRH','MonthlyDewpointTemp','MonthlyWetBulbTemp','MonthlyAvgHeatingDegreeDays','MonthlyAvgCoolingDegreeDays','MonthlyStationPressure','MonthlySeaLevelPressure','MonthlyAverageWindSpeed','MonthlyTotalSnowfall','MonthlyDeptFromNormalMaximumTemp','MonthlyDeptFromNormalMinimumTemp','MonthlyDeptFromNormalAverageTemp','MonthlyDeptFromNormalPrecip','MonthlyTotalLiquidPrecip','MonthlyGreatestPrecip','MonthlyGreatestPrecipDate','MonthlyGreatestSnowfall','MonthlyGreatestSnowfallDate','MonthlyGreatestSnowDepth','MonthlyGreatestSnowDepthDate','MonthlyDaysWithGT90Temp','MonthlyDaysWithLT32Temp','MonthlyDaysWithGT32Temp','MonthlyDaysWithLT0Temp','MonthlyDaysWithGT001Precip','MonthlyDaysWithGT010Precip','MonthlyDaysWithGT1Snow','MonthlyMaxSeaLevelPressureValue'
]].fillna(0))


# In[48]:

# dirty_data.update(dirty_data[['MonthlyMinSeaLevelPressureValue']]).fillna(0)


dirty_data.to_csv('TX_170617_WBAN_13910_clean.csv',index=False)



