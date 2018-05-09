# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 19:59:16 2018

@author: Suhas
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import datetime as dt 
import seaborn as sns # data visualization


#plt.style.use(style='ggplot')
#plt.rcParams['figure.figsize'] = (6, 4) # to change width and height of figure
##%matplotlib inline
#
#color = sns.color_palette()
##import warnings
##warnings.filterwarnings('ignore') 
#
#from subprocess import check_output
#print(check_output(["ls"]).decode("utf8"))


df_trip = pd.read_csv('F:\\yellow_tripdata.csv', parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
print(df_trip.shape)
df_trip.head()
print(df_trip.vendor_id.unique())
