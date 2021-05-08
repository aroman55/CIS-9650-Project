# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:52:32 2021

@author: ifahm
"""

import pandas as pd

data = pd.read_csv('hour.csv')

#Drop colummns instant and dteday. Instant does not provide useful info and 
#dteday give date in string and that information is given in other columns
data = data.drop(['instant', 'dteday'], axis = 1)

