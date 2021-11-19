import pandas as pd
import numpy as np

################################# EXAMPLE 1 ################################
df=np.random.randn(5, 3)
print(df)
df = pd.DataFrame(df, index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
print(df)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)

# CHECK FOR MISSING VALUES - isnull() or notnull()
print(df['one'].isnull())

# METHOD 1
# FILL MISSING DATA
print ("NaN replaced with '0':")
print(df.fillna(0))

# METHOD 2
# FILL NA Forward and Backward
print('Using fill methods')
print(df.fillna(method='pad'))

print('Replace all NaN elements with 0s.')
print(df.fillna(0))
print(df.fillna(method='ffill'))

# DROP MISSING VALUES
values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
print(df.fillna(value=values))

print(df)
print(df.dropna())

################################# EXAMPLE 2 ################################
# DROP COLUMNS
combinedData.drop(columns='customer_num', inplace=True)
combinedData.drop(columns='product_num', inplace=True)

# RENAME COLUMNS
combinedData = combinedData.rename(columns={'id_x':'purchase_id', 'id_y':'customer_id','id':'product_id'})

# FIND INCONSISTENT DATA
print(combinedData.dtypes)
print(combinedData.head(2))

# CHANGE DATA TYPE
print(pd.to_datetime(combinedData['purch_date'], errors='coerce').isnull().value_counts())
print(pd.to_numeric(combinedData['amount'], errors='coerce').isnull().value_counts())
print(pd.to_numeric(combinedData['paid'], errors='coerce').isnull().value_counts())
print(pd.to_numeric(combinedData['cost'], errors='coerce').isnull().value_counts())

# REPLACE/REMOVE SIGNS
combinedData.paid = combinedData['paid'].str.replace('$','')
combinedData.cost = combinedData['cost'].str.replace('$','')

# RAISE ERRORS
print(pd.to_numeric(combinedData['paid'], errors='raise'))

# DROP NA 
combinedData.dropna(subset = ['amount'], inplace=True)

print(combinedData.isnull().sum())
print(combinedData.shape)
print(combinedData.dtypes)

################################# EXAMPLE 3 ################################
# import libraries
import pandas as pd 
import numpy as np 
  
# Create dictionary 
dictionary = {'Name':['Alex', 'Mike', 'John', 'Dave', 'Joey'],
              'Height(m)': [1.75, 1.65, 1.73, np.nan, 1.82], 
              'Test Score':[70, np.nan, 84, 62, 73]} 
  
# Convert dictionary to dataframe 
df = pd.DataFrame(dictionary) 

##### Dealing with missing values
# CHECK MISSING VALUES
df.isnull().sum()

# DEALING WITH MISSING VALUES
df = df.fillna('*') 
df['Test Score'] = df['Test Score'].fillna('*') 

# # replace it with the average
df['Test Score'] = df['Test Score'].fillna(df['Test Score'].mean()) 

# take the average of the number above and below the missing value in the dataframe
df['Test Score'] = df['Test Score'].fillna(df['Test Score'].interpolate())

df= df.dropna() 

# delete rows with missing data in a certain column, e.g. the height column
df['Height(m)']= df['Height(m)'].dropna()  

##### Dealing with Non-standard missing values
# (isnull() function only picks up ‘Nan’, not other types of missing values such as a dash(‘-‘) or even ‘na’)
# dictionary of lists 
dictionary = {'Name':['Alex', 'Mike', 'John', 'Dave', 'Joey'],
              'Height(m)': [1.75, 1.65, '-', 'na', 1.82], 
              'Test Score':[70, np.nan, 84, 62, 73]} 
  
# creating a dataframe from list 
df = pd.DataFrame(dictionary) 

df.isnull() 

# CONVERT NA AND - TO NAN 
df = df.replace(['-','na'], np.nan)

##### Data in the wrong format
# dictionary of lists 
dictionary = {'Name':['Alex', 'Mike', 'John', 'Dave', 'Joey'],
              'Height(m)': [1.75, 1.65, '-', 'na', 1.82], 
              'Test Score':[70, 'yes', 84, 62, 73]} 
  
# creating a dataframe from list 
df = pd.DataFrame(dictionary) 

df = df.replace(['-','na','yes'], np.nan)