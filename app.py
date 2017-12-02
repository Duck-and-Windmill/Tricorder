from flask import Flask, render_template, request
import json
import os

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()