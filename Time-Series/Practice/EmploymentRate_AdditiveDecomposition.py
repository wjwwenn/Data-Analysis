import pandas as pd
from statsmodels.tsa.stattools import *
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 5/employment_rate.csv")
df['dateInt']=df['year'].astype(str) + df['month'].astype(str).str.zfill(2)+ df['day'].astype(str).str.zfill(2)
df['Date'] = pd.to_datetime(df['dateInt'], format='%Y%m%d')
print(df)
df = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 5/employment_rate.csv",
                 parse_dates=[['year', 'month', 'day']], index_col=0)

# 1. Construct the plots for low, middle and high income groups over months.
# 1 square bracket for lease data i.e. [], additional square bracket to make it like a table i.e. [[]]
# index_col allow x-axis to be processed automatically
# datetime is important to pick up the seasonal component
fig, ax = plt.subplots(1,1)
ax.plot(df.index.month, df.emp_combined_inclow, label = "Low Income")
ax.plot(df.index.month, df.emp_combined_incmiddle, label = "Mid Income")
ax.plot(df.index.month, df.emp_combined_inchigh, label = "High Income")
ax.legend()
ax.set_title("Employment Rates Changes in First 8 months of 2020")

"""
Notice the graph above showing 2 values for each month, the 2 values denote
the minimum and maximum within the give month. 
See the following details in number for low income group (Orange color form the above plot)

"""
df.emp_combined_inclow.groupby(df.index.month).describe()

# 2. Do they exhibit significant trend or seasonality?
result = adfuller(df.emp_combined)
print(f"Test Statistic: {result[0]}, p-value: {result[1]}")# ADF statistic and p-value.
"""
Null Hypothesis-> There is a unit root 
p-value
In this case, the test statistic is -3.09969
p-value is 0.0265 > 0.01 for 1% significance level, 
Hence null hypothesis that there is a unit root cannot be rejected 
so the data is non-stationary implying the presence of trend/seasonality
In the event of higher significance level, 
e.g. 5%, the null hypothesis will then be rejected and hence stationary.
"""
decomposed = seasonal_decompose(df.emp_combined, model="additive")
decomposed.plot() # The following plots display the trend and seasonal components found in emp_combined variable.

# Which month has the lowest employment rate?
df[df.emp_combined == df.emp_combined.min()].index.month_name() # April

# For emp_combined variable, which decomposition method is more appropriate? Why?
# decomposed = seasonal_decompose(df.emp_combined, model="multiplicative")
# decomposed.plot() 
# The above will result in error due to the presence of negative values.
# Hence, additive model is more suitable in this case.

# multiplicative assume a product of each other
# negative number comes from seasonality or train?
