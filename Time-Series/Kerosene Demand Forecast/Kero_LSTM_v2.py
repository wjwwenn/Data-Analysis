# %% [code]
import tensorflow
import keras

# %% [code]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm_notebook as tqdm

# %% [code]
train_df = pd.read_csv("Kero.csv",parse_dates=['Month'],index_col='Month')

# %% [code]
train_df.head(10)

# %% [code]
plt.figure(figsize=(9,9))
plt.plot(train_df.index.year,train_df['Kerosene'])

# %% [code]
plt.figure(figsize=(9,9))
sns.lineplot(x=train_df.index,y='Kerosene',data=train_df)

# %% [code]
df_by_month = train_df.resample("M").sum()

plt.figure(figsize=(9,9))
sns.lineplot(x=df_by_month.index,y='Kerosene',data=df_by_month)

# %% [code]
plt.figure(figsize=(14,8))
sns.pointplot(x=train_df.index.hour,y='Kerosene',data=train_df)

# %% [code]
plt.figure(figsize=(11,5))
sns.pointplot(x=train_df.index.dayofweek,y='Kerosene',data=train_df)

# %% [code]
train_len =  int(0.8*len(train_df))
test_len = len(train_df) - train_len

train,test = train_df.iloc[:train_len],train_df.iloc[train_len:len(train_df)]
print(train_df.shape,train.shape,test.shape)

# %% [code]
#train_trans = train[['t1','t2','hum','wind_speed']].to_numpy()
#test_trans = test[['t1','t2','hum','wind_speed']].to_numpy()

# %% [code]
from sklearn.preprocessing import RobustScaler

# %% [code]
rs = RobustScaler()
rs_cnt = RobustScaler()

t_c = ['Temperature']

train.loc[:,t_c] = rs.fit_transform(train[t_c].to_numpy())
test.loc[:,t_c] = rs.transform(test[t_c].to_numpy())

# %% [code]
train['Kerosene'] = rs_cnt.fit_transform(train[['Kerosene']])
test['Kerosene'] = rs_cnt.transform(test[['Kerosene']])

# %% [code]
train.to_numpy()
test.to_numpy()

# %% [code]
def create_dataset(x,y,time_steps=1):
    x_train,y_train = [],[]
    
    for i in range(len(x)-time_steps):
        v = x.iloc[i:(i+time_steps)].values
        x_train.append(v)
        y_train.append(y.iloc[i+time_steps])
        
    return np.array(x_train),np.array(y_train)

# %% [code]
time_steps = 24

x_train,y_train = create_dataset(train,train.Kerosene,time_steps)
x_test,y_test = create_dataset(test,test.Kerosene,time_steps)

print(x_train.shape,y_train.shape)

# %% [code]
from keras.models import Sequential
from keras.layers import Dense,LSTM ,Bidirectional,Dropout

# %% [code]
model = Sequential()

model.add(Bidirectional(LSTM(128,
                            input_shape=(x_train.shape[1],x_train.shape[2]))))
model.add(Dropout(0.25))
model.add(Dense(1))

model.compile(loss='mse',optimizer='adam', run_eagerly=True)

# %% [code]
history = model.fit(x_train,y_train,
                   epochs=30,
                   batch_size=32,
                   validation_split=0.1,
                   shuffle=False 
                   )

# %% [code]
plt.plot(history.history['loss'],label='train')
plt.plot(history.history['val_loss'],label='test')
plt.legend()

# %% [code]
# New issue with the code: ValueError: Unexpected result of `predict_function` (Empty batch_outputs). Please use `Model.compile(..., run_eagerly=True)`, or `tf.config.run_functions_eagerly(True)` 
y_pred = model.predict(x_test)

# %% [code]
y_test_inv = rs_cnt.inverse_transform(y_test.reshape(1,-1))
y_pred_inv = rs_cnt.inverse_transform(y_pred)

# %% [code]
plt.figure(figsize=(12,12))
plt.plot(y_test_inv.flatten(), marker='.', label="true")
plt.plot(y_pred_inv.flatten(), 'r', label="prediction")
plt.ylabel('Kero')
plt.xlabel('Months')
plt.legend()
plt.show();
