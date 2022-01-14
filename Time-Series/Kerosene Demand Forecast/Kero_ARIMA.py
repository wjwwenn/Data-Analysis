# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:15:12 2021

@author: JingWen.Wang
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf

# purpose: checking seasonality trend against demand of products
df = pd.read_csv('/Users/jingwen.wang/PycharmProjects/KeroTemperature/Japan_SD_Data.csv')
df

# plot visual 
df.plot(figsize=(20,10), linewidth=4, fontsize=20)
plt.xlabel('Months',fontsize=20)

# checking historical trend for kerosene
Kero = df[['Kerosene']]
Kero.rolling(12).mean().plot(figsize=(20,10), linewidth=4, fontsize=20)
plt.xlabel('Month', fontsize=20)

# checking seasonality
Kero.diff().plot(figsize=(20,10),linewidth=4, fontsize=20)
plt.xlabel('Month', fontsize=20)

# convert '/' in CSV file to blank, from string to float for ARIMA to function
df["Month"] = [float(str(i).replace("/", "")) for i in df["Month"]]

# ARIMA.
model = ARIMA(np.asarray(df['Kerosene']), order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# Log likelihood: maximum likelihood estimation / higher, better (for comparing models)
# AIC: Akaike's Information Criterion. evaluate strength of model. / lower, better.
# BIC: Baynesian Information Criterion. similar to AIC. / lower, better
# HQIC: Hannan-Quinn Information Criterion. feature selection. 

# ar.L1, ar.L2 - lag 1, lag 2...
# z = standardised coefficient = coef/std error 
# P > 0.05 = statistically not significant... 

# PACF - summary of relationship between observation in a time series with observations 
# at prior time steps with the relationship of in between observation removed 
plot_acf(df['Kerosene'], lags=50)
pyplot(show)

