import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1
df = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 4/airbnb_clean.csv")
df.head()
df.columns
df.plot(kind="density", y="price") 
# y axis is the relative probability, highly probabable at the peak 100+
df.plot(kind="box", y="price") 

outliers = df[df.price > 400]
df.plot(kind="hist",y="price", bins=20) #bins to slice the histogram to be thinner
df.plot(kind="hist",y="price", bins=100) #bins to slice the histogram to be thinner

##### SEABORN
import seaborn as sns
sns.barplot(data=df, x="room_type", y="price") 
# black line shows CI, remove black line 
sns.barplot(data=df, x="room_type", y="price", ci=None)

import numpy as np
from numpy import median
# import median from numpy and then use median as estimator... 
# previous visual showed max 200, now its 175
sns.barplot(data=df, x="room_type", y="price", estimator=median, ci=None)

sns.barplot(data=df, x="minimum_nights", y="price", estimator=median, ci=None)

# with hue and filter for <14 days
sns.barplot(data=df[df.minimum_nights<14], x="minimum_nights", y="price", 
            estimator=median, ci=None, hue="room_type")

##### PIVOT TABLES
df[df.minimum_nights<10].pivot_table(index = "room_type", columns="minimum_nights", values="price").plot(kind="bar")

# cross tabulation - similar to pivot table
# count of minimum nights and room type
df1=df[df.minimum_nights<10]
pd.crosstab(df1.room_type, df1.minimum_nights).plot(kind="bar")

# histo
sns.histplot(data=df, x="price")

# boxplot
sns.boxplot(data=df, x="price", y="room_type")

##### MULTIPLE PLOTS ON SEABORN
# shared room shows a vertical 
# VIOLIN PLOT
import matplotlib.pyplot as plt
charts = sns.FacetGrid(df, col="room_type")
charts.map(sns.violinplot, "price")
df[df.room_type == "Shared room"]

# HISTOGRAM
charts = sns.FacetGrid(df, col="room_type")
charts.map(plt.hist, "price")

# PLOTLY
# pip install chart_studio
import plotly.express as px
# scatter
fig = px.scatter(df, x="price", y="number_of_reviews")
fig.show()

# pie
fig = px.pie(df, values="number_of_reviews", names="minimum_nights")
fig.show()

# sunbursts
fig = px.sunburst(df, path=["room_type"], values="price")
fig.show()

# apply lambda to get value quickly
# lambda calls the anonymous function within the item
# within the lambda, you pass the value
df['area'] = df.neighbour_hood_info.apply(lambda x:x.split(",")[0])
df.head()
fig = px.sunburst(df, path=["area","room_type"], values="price")
fig.show()

##### NEXT SECTION
df = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 4/commodity_a.csv")
df[['Gold']].mean()
df[['Silver']].mean()
df[['Platinum']].mean()

