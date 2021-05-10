# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:52:32 2021

@author: ifahm
"""

import pandas as pd
import statsmodels.formula.api as smf

data = pd.read_csv('Portugual_hour_clean.csv')


#Linear model
#C(x) indicates that x is a categorical variable 
model = smf.ols('total_count ~ windspeed + temp + atemp + hum + C(season) + C(weathersit) + C(weekday) + C(year) + C(month) + C(hour)', data = data).fit() ## sm.OLS(output, input)

model.summary()

# Print out the statistics




