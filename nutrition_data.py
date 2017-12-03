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
from fuzzyset import FuzzySet

cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://eduroam-cbbfb.firebaseio.com'
})
ref = db.reference('/hosts')
hosts = ref.get()


def get_nutrition_data(image_class):
	url = "https://api.nal.usda.gov/ndb/search/?format=json&q=" + image_class + "&sort=n&max=25&offset=0&api_key=FLKBoKOh7C1apAA4bPL0jH4GAW6f2wS9Lw0a2iFu"
	r = requests.get(url).json()

	max_dist_ratio = 0
	ndbno = 0
	for item in r["list"]["item"]:
		fs = FuzzySet()
		fs.add(image_class)
		ratio = fs.get(item["name"])[0][0]

		if ratio > max_dist_ratio:
			max_dist_ratio = ratio
			ndbno = item["ndbno"]

	print(ndbno)

	nutrition_url = "https://api.nal.usda.gov/ndb/V2/reports?ndbno=" + ndbno + "&type=f&format=json&api_key=FLKBoKOh7C1apAA4bPL0jH4GAW6f2wS9Lw0a2iFu"
	nutrition_data = requests.get(nutrition_url).json()

	nutrition_facts = {}
	nutrients = nutrition_data["foods"][0]["food"]["nutrients"]

	nutrition_facts["serve_size"] = str(nutrients[0]["measures"][0]["qty"]) + nutrients[0]["measures"][0]["eunit"]
	nutrition_facts["kcal"] = str(nutrients[0]["measures"][0]["value"]) + " calories"
	nutrition_facts["fat"] = str(nutrients[2]["measures"][0]["value"]) + " grams"
	nutrition_facts["carbs"] = str(nutrients[3]["measures"][0]["value"]) + " grams"
	nutrition_facts["protein"] = str(nutrients[1]["measures"][0]["value"]) + " grams"
	nutrition_facts["sugar"] = str(nutrients[4]["measures"][0]["value"]) + " grams"
	nutrition_facts["sodium"] = str(nutrients[5]["measures"][0]["value"]) + " milligrams"

	return nutrition_facts

print(get_nutrition_data("orange"))
