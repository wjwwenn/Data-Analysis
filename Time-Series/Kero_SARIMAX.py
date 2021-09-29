import numpy as np
import pandas as pd
from pandas import DataFrame
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse
from matplotlib import pyplot

# SARIMAX - Seasonal Autoregressive Integrated Moving Average X - Exogenous
# future test: compare with TBATS/BATS
# variation of ARIMA
# endogenous: input variables influenced by other variables (opp: exogenous)
# regression, multivariate, multi-step, dynamic, discontiguous

# DEMAND
df = pd.read_csv('/Users/jingwen/Desktop/Python_Projects/Japan_SD_Data.csv', sep = ',', parse_dates= ['Month'], encoding='utf-8-sig')    
df.head()
Kero = df[['Month', 'Kerosene']]

# GROUP KERO BY MONTHS
Kero['Month'] = pd.to_datetime(Kero['Month'])
Kero_adj = pd.DatetimeIndex(Kero.Month) #converting from pandas.core.series.Series to DatetimeIndex
cluster = Kero

df['Month']= pd.to_datetime(df['Month'], errors='coerce', format = "%mm-%d-%YYY").dt.strftime("%Y%m")
cluster['Month']= pd.to_datetime(cluster['Month']) # convert to datetime

# TEMPERATURE - Data processing. Need further work.
temp = pd.read_html('https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=3', header=0)
temp = temp[1] #retrieve dataframe from index = 1
df_temp = pd.DataFrame(temp) #convert list to df

df_merge_col = pd.merge(df_temp, Kero, left_index=True,right_index=True, how="outer")

# Below, a test of Kero decomposition - additive/multiplicative
# Multiplicative seasonal decomposition
result_mul = seasonal_decompose(Kero['Kerosene'],   # 3 years
                                model='multiplicative', 
                                period=1,
                                extrapolate_trend='freq')

seasonal_index = result_mul.seasonal[-12:].to_frame()
seasonal_index['Month'] = pd.to_datetime(seasonal_index.index).month
result_mul.plot()
pyplot.show()

# Additive seasonal decomposition
result_add = seasonal_decompose(Kero['Kerosene'],   # 3 years
                                model='additive', 
                                period=1,
                                extrapolate_trend='freq')

seasonal_index = result_add.seasonal[-12:].to_frame()
seasonal_index['Month'] = pd.to_datetime(seasonal_index.index).month
result_add.plot()
pyplot.show()

# difference between multiplicative and additive decomposition:
# additive: level + trend + seasonality + noise (linear-like behavior)
# multiplicative: level * trend * seasonality * noise (can be exponential/quadratic/curved line)
# if seasonality & residual are independent of trend, additive
# if dependent, multiplicative

# Level: the average value in the series
# Trend: the increasing or decreasing value in the series
# Seasonality: the repeating the short-term cycle in the series
# Noise: the random variation in the series
