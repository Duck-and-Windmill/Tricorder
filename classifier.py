import numpy as np


model = VGG16(weights="imagenet")
preds = model.predict(preprocess_input(image))
print(decode_predictions(preds))