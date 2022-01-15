# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:11:23 2021

@author: JingWen.Wang
"""

import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, TimeDistributed, Bidirectional
from sklearn.metrics import mean_squared_error, accuracy_score
from scipy.stats import linregress
from sklearn.utils import shuffle
from sklearn import preprocessing

df = pd.read_csv('/Users/jingwen.wang/Desktop/Python/Japan_SD_Data.csv', parse_dates=['Month'], index_col="Month")
df.info()
Kero = df[['Kerosene', 'Temperature']]
raw = Kero

scaler = MinMaxScaler(feature_range=(-1, 1))
raw = scaler.fit_transform(raw)

time_steps = 7
def create_ds(data, t_steps):
    data = pd.DataFrame(data)
    data_s = data.copy()
    for i in range(time_steps):
        data = pd.concat([data, data_s.shift(-(i+1))], axis = 1)   
    data.dropna(axis=0, inplace=True)
    return data.values

ds = create_ds(raw, time_steps)
print (ds.shape)
n_feats = raw.shape[1]
n_obs = time_steps * n_feats

n_rows = ds.shape[0]
train_size = int(n_rows * 0.8)

time_shift = 7 #shift = no. of steps vbpredicting ahead
train_size = int(n_rows * 0.8)

train_data = raw[:train_size, :] # first train_size steps, all 5 features
test_data = raw[train_size:, :] # beginning of the data as state adjuster

x_train = train_data[:-time_shift, :] # whole train data, except the last shift steps 
x_test = test_data[:-time_shift,:] # whole test data, except last shift steps
x_predict = raw[:-time_shift,:] # whole raw data, except last shift steps

y_train = train_data[time_shift:, :] 
y_test = test_data[time_shift:,:]
y_predict_true = raw[time_shift:,:]

x_train = x_train.reshape(1, x_train.shape[0], x_train.shape[1]) # shape (1,steps,5) - 1 sequence, many steps, 5 features
y_train = y_train.reshape(1, y_train.shape[0], y_train.shape[1])
x_test = x_test.reshape(1, x_test.shape[0], x_test.shape[1])
y_test = y_test.reshape(1, y_test.shape[0], y_test.shape[1])
x_predict = x_predict.reshape(1, x_predict.shape[0], x_predict.shape[1])
y_predict_true = y_predict_true.reshape(1, y_predict_true.shape[0], y_predict_true.shape[1])

print("\nx_train:")
print (x_train.shape)
print("y_train")
print (y_train.shape)
print("x_test")
print (x_test.shape)
print("y_test")
print (y_test.shape)

model = Sequential()
n_feats = Kero.shape[1]
model.add(LSTM(64, return_sequences=True, input_shape=(None, x_train.shape[2])))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(256, return_sequences=True))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(64, return_sequences=True))
model.add(LSTM(n_feats, return_sequences=True)) 

model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=2, validation_data=(x_test,y_test))

y_predict_model = model.predict(x_predict)
n_rows = Kero.shape[0] #n_rows is the number of time steps of our sequence
print("\ny_predict_true:")
print (y_predict_true.shape)
print("y_predict_model: ")
print (y_predict_model.shape)

def plot(true, predicted, divider):
    predict_plot = scaler.inverse_transform(predicted[0])
    true_plot = scaler.inverse_transform(true[0])
    predict_plot = predict_plot[:,0]
    true_plot = true_plot[:,0]
    plt.figure(figsize=(16,6))
    plt.plot(true_plot, label='True',linewidth=5)
    plt.plot(predict_plot,  label='Predict',color='y')
    if divider > 0:
        maxVal = max(true_plot.max(),predict_plot.max())
        minVal = min(true_plot.min(),predict_plot.min())
        plt.plot([divider,divider],[minVal,maxVal],label='train/test limit',color='k')
    plt.legend()
    plt.show()

test_size = n_rows - train_size
print("test length: " + str(test_size))

plot(y_predict_true,y_predict_model,train_size)
plot(y_predict_true[:test_size],y_predict_model[:test_size],test_size)
