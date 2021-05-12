# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:52:32 2021

@author: ifahm
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm

data_porto = pd.read_csv('Portugual_hour_clean.csv')


#Linear model
#C(x) indicates that x is a categorical variable 
model_porto = smf.ols('total_count ~ windspeed + temp + atemp + hum + C(season) + C(weathersit) + C(weekday) + C(month) + C(hour)', data = data_porto).fit() ## sm.OLS(output, input)

model_porto.summary()

# Print out the statistics


data_seoul = pd.read_csv('Seoul_hour_clean.csv')

model_seoul = smf.ols('count ~ rainfall + solar_rad + dew_point + visibility + windspeed + hum + temp + C(weekday) + C(month) + C(hour) + C(season)', data = data_seoul).fit()

model_seoul.summary()

X_train = data_porto[['temp', 'atemp', 'hum', 'windspeed']]
Y_train = data_porto[['total_count']]

X = X_train
y = Y_train

model_temp_porto = smf.ols('total_count~ temp + atemp + hum + windspeed', data =data_porto).fit()

model_temp_porto.summary()



