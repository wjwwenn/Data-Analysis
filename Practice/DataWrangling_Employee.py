import pandas as pd
import numpy as np

df = pd.read_csv("/Users/jingwen/Desktop/Trimester 2/AN6002 Analytics and ML in Business/Class 2/Class/employee.csv")
df

# set maximum number of rows to none, dont set the limit
pd.set_option("display.max_rows", None)
df

# dont set maximum number of column to a certain number
pd.set_option("display.max_columns", None)
df

df.head()
df.tail()
df.info()

df.columns
# rows and corresponding columns (8687, 37)
df.shape

# sum of NA in individual columns
df.isna().sum() 

# sum of NA in all the columns
df.isna().sum().sum()
df.isnull().any(axis=1).sum()

# find duplicated number within the column
df.duplicated(subset="EmployeeNumber")
df.isnull()

df.duplicated().sum() # there are duplicated records
df[df.isna()].sum() #data selection

# column
df[df.isna()].loc[:, "Department"] #data selection
# row
df[df.isna()].loc[:, :"Department"] #data selection

# iloc: row number and column number
df[df.isna()].iloc[:, 4]

# beginning to column index number 4
df[df.isna()].iloc[:, :4]

# CLASS EXERCISE
# Q1 Add prefix E in front of Employee Number
df['EmployeeNumber'] = 'E' + df['EmployeeNumber'].astype(str)
df['EmployeeNumber']

# Q2 Replace Work Life Balance
df['WorkLifeBalance'].replace({1:'Bad',2:'Good',3:'Better',4:'Best'})

# Q3 Examine MonthlyRate and MonthlyIncome
# 4 NA, 4 blanks
weird_rows = []
for index, data in enumerate(df['MonthlyIncome']):
    try:
        float(data)
    except:
        print(index)
        weird_rows.append(index)
df.iloc[weird_rows, :]

df['MonthlyIncome'] = pd.to_numeric(df['MonthlyIncome'], errors='coerce')
df['MonthlyRate'] = pd.to_numeric(df['MonthlyRate'], errors='coerce')
df['MonthlyIncome'].isna().sum()  # 4
df['MonthlyRate'].isna().sum()  # 4
df = df.dropna(axis=0)

# Remove the integer rows in Gender column
integer_in_gender_column = [index for index, i in enumerate(df['Gender']) if i in df['Gender'].unique()[2:]]
df['Gender'][integer_in_gender_column]
df = df.drop(axis=0, index=integer_in_gender_column)

# Querying data more
df['Gender'].unique()
df['Age'].median()
df[df.JobRole == "Manager"].HourlyRate.median()
df[df.JobRole == "Research Scientist"].HourlyRate.median()
df[df.JobRole == "Sales Executive"].HourlyRate.median()

# Segmenting into bins
df["Age_Cat"]= pd.cut(df.Age, [0, 30, 40, 50, 100], labels=["Young", "30s", "40s", "OLD"])
df[df.Age_Cat == "Young"].describe()