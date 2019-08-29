# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:50:53 2018

@author: Ravuri Srinivas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from keras.models import Sequential
from keras.layers import Dropout,Dense,BatchNormalization,LSTM, GaussianNoise
from keras import optimizers
from keras.models import model_from_json
from sklearn.metrics import confusion_matrix
from keras.callbacks import ModelCheckpoint,EarlyStopping
from keras.models import load_model
import seaborn as sns
import keras

early_stopper = EarlyStopping(patience=5)

file_name = 'left_leg_Arvind.txt'
seed = 7
np.random.seed(seed)

######### Comment the following lines based on number of classes to be classified ##############

no_class = 2
# no_class = 7


############# Loading the Dataset ###################

data = pd.read_csv(file_name,sep="\t",header=None, index_col= False)

Xl = data.iloc[:,1:11].values
yl = data.iloc[:,11].values


 ######## Normalization of the data  ###################### 
#scaler = MinMaxScaler(feature_range=(0, 1))
#scaler = scaler.fit(Xl)
#scaled_X = scaler.transform(X)
#scaler = scaler.fit(Xr)
#scaled_Xr = scaler.transform(Xr)

############### Label Encoding ########################

encoder = LabelEncoder()
encoder.fit(yl)

if no_class == 2:

	Yl = encoder.fit_transform(yl)

if no_class > 2:

	Yl = keras.utils.to_categorical(Yl)


############ Splitting data for Train & Validation ###############################

Xl_train, Xl_test,Yl_train,Yl_test = train_test_split(Xl,Yl,test_size=0.20,shuffle=False)

################## Neural Network Model #########################


model = Sequential()
model.add(Dense(768, input_dim=10 , kernel_initializer="uniform", activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(768, kernel_initializer="uniform",activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(768 , kernel_initializer="uniform",activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(768, kernel_initializer="uniform",activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))

if no_class == 2:
	model.add(Dense(1, activation='sigmoid'))

if no_class > 2:
	model.add(Dense(no_class, activation='softmax'))

filepath = 'GaitNet.h5'

model.compile(optimizer='adagrad', loss='binary_crossentropy', metrics=['accuracy'])

history=model.fit(Xl_train, Yl_train, batch_size=64, epochs=100, verbose=2, validation_data =(Xl_test,Yl_test))

score = model.evaluate(Xl_test, Yl_test, verbose=0)
classes = model.predict_classes(Xl_test, batch_size=64)
model.save_weights(filepath)

print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))
plt.figure(figsize=(8,5))
#plt.plot(history.history['loss'], linewidth=2.0,label='train')
plt.plot(history.history['acc'], linewidth=2.0,label='train_acc')
#plt.plot(history.history['val_loss'], label='validation')
plt.plot(history.history['val_acc'], label='validation')
plt.grid(linestyle='--', linewidth=1.0)
plt.title('Training Progress', fontsize=14)
plt.xlabel('Epochs',fontsize=12)
plt.ylabel('Training Progress (accuracy)',fontsize=12)
plt.legend()
#plt.savefig('DNN.png')
plt.show()

#print('Gait Net Model Saved')


############# Inference #######################


#model.load_weights("GaitClassNet.h5")
#print("Loaded model from disk")
#score = model.evaluate(Xl_test, Yl_test, verbose=0)
#predictions = model.predict_classes(Xl_test, batch_size=64)
#print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))
cnf = confusion_matrix(Yl_test,classes)
#
#
########## Confusion Matrix ####################
ax= plt.subplot()
sns.heatmap(cnf, annot=True, ax = ax); #annot=True to annotate cells
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(['stance', 'swing']); ax.yaxis.set_ticklabels(['stance', 'swing'])

