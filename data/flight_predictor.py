from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from keras.models import Sequential
from keras.layers import Activation
from keras.optimizers import SGD
from keras.layers import Dense
from keras.utils import np_utils
from imutils import paths
import numpy as np
import argparse
import cv2
import os
import pandas as pd

df = pd.read_csv('JetBlue_data.csv')
dataset = []

for row in range(df.length):
	dataset.append(data_point = (row[1], row[2], row[3], row[6], row[7], row[8], row[9], row[10]))

#initialize model
model = Sequential()

#Add two layers
model.add(Dense(40, (8,)))
model.add(Dense(40))