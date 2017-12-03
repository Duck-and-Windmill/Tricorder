from flask import Flask, render_template, request
import json
import os
import base64
import codecs
# import data.classifier

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    # return render_template("index.html")
    return render_template("video.html")

@app.route('/sendStaticImage',  methods=["POST"])
def sendStaticImage():
    # print(request)

    image64 = request.form['image'].split(',')[1]
    print(type(image64))
    imagetest=bytes(image64, 'ascii')
    print(len(imagetest))
    test=base64.decodestring(imagetest)
    with open("test.jpg", "wb") as f:
        f.write(test)
        f.close()
    # print("remainder: " + str(len(image64) % 4))
    # print("type image64: " + str(type(image64)))
    # print(image64[0:50])
    # print(image64[-50:])
    # # print(len(image64))
    # # base64.decodestring(
    # # image = codecs.decode(image64.strip(), 'base64')
    # print(len(image64))
    # imageByte=bytes(str(image64), 'ascii')
    # missing_padding = len(imageByte) % 4
    # if missing_padding != 0:
    #     imageByte += b'='* (4 - missing_padding)
    #
    # # image= base64.b64decode(imageByte, '-_')
    # image = base64.decodestring(imageByte)
    #
    # # print("type image: " + str(type(image)))
    #
    # with open("test.jpg", "wb") as f:
    #     f.write(image)
    #     f.close()

    return "test"

    # classifier.model("test.png")

if __name__ == "__main__":
    # sendStaticImage()
    # app.run()
    app.run(debug=True)
