import numpy as np 
import requests
import json
from bs4 import BeautifulSoup
import re
import firebase_admin
import firebase
from firebase_admin import credentials
from firebase_admin import db
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
import json

cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://eduroam-cbbfb.firebaseio.com'
})
ref = db.reference('/hosts')
hosts = ref.get()


def get_nutrition_data(image_class):
	url = "https://api.nal.usda.gov/ndb/search/?format=json&q=" + image_class + "&sort=n&max=1&offset=0&api_key=FLKBoKOh7C1apAA4bPL0jH4GAW6f2wS9Lw0a2iFu" 
	r = requests.get(url).json()
	ndbno = r["list"]["item"][0]["ndbno"]
	print(ndbno)

	nutrition_url = "https://api.nal.usda.gov/ndb/V2/reports?ndbno=01009&ndbno=" + ndbno + "&ndbno=35193&type=f&format=json&api_key=FLKBoKOh7C1apAA4bPL0jH4GAW6f2wS9Lw0a2iFu"
	nutrition_data = requests.get(nutrition_url)

	return json.dumps(nutrition_data.json())

print(get_nutrition_data("pizza"))
