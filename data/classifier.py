import numpy as np

class model():

	def __init__(self, image):

		self.model = VGG16(weights="imagenet")
		self.preds = self.model.predict(preprocess_input(imafge))
		print(decode_predictions(self.preds))

