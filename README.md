###CIS-9650-Project
###Iftikhar Ahmed, Colin Rojas, Ayesha Iftikar, Abel Roman

###A New Bike-Sharing Venture

###In this project we examined data from two bike-sharing programs in Porto, Portugal and Seoul, South Korea. 

###from UCI Machine Learning Repository, Center for Machine Learning and Intelligent Systems
###Portugal: [https://archive.ics.uci.edu/ml/datasets/bike%2Bsharing%2Bdataset], attribute information on webpage
###South Korea: [https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand], attribute information on webpage

###The aim is to analyze trends in these datasets and use those trends to inform decisions on how to develop and operate a new bike-sharing program. Are there observable differences in customers' use of the bike-sharing program? Is there variation between the Portuguese and Korean programs? Does weather matter to the success of the business? Can we quantify to what degree weather is an important variable?

###Clean-Up###
#To begin we cleaned and processed our two datasets. The datasets required that we: convert MM/DD/YYYY dates to DD/MM/YYYY dates, add a column that corresponds to the day of the week (where, 0 = sunday, 6 = saturday) and standardize column names between datasets. 

###Initial Look###
#We then examined the data by looking at trends over various time periods (days, weeks, months and years). Through a cursory inspection we observed four key trends. Firstly, both datasets exhibit nearly identical daily trends. In both Porto and Seoul we see bike-share ridership peak in the early morning and in the evening, presumably when people are commuting to and from work. We also observe that throughout the week (from Sunday to Saturday) ridership increases in both Porto and Seoul, though there are small differences in the shape of their curves. When comparing ridership throughout the seasons we see another similar trend. Ridership is lowest in the winter, with higher and more widely-spread distributions in the spring, summer and fall. Finally, we see that Porto and Seoul have relatively similar intra-yearly weather patterns. The two cities’ temperature and wind speed trends mirror each other closely, though there is a noticeable difference in their intra-yearly humidity profiles. These corresponding trends indicate that there are strong parallels between Porto and Seoul, as well as, how customers use these bike-sharing programs. This gives us confidence that these trends may be used to inform future decisions in developing and operating a new bike-sharing venture and warrant further analysis.

###Regression Analysis### 
#Use the regression.py file 
#To quantify how these factors may affect the success of a bike-sharing program we performed regression analysis using the statsmodel package in conjunction with pandas. We used an ordinary least squares model to look at how our data performs in predicting the number of riders every day. Using the linear regression model, we were able to see that the Porto and Seoul models have similar performance. We also concluded that temporal data like the day of the week and the hour are important when trying to predict ridership. We should try to find more important variables that would improve our model performance. 

###Conclusions###
#1.Customers tend to use the bike-share programs most in the morning and evening hours.
#2.Customers tend to use the programs more throughout the week.
#3.Customers tend to use the programs more and with greater variation in the spring, summer and fall.
#4.Day, time and weather hold a moderately-high amount of explanatory power in determining ridership.
#5.Removing day and time variables decrease the explanatory power of the model.
