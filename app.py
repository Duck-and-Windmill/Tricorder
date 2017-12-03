from flask import Flask, render_template, request
import json
import os
import base64
import codecs
import data.classifier
import kairos_face
import credentials
import numpy as np
import nutrition_data as BiggestNut

kairos_face.settings.app_id = credentials.app_id
kairos_face.settings.app_key = credentials.key


template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)
user = False

@app.route('/')
def main():
    print(kairos_face.get_gallery("hackathon"))
    return render_template("video.html")

@app.route('/send-static-image',  methods=["POST"])
def sendStaticImage():
    print('recieved image')
    save_image(request.form['image'], 'stream.jpg')

    model = data.classifier.model()
    pred = model.predict_class('stream.jpg')

    print(pred)

    possibilities = [item for (item_id, item, confidence) in pred[0]]
    print(possibilities)

    bestGuess = possibilities[0]
    bestGuesses = json.dumps(possibilities)

    # #look up facts
    # print('Looking up Nutrition facts for: ', bestGuess)
    # Nuts = BiggestNut.get_nutrition_data(bestGuess)
    # # Nut=json.dumps(Nuts)
    # print(Nuts)
    # results=[possibilities, Nuts]
    # resultsString=json.dumps(results)
    # return resultsString
    # # classifier.model("test.png")

    # if not user:
        # faces = kairos_face.recognize_face(file='stream.jpg', gallery_name='hackathon')
    print(classified)
    print(faces)

    return 'finished'


@app.route('/register-face', methods=['POST'])
def register_face():
    save_image(request.form['image'], 'face.jpg')
    return kairos_face.enroll_face(file='face.jpg', subject_id=request.form['name'], gallery_name='hackathon')

    # return 'finished'

def save_image(raw_data, name):
    image64 = raw_data.split(',')[1]
    image_data = bytes(image64, encoding='ascii')

    with open(name, 'wb') as f:
        f.write(base64.decodebytes(image_data))


if __name__ == "__main__":
    app.run()
