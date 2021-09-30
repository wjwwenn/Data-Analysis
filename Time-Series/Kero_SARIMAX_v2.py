import pandas as pd
import seaborn as sns
import itertools
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot

# demand
df = pd.read_csv('/Users/jingwen.wang/Desktop/Python/Japan_SD_Data.csv', sep = ',', parse_dates= ['Month'], index_col='Month')
df.head()
Kero = df[["Kerosene"]]
cluster = Kero

# temperature
df_temp = pd.read_csv('/Users/jingwen.wang/Desktop/Python/Japan_Weather.csv', sep = ',', parse_dates= ['Month'], index_col='Month')
df_temp.head()

# merge demand with temperature data
df_merge_col = pd.merge(df_temp, Kero, left_index=True,right_index=True, how="inner")
df_merged = df_merge_col

# stationarity test
import statsmodels.tsa.stattools as sts
dftest = sts.adfuller(train.iloc[:,:].Kerosene)
print('ADF Statistic: %f' % dftest[0])
print('p-value: %f' % dftest[1])
print('Critical Values:')
for key, value in dftest[4].items():
  print('\t%s: %.3f' % (key, value))

# calculation
p = range(0, 3)
d = range(1,2)
q = range(0, 3)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for SARIMA:')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(df_merged[['Kerosene']],
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# Model:             SARIMAX(2, 1, 2)x(2, 1, 2, 12)
# AIC                           6250.444
import statsmodels.api as sm
model=sm.tsa.statespace.SARIMAX(df_merged['Kerosene'],order=(2, 1, 2),seasonal_order=(2,1,2,12))
results=model.fit()
print(results.summary())

# plot
df_merged['Forecast']=results.predict(start=180,end=333,dynamic=True)
df_merged[['Kerosene','Forecast']].plot(figsize=(12,8))
