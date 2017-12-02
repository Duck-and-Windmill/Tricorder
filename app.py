from flask import Flask, render_template, request
import json
import os
import base64 

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/sendStaticImage',  methods=["POST"])
def sendStaticImage():
	image64=request.form['image']
	image=base64.decodestring(image_64_encode)
	print(image)
	fh = open("test.png", "wb")
	fh.write(image)
	fh.close()

if __name__ == "__main__":
    app.run()	
