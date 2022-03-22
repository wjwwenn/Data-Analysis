# VECM - Vector Error Correcting Model
# VECM = VAR model with cointegration constraints

# ECM is important to better understand long-run dynamic
# Can be derived from auto-regressive disributed lag model as there is a cointegration relationship between variables
# Thus, each equation in the VAR model is an autoregressive distributed lag model

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import datetime, pickle, copy, warnings
from pandas import DataFrame, merge, concat
import glob
from matplotlib import pyplot as plt
plt.style.use('dark_background')

df = pd.read_csv('April_data_6series.csv')
df.sample(5)

# Data Cleaning -------------------------------------------------------------
df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)
df = df.set_index('timestamp')
df.index = pd.to_datetime(df.index)
df.info()

# Select subset of data ------------------------------------------------------
X = df[:15000]
plt.style.use('dark_background')
def plot_vars(train, levels, color, leveltype):
    
    """
    Displays historical trends of variables
    And see if it's sensible to just select levels instead of differences
    """
    fig, ax = plt.subplots(1, 6, figsize=(16,3), sharex=True)
    for col, i in dict(zip(levels, list(range(6)))).items():
        X[col].plot(ax=ax[i], legend=True, linewidth=1.0, color=color, sharex=True)     
    
    fig.suptitle(f"Historical trends of {leveltype} variables", 
                 fontsize=12, fontweight="bold")
    
plot_vars(X.values, levels = X.columns, color="red", leveltype="levels")
plt.tight_layout()

# Augmented Dickey-Fuller Test [Ad Fuller Test] ------------------------------
from statsmodels.tsa.stattools import adfuller
def adfuller_test(series, signif=0.05, name='', verbose=False):
    """Perform ADFuller to test for Stationarity of given series and print report"""
    r = adfuller(series, autolag='AIC')
    output = {'test_statistic':round(r[0], 4), 'pvalue':round(r[1], 4), 'n_lags':round(r[2], 4), 'n_obs':r[3]}
    p_value = output['pvalue'] 
    def adjust(val, length= 6): return str(val).ljust(length)

    # Summary
    print(f'    Augmented Dickey-Fuller Test on "{name}"', "\n   ", '-'*47)
    print(f' Null Hypothesis: Data has unit root. Non-Stationary.')
    print(f' Significance Level    = {signif}')
    print(f' Test Statistic        = {output["test_statistic"]}')
    print(f' No. Lags Chosen       = {output["n_lags"]}')

    for key,val in r[4].items():
        print(f' Critical value {adjust(key)} = {round(val, 3)}')

    if p_value <= signif:
        print(f" => P-Value = {p_value}. Rejecting Null Hypothesis.")
        print(f" => Series is Stationary.")
    else:
        print(f" => P-Value = {p_value}. Weak evidence to reject the Null Hypothesis.")
        print(f" => Series is Non-Stationary.")
        
# ADF Test on each column
for name, column in X.iteritems():
    adfuller_test(column, name=column.name)
    print()
    
# KPSS Test ------------------------------------------------------------------
# Unit root test for stationarity 
from statsmodels.tsa.stattools import kpss
def kpss_test(x, h0_type='c'):
    indices = ['Test Statistic', 'p-value', '# of Lags']
    kpss_test = kpss(x, regression=h0_type, nlags ='auto')
    results = pd.Series(kpss_test[0:3], index=indices)
    for key, value in kpss_test[3].items():
        results[f'Critical Value ({key})'] = value
        return results
    
print('KPSS-EURUSD:')
print(kpss_test(X.eurusd))
print('___________________')
print('KPSS-GBPUSD:')
print(kpss_test(X.gbpusd))
print('___________________')
print('KPSS-USDJPY:')
print(kpss_test(X.usdjpy))
print('___________________')
print('KPSS-GC:')
print(kpss_test(X.gc))
print('___________________')
print('KPSS-NQ:')
print(kpss_test(X.nq))
print('___________________')
print('KPSS-ES:')
print(kpss_test(X.es))

# Stats ----------------------------------------------------------------------
from scipy import stats

stat,p = stats.normaltest(X.eurusd)
print('Statistics=%.3f, p=%.3f' % (stat,p))
alpha = 0.05
if p > alpha:
    print('EURUSD Data looks Gaussian (fail to reject H0)')
else:
    print('EURUSD Data do not look Gaussian (reject H0)')
print('______________')

stat,p = stats.normaltest(X.gbpusd)
print('Statistics=%.3f, p=%.3f' % (stat,p))
alpha = 0.05
if p > alpha:
    print('GBPUSD Data looks Gaussian (fail to reject H0)')
else:
    print('GBPUSD Data do not look Gaussian (reject H0)')
print('______________')

stat,p = stats.normaltest(X.usdjpy)
print('Statistics=%.3f, p=%.3f' % (stat,p))
alpha = 0.05
if p > alpha:
    print('USDJPY Data looks Gaussian (fail to reject H0)')
else:
    print('USDJPY Data do not look Gaussian (reject H0)')
print('______________')

stat,p = stats.normaltest(X.es)
print('Statistics=%.3f, p=%.3f' % (stat,p))
alpha = 0.05
if p > alpha:
    print('ES Data looks Gaussian (fail to reject H0)')
else:
    print('ES Data do not look Gaussian (reject H0)')
print('______________')

stat,p = stats.normaltest(X.nq)
print('Statistics=%.3f, p=%.3f' % (stat,p))
alpha = 0.05
if p > alpha:
    print('NQ Data looks Gaussian (fail to reject H0)')
else:
    print('NQ Data do not look Gaussian (reject H0)')
print('______________')

stat,p = stats.normaltest(X.gc)
print('Statistics=%.3f, p=%.3f' % (stat,p))
alpha = 0.05
if p > alpha:
    print('GC Data looks Gaussian (fail to reject H0)')
else:
    print('GC Data do not look Gaussian (reject H0)')
print('______________')

print('EURUSD: Kurtosis of normal distribution: {}'. format(stats.kurtosis(X.eurusd)))
print('EURUSD: Skewness of normal distribution: {}'. format(stats.skew(X.eurusd)))
print('************')

print('GBPUSD: Kurtosis of normal distribution: {}'. format(stats.kurtosis(X.gbpusd)))
print('GBPUSD: Skewness of normal distribution: {}'. format(stats.skew(X.gbpusd)))
print('************')

print('USDJPY: Kurtosis of normal distribution: {}'. format(stats.kurtosis(X.usdjpy)))
print('USDJPY: Skewness of normal distribution: {}'. format(stats.skew(X.usdjpy)))
print('************')

print('ES: Kurtosis of normal distribution: {}'. format(stats.kurtosis(X.es)))
print('ES: Skewness of normal distribution: {}'. format(stats.skew(df.es)))
print('************')

print('NQ: Kurtosis of normal distribution: {}'. format(stats.kurtosis(X.nq)))
print('NQ: Skewness of normal distribution: {}'. format(stats.skew(X.nq)))
print('************')

print('GC: Kurtosis of normal distribution: {}'. format(stats.kurtosis(X.gc)))
print('GC: Skewness of normal distribution: {}'. format(stats.skew(X.gc)))
print('************')

# Plot (EURUSD) --------------------------------------------------------------
pd.options.display.float_format = "{:.2f}".format
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
X['eurusd'].hist(bins=50)
plt.title('EURUSD')
plt.subplot(1,2,2)
stats.probplot(df['eurusd'], plot=plt);
X['eurusd'].describe().T

# Plot (GBPUSD) --------------------------------------------------------------
pd.options.display.float_format = "{:.2f}".format
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
X['gbpusd'].hist(bins=50)
plt.title('GBPUSD')
plt.subplot(1,2,2)
stats.probplot(df['gbpusd'], plot=plt);
X['gbpusd'].describe().T

# Plot (USDJPY) --------------------------------------------------------------
pd.options.display.float_format = "{:.2f}".format
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
X['usdjpy'].hist(bins=50)
plt.title('USDJPY')
plt.subplot(1,2,2)
stats.probplot(df['usdjpy'], plot=plt);
X['usdjpy'].describe().T

# Plot (ES) --------------------------------------------------------------
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
X['es'].hist(bins=50)
plt.title('ES')
plt.subplot(1,2,2)
stats.probplot(df['es'], plot=plt);
X['es'].describe().T

# Plot (GC) --------------------------------------------------------------
plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
X['gc'].hist(bins=50)
plt.title('gc')
plt.subplot(1,2,2)
stats.probplot(df['gc'], plot=plt);
X['gc'].describe().T

import seaborn as sns
# Correlation Matrix ------------------------------------------------------
corr = X.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(10, 10))

# Heatmap with the mask and correct aspect ratio
sns.heatmap(corr, annot=True, fmt = '.4f', mask=mask, center=0, square=True, linewidths=.5)
print("value > 0.5 is considerred correlated, > 0.8 is highly correlated")
plt.show()
print('Correlation matrix:')
corr = X.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)

# Granger Causality Test ----------------------------------------------------
from statsmodels.tsa.stattools import grangercausalitytests
max_lag = 6
test = 'ssr_chi2test'
def causation_matrix(data, variables, test='ssr_chi2test', verbose=False):
    X = DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)
    for c in X.columns:
        for r in X.index:
            test_result = grangercausalitytests(data[[r, c]], maxlag = max_lag, verbose = False)
            p_values = [round(test_result[i+1][0][test][1],4) for i in range(max_lag)]
            if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')
            min_p_value = np.min(p_values)
            X.loc[r, c] = min_p_value
    X.columns = [var + '-x axis' for var in variables]
    X.index = [var + '-y axis' for var in variables]
    return X
causation_matrix(X, variables = X.columns)

from statsmodels.tsa.vector_ar.vecm import VECM, select_order
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from statsmodels.tsa.vector_ar.vecm import select_coint_rank
from statsmodels.tsa.vector_ar.vecm import CointRankResults

nobs = 15
train_ecm, test_ecm = X[0:-nobs], X[-nobs:]

# Check Size -----------------------------------------------------------------
print(train_ecm.shape)  
print(test_ecm.shape)

# VECM Model Fitting ---------------------------------------------------------
from statsmodels.tsa.vector_ar import vecm
# pass "1min" frequency
train_ecm.index = pd.DatetimeIndex(train_ecm.index).to_period('1min')
model = vecm.select_order(train_ecm, maxlags=8)
print(model.summary())

# Johansen Co-Integration ----------------------------------------------------
pd.options.display.float_format = "{:.2f}".format
"""definition of det_orderint:
-1 - no deterministic terms; 0 - constant term; 1 - linear trend"""
pd.options.display.float_format = "{:.2f}".format
model = coint_johansen(endog = train_ecm, det_order = 1, k_ar_diff = 3)
print('Eigen statistic:')
print(model.eig) 
print()
print('Critical values:')
d = DataFrame(model.cvt)
d.rename(columns = {0:'90%', 1: '95%', 2:'99%'}, inplace=True)
print(d); print()
print('Trace statistic:')
print(DataFrame(model.lr1)) 

# Cointegration Rank Determination -------------------------------------------
from statsmodels.tsa.vector_ar.vecm import select_coint_rank
rank1 = select_coint_rank(train_ecm, det_order = 1, k_ar_diff = 3,
                                   method = 'trace', signif=0.01)
print(rank1.summary())

rank2 = select_coint_rank(train_ecm, det_order = 1, k_ar_diff = 3, 
                              method = 'maxeig', signif=0.01)

print(rank2.summary())

# VECM Fitting ---------------------------------------------------------------
vecm = VECM(train_ecm, k_ar_diff=3, coint_rank = 3, deterministic='ci')
"""estimates the VECM on the prices with 3 lags, 3 cointegrating relationship, and 
a constant within the cointegration relationship"""
vecm_fit = vecm.fit()
print(vecm_fit.summary())

# Residual Auto-Correlation --------------------------------------------------
from statsmodels.stats.stattools import durbin_watson
out = durbin_watson(vecm_fit.resid)
for col, val in zip(train_ecm.columns, out):
    print((col), ':', round(val, 2))
    
# Impulse-Response Plot ------------------------------------------------------
from statsmodels.tsa.vector_ar import irf
irf = vecm_fit.irf(15)
irf.plot(orth = False)
plt.show()

plt.style.use('ggplot')
irf.plot(impulse='eurusd')
plt.show()

plt.style.use('ggplot')
irf.plot(impulse='usdjpy', orth = True)
plt.show()

plt.style.use('ggplot')
irf.plot(impulse='es')
plt.show()

plt.style.use('ggplot')
irf.plot(impulse='gc')
plt.show()

plt.style.use('ggplot')
irf.plot(impulse='nq')
plt.show()

# Prediction -----------------------------------------------------------------
pd.options.display.float_format = "{:.2f}".format
forecast, lower, upper = vecm_fit.predict(nobs, 0.05)
print("lower bounds of confidence intervals:")
print(DataFrame(lower.round(2)))
print("\npoint forecasts:")
print(DataFrame(forecast.round(2)))
print("\nupper bounds of confidence intervals:")
print(DataFrame(upper.round(2)))

pd.options.display.float_format = "{:.2f}".format
forecast = DataFrame(forecast, index= test_ecm.index, columns= test_ecm.columns)
forecast.rename(columns = {'eurusd':'eurusd_pred', 'gbpusd':'gbpusd_pred', 'usdjpy':'usdjpy_pred',
                    'gc':'gc_pred', 'nq':'nq_pred', 'es':'es_pred'}, inplace = True)
forecast

combine = concat([test_ecm, forecast], axis=1)
pred = combine[['eurusd', 'eurusd_pred', 'gbpusd', 'gbpusd_pred', 'usdjpy', 
                   'usdjpy_pred', 'gc', 'gc_pred', 'nq', 'nq_pred', 'es', 'es_pred']]

def highlight_cols(s):
    color = 'yellow'
    return 'background-color: %s' % color

pred.style.applymap(highlight_cols, subset=pd.IndexSlice[:, ['eurusd_pred', 'gbpusd_pred', 'usdjpy_pred',
                                                               'gc_pred', 'nq_pred', 'es_pred']])

# MSE and MAE ----------------------------------------------------------------
from sklearn.metrics import mean_absolute_error, mean_squared_error

# score eur_usd
mae = mean_absolute_error(pred.eurusd, pred['eurusd_pred'])
mse = mean_squared_error(pred.eurusd, pred.eurusd_pred)
rmse = np.sqrt(mse)
sum = DataFrame(index = ['Mean Absolute Error', 'Mean squared error', 'Root mean squared error'])
sum['Accuracy metrics :    EURUSD'] = [mae, mse, rmse]

# score gbp_usd
mae = mean_absolute_error(pred.gbpusd, pred['gbpusd_pred'])
mse = mean_squared_error(pred.gbpusd, pred.gbpusd_pred)
rmse = np.sqrt(mse)
sum['GBPUSD'] = [mae, mse, rmse]

# score usd_jpy
mae = mean_absolute_error(pred.usdjpy, pred['usdjpy_pred'])
mse = mean_squared_error(pred.usdjpy, pred.usdjpy_pred)
rmse = np.sqrt(mse)
sum['USDJPY'] = [mae, mse, rmse]

# score nq
mae = mean_absolute_error(pred.nq, pred['nq_pred'])
mse = mean_squared_error(pred.nq, pred.nq_pred)
rmse = np.sqrt(mse)
sum['NQ'] = [mae, mse, rmse]

# score usd_jpy
mae = mean_absolute_error(pred.es, pred['es_pred'])
mse = mean_squared_error(pred.es, pred.es_pred)
rmse = np.sqrt(mse)
sum['ES'] = [mae, mse, rmse]

# score usd_jpy
mae = mean_absolute_error(pred.gc, pred['gc_pred'])
mse = mean_squared_error(pred.gc, pred.gc_pred)
rmse = np.sqrt(mse)
sum['GC'] = [mae, mse, rmse]
sum