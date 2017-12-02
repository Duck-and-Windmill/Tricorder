import numpy as np
import vgg16
from keras import predict

class model():

	def __init__(self, image):

		self.model = vgg16.VGG16(weights="imagenet")
		self.preds = self.model.predict(preprocess_input(image))
		print(decode_predictions(self.preds))

