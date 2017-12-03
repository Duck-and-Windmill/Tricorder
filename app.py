from flask import Flask, render_template, request
import json
import os
import base64
import codecs
import data.classifier
import kairos_face
import credentials

kairos_face.settings.app_id = credentials.app_id
kairos_face.settings.app_key = credentials.key

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)
user = False

@app.route('/')
def main():
    return render_template("video.html")

@app.route('/sendStaticImage',  methods=["POST"])
def sendStaticImage():
    print('recieved image')
    image64 = request.form['image']
    # image64 = image64.split(',')[1]
    # image_data = bytes(image64, encoding="ascii")

    # with open('stream.jpg', 'wb') as fh:
    # 	fh.write(base64.decodebytes(image_data))

    save_image(request.form['image'], 'stream.jpg')
    classified = data.classifier.model('stream.jpg')

    if not user:
        faces = kairos_face.recognize_face(file='stream.jpg', gallery_name='hackathon')

    print(classified)
    print(faces)

    return 'finished'


@app.route('/register-face', methods=['POST'])
def register_face():
    save_image(request.form['image'], 'face.jpg')
    kairos_face.enroll_face(file=image_file, subject_id=request.form['name'], gallery_name='hackathon')


def save_image(raw_data, name):
    image64 = raw_data.split(',')[1]
    image_data = bytes(image64, encoding="ascii")

    with open(name, 'wb') as fh:
    	fh.write(base64.decodebytes(image_data))

    classified = data.classifier.model(raw_data)


if __name__ == "__main__":
    app.run()
