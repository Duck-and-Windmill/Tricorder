from flask import Flask, render_template, request
import json
import os
import base64 
import data.classifier

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/sendStaticImage',  methods=["POST"])
def sendStaticImage():

	# with open("data/img/banana.jpg", "rb") as image_file:
		# encoded_string = base64.b64encode(image_file.read())

	image64=request.form['image']
	image64=encoded_string
	image=base64.decodestring(image64)
	print(image)
	
	fh = open("test.png", "wb")
	fh.write(image)
	fh.close()
	classifier.model("test.png")

if __name__ == "__main__":
	# sendStaticImage()
	app.run()	
