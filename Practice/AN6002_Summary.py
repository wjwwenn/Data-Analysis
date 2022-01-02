### Pandas Summary
import pandas as pd
import numpy as np

df = pd.read_csv("filename")
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.crosstab(df.col1, df.col2)
pd.pivot_table(index="room_type", data=df.loc[:, ["price", "room_type"]])

df.index, df.columns, df.values, df.shape, df.dtypes, df.str
df.head(), df.tail(), df.info(), df.describe(), df.isnull(), df.corr(), 
df.mean(), df.median(), df.mode(), df.std(), df.sum(),df.pct_change()
df.min(), df.max(), df.cov(), df.drop(row_index)
df.duplicated(), df.duplicated(subset="col1"), df.col1.isna()
df.replace(oldValue, newValue)
df.groupby(col_name)
df.col_name.fillna('newvalue')
df.col1.drop_duplicates(inplace=True)
df.unique(), df.nunique()
df.count()
df.value_counts()
df.quantile(0.25)

df[col_name] / df[[col1, col2]]
df[col_name][row_index]
df[df.col_name > 100] # data selection

df.colName[row_index]

df.loc[row_index, 'col name']
df.loc[df.col_name > 100] # data selection

df.iloc[row_index]
df.iloc[row_index, col_index]

df["price_cat"]= pd.cut(df.price, [0, 50, 100, 2000], labels=["Low", "Average", "High"])

### Numpy Summary
np.add(df.col, 10)
np.divide(),
np.subtract()
np.divide()
np.divmod()
np.mod(), 
np.power(), 
np.absolute(), 
np.log(), 
np.exp(),  
np.log10(), 
np.sum()
np.prod([[11, 22], [3, 4]], axis=1) # row product
np.argmax(df.Age) # max age index number
df['Age_np'] = np.where(df.Age < 40, "Forever Young", "Not so") # Data transformation
np.extract(df.Age == 19, df.Attrition) # data extraction

np.mean(df.col), np.std(), np.var(), 

# Numpy constant
# https://numpy.org/doc/stable/reference/constants.html
# np.nan

# # Numpy Statistics
# https://numpy.org/devdocs/reference/routines.statistics.html

### Seaborn summary
import seaborn as sns

sns.barplot(data=df, y="price", x="room_type")
sns.boxplot(data=df, y="price", x="room_type")
sns.boxplot(data=df[df.minimum_nights <7], y="number_of_reviews", x="minimum_nights")
sns.barplot(data=df, x="price", y="room_type", estimator=sum)