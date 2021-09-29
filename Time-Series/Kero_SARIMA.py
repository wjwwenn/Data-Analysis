import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# pip install pyramid-arima
# pyramid - bringing R's auto.arima to python 
import pmdarima as pm

# SARIMA - Seasonal Autoregressive Integrated Moving Average 
# Inclusive of seasonality. 
# p: no. of lag observations included in the model i.e. lag order
# d: no. of times that the raw observations are differenced i.e.  degree of differencing
# q: size of the moving average window i.e. order of moving average

data = pd.read_csv('/Users/jingwen.wang/PycharmProjects/KeroTemperature/Japan_SD_Data.csv', sep = ',', parse_dates= ['Month'])   
Kero = data[['Kerosene']]

# Plot for two graphs - Usual and Seasonal Differencing
fig, axes = plt.subplots(2, 1, figsize=(10,5), dpi=100, sharex=True)

# Usual Differencing
axes[0].plot(Kero[:], label='Original Series')
axes[0].plot(Kero[:].diff(1), label='Usual Differencing')
axes[0].set_title('Usual Differencing')
axes[0].legend(loc='upper right', fontsize=10)

# Seasonal Differencing
axes[1].plot(Kero[:], label='Original Series')
axes[1].plot(Kero[:].diff(12), label='Seasonal Differencing', color='red')
axes[1].set_title('Seasonal Differencing')
plt.legend(loc='upper right', fontsize=10)
plt.suptitle('Kerosene', fontsize=16)
plt.show()

# Seasonal - stepwise auto-ARIMA
seasonal_model = pm.auto_arima(Kero, start_p=1, start_q=1,
                         test='adf',
                         max_p=3, max_q=3, m=12,
                         start_P=0, seasonal=True,
                         d=None, D=1, trace=True,
                         error_action='ignore',  
                         suppress_warnings=True, 
                         stepwise=True)

seasonal_model.summary()
# Best model - SARIMAX (3,0,3)(2,1,2)[12] intercept
# Intercept p value < 0.05, statistically significant
# AIC 6200.430
# Kurtosis - heavier tails than a normal distribution 

# Forecast
n = 600
fitted, confint = seasonal_model.predict(n_periods=n, return_conf_int=True) # confidence interval 
forecast_index = pd.date_range(Kero.index[1], periods=n, freq='MS') # frequency by months 

# Series to plot
fitted_series = pd.Series(fitted, index=forecast_index)
lower_series = pd.Series(confint[:, 0], index=forecast_index)
upper_series = pd.Series(confint[:, 1], index=forecast_index)

# Plot
plt.plot(Kero)
plt.plot(fitted_series, color='darkred')
plt.fill_between(lower_series.index, 
                 lower_series, 
                 upper_series, 
                 color='k', alpha=.1) #alpha shows the grey area 

plt.title("SARIMA - Kerosene Forecast")
plt.show()
