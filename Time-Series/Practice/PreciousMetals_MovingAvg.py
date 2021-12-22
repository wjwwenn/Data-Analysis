import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 

# Y = T + C + S + I
# T = train, c = cyclic, s = seasonality, irregularity (error)
# Y = T x C x S x I
# noise should not have pattern (look at resid)

## Moving average
df = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 5/Commodity_a.csv", index_col=0)
data = pd.DataFrame({"Period": [i for i in range(10)]})
data
data.rolling(window=2).mean()
data.ewm(span=2).mean()
dfa_loc = df.iloc[:320]
dfa_loc.shape
dfa_loc.columns
sma2 = dfa_loc.rolling(window=2)
df2 = sma2.mean()

# Platinum
plt.plot(df.index, df['Platinum'])
plt.plot(df.index, df2['Platinum'])
plt.legend(loc = 'upper left')

# Gold
plt.plot(df.index, df['Gold'])
plt.plot(df.index, df2['Gold'])
plt.legend(loc = 'upper left')

# Silver
plt.plot(df.index, df['Silver'])
plt.plot(df.index, df2['Silver'])
plt.legend(loc = 'upper left')
 
#### Another example with Platinum
df = df[["Platinum"]]
df = df.interpolate()
train_size = int(len(df) * 0.9)
test_size = len(df) - train_size
train, test = df.iloc[0:train_size], df.iloc[train_size:len(df)]
print(len(train), len(test))

pred = test.copy()
pred['MA'] = train.iloc[:,0].rolling(60).mean().iloc[-1]
mean_squared_error(pred['MA'],test["Platinum"])**0.5

plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(pred['MA'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.show()

dfb = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 5/Commodity_b.csv")
dfc = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 5/Commodity_c.csv")
dfd = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 5/Commodity_d.csv")
