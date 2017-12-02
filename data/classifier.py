import numpy as np
import vgg16
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.imagenet_utils import decode_predictions

class model():

	def __init__(self, img_path):
		model = vgg16.VGG16(include_top=True, weights='imagenet')

		img = image.load_img(img_path, target_size=(224, 224))
		x = image.img_to_array(img)
		
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
		print('Input image shape:', x.shape)
		preds = model.predict(x)
		print('Predicted:', decode_predictions(preds))
	

