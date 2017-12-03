from flask import Flask, render_template, request
import json
import os
import base64
import codecs
import data.classifier
import numpy as np
import nutrition_data as BiggestNut
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

    mo = data.classifier.model()
    pred = mo.predict_class('Stream.jpg')
    print(pred)
    possibilities = [item for (itemId, item, confidence) in pred[0] ]
    print(possibilities)
    bestGuess=possibilities[0]
    bestGuesses=json.dumps(possibilities)
    

    #look up facts
    print('Looking up Nutrition facts for: ',bestGuess)
    Nuts=BiggestNut.get_nutrition_data(bestGuess)
    # Nut=json.dumps(Nuts)
    print(Nuts)
    results=[possibilities, Nuts]
    resultsString=json.dumps(results)
    return resultsString
    # classifier.model("test.png")

if __name__ == "__main__":
    # sendStaticImage()
    # app.run()
    app.run(debug=True)
