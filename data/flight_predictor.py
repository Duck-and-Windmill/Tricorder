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

class model():

	def __init__():
		model = Sequential()
		
		model.add(Dense(40, (8,)), activation="sigmoid")
		model.add(Dense(40), activation="sigmoid")

	def get_data(arr, dest, date):
		df = pd.read_csv('JetBlue_data.csv')
		dataset = []

		places = {}
		for row in range(df.length):
			if row[1] not in places:
				places[row[1]] = 1
			if row[2] not in places:
				places[row[2]] = 1

			dataset.append(data_point = (row[1], row[2], row[3], row[6], row[7], row[8], row[9], row[10]))

		print(len(places))

		#X_train, X_test = 


model.get_data(1,1,1)


