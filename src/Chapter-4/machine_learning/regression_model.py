# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 21:12:54 2018

@author: Ravuri Srinivas
"""

import pandas as pd
import math
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dropout,Dense,BatchNormalization,LSTM
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import scipy.signal as signal




filename = 'data.txt'




####### convert series to supervised learning #######################
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = pd.DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = pd.concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg



############## Loading Dataset ############################
data = pd.read_csv(filename, sep="\t",header=None, index_col= False)
values = data.values

############### Preprocessing ###############################
encoder = LabelEncoder()

N  = 1    # Filter order
Wn = [0.02,0.2] # Cutoff frequency
B, A = signal.butter(N, Wn,btype= 'band', output='ba')
filter_shank = signal.filtfilt(B,A,values[:,9] )
values[:,9] = filter_shank 
values[:,11] = encoder.fit_transform(values[:,11])

scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
reframed = series_to_supervised(scaled, 1, 1)
reframed.drop(reframed.columns[[0,5,6,7,8,9,11]], axis=1, inplace=True)
data = reframed.values
#data = scaled
X = data[:,1:9]
Y = data[:,9]
train_X, test_X,train_Y,test_Y = train_test_split(X,Y,test_size=0.30, shuffle = False)

train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

print(train_X.shape, train_Y.shape, test_X.shape, test_Y.shape)

################# LSTM Network ################################

model = Sequential()
model.add(LSTM(100,input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1024, input_dim=8 , kernel_initializer="uniform", activation='relu'))
model.add(Dropout(0.2))
#model.add(Dense(64, activation='tanh'))
#model.add(Dense(256, kernel_initializer="uniform", activation='relu'))
#model.add(Dropout(0.5))
#model.add(Dense(512, kernel_initializer="uniform", activation='relu'))
#model.add(Dropout(0.2))
#model.add(Dense(512, kernel_initializer="uniform", activation='relu'))
#model.add(Dropout(0.2))
model.add(Dense(128, kernel_initializer="uniform", activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1))
#model.add(Dropout(0.5))

model.compile(loss='mean_squared_error', optimizer = 'adam')
history = model.fit(train_X,train_Y, epochs=100, batch_size=64, validation_data=(test_X,test_Y), verbose=2, shuffle=False)

# plot line graph
# plot history

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()


############### Inference ###############################


predict_y = model.predict(test_X)
rmse = math.sqrt(mean_squared_error(test_Y, predict_y))
filepath = 'RegressionGaitNet.h5'
model.save_weights(filepath)
print('Gait Net Model Saved')
print('Test RMSE:' ,rmse)
plt.figure(figsize=(10,10))
plt.plot(predict_y[0:100], label='predict')
plt.plot(test_Y[0:100], label='actual')
plt.legend()
plt.grid()
plt.show()
