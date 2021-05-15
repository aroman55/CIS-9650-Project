# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:52:32 2021

@author: ifahm
"""

import pandas as pd
import statsmodels.formula.api as smf

data_porto = pd.read_csv('Portugual_hour_clean.csv')
data_seoul = pd.read_csv('Seoul_hour_clean.csv')

############# average number of rider for each hour in the day
p_hours = data_porto.groupby('hour')['total_count'].mean()
s_hours = data_seoul.groupby('hour')['count'].mean() 

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.set_title('Porto, Portugal')
ax2.set_title('Seoul, South Korea')

ax1.set_xlabel('Hours')
ax1.set_ylabel('Customers')

ax1.plot(p_hours)
ax2.plot(s_hours)

ax1.set_xlabel('Hour of the Day')
ax1.set_ylabel('Customers')
ax2.set_xlabel('Hour of the Day')

######### average number of riders per day of the week
p_daily = data_porto.groupby("weekday")['total_count'].mean()
s_daily = data_seoul.groupby("weekday")['count'].mean()

fig, (ax1, ax2) = plt.subplots(1,2)
#fig.suptitle('Ridership Throughout the Week')
ax1.set_title('Porto, Portugal')
ax2.set_title('Seoul, South Korea')

ax1.set_xlabel('Day of the Week')
ax1.set_ylabel('Customers')
ax2.set_xlabel('Day of the Week')

ax1.plot(p_daily)
ax2.plot(s_daily)

######### distribution of bike-rides by season - Porto
season = data_porto.groupby("month")['total_count'] ###### riders by season
season.describe() #### summary statistics for each season
sns.boxplot('season', 'total_count', data=df).set_title('Porto, Portugal') ### boxplot

season = data_seoul.groupby("season")['count']
season.describe()
sns.boxplot('season','count', data=df2).set_title('Seoul, South Korea')


#Linear model
#C(x) indicates that x is a categorical variable 
model_porto = smf.ols('total_count ~ windspeed + temp + atemp + hum + C(season) + C(weathersit) + C(weekday)  + C(hour)', data = data_porto).fit() ## sm.OLS(output, input)

model_porto.summary()

# Print out the statistics


data_seoul = pd.read_csv('Seoul_hour_clean.csv')

model_seoul = smf.ols('count ~ rainfall + solar_rad + dew_point + visibility + windspeed + hum + temp + C(weekday) + C(hour) + C(season)', data = data_seoul).fit()

model_seoul.summary()


model_temp_porto = smf.ols('total_count~ temp + atemp + hum + windspeed+ C(season)+ C(weathersit)', data =data_porto).fit()

model_temp_porto.summary()



model_temp_seoul = smf.ols('count ~ rainfall + solar_rad + dew_point + visibility + windspeed + hum + temp + C(season)', data = data_seoul).fit()

model_temp_seoul.summary()

