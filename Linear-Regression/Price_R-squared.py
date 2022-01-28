import pandas as pd
from sklearn.metrics import r2_score

df = pd.read_csv('/Users/jingwen.wang/Desktop/Python/OmanPrices.csv', parse_dates=['Date'])
df.apply(pd.to_numeric)
df = df.fillna(0)

X = df[["TR"]]
y = df[["DME"]]
z = df[["Argus"]]

## y is the actual value and X/z is the predicted value
## y is DME prices comparing against X/z - TR and Argus
r2_TR = r2_score(y, X)
print('r2 score for DME and TR', r2_TR)

r2_Argus = r2_score(y, z)
print('r2 score for DME and Argus', r2_Argus)