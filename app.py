from flask import Flask, render_template, request
import json
import os
import base64
import codecs
import data.classifier

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    # return render_template("index.html")
    return render_template("video.html")

@app.route('/sendStaticImage',  methods=["POST"])
def sendStaticImage():
    # print(request)
    print('recieved image')
    image64 = request.form['image']
    image64 = image64.split(',')[1]
    # file = request.args.get('file')
    # starter = file.find(',')
    # image_data = file[starter+1:]
    # print(image64)
    image_data = bytes(image64, encoding="ascii")

    with open('Stream.jpg', 'wb') as fh:
    	fh.write(base64.decodebytes(image_data))
    fh.close

    mo = data.classifier.model('Stream.jpg')
    print(mo)
   

    return "test"

    # classifier.model("test.png")

if __name__ == "__main__":
    # sendStaticImage()
    # app.run()
    app.run(debug=True)
