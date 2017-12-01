import numpy as np 
import scraper
import requests
from bs4 import BeautifulSoup
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

cred = credentials.Certificate('creds.json')
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://bastion-66cb2.firebaseio.com'
})
ref = db.reference('/hosts')
hosts = ref.get()

def index():
	with open('cache.txt', 'w+') as file:
		gen_categories = file.read()

		if not gen_categories:
			gen_categories = {
				"food": [],
				"sports": [],
				"finance": [],
				"music": [],
				"travel": [],
				"tech": [],
				"education": [],
				"entertainment": [],
				"fashion":[]
			}

			links = {
				"food": ['https://en.wikipedia.org/wiki/Food', 'https://en.wikipedia.org/wiki/Cooking', 'https://en.wikipedia.org/wiki/Cuisine', 'https://en.wikipedia.org/wiki/Snack'],
				"sports": ['https://en.wikipedia.org/wiki/Sport', 'https://en.wikipedia.org/wiki/Basketball', 'https://en.wikipedia.org/wiki/Tennis', 'https://en.wikipedia.org/wiki/Football', 'https://en.wikipedia.org/wiki/Swimming', 'https://en.wikipedia.org/wiki/Soccer', 'https://en.wikipedia.org/wiki/Running', 'https://en.wikipedia.org/wiki/volleyball', 'https://en.wikipedia.org/wiki/boxing', 'https://en.wikipedia.org/wiki/fitness'],
				"finance": ['https://en.wikipedia.org/wiki/Finance', 'https://en.wikipedia.org/wiki/Economics', 'https://en.wikipedia.org/wiki/Stocks', 'https://en.wikipedia.org/wiki/Business', 'https://en.wikipedia.org/wiki/Entrepreneurship', 'https://en.wikipedia.org/wiki/stock_market', 'https://en.wikipedia.org/wiki/trade', 'https://en.wikipedia.org/wiki/wall_street'],
				"music": ['https://en.wikipedia.org/wiki/music', 'https://en.wikipedia.org/wiki/music_festival', 'https://en.wikipedia.org/wiki/rap', 'https://en.wikipedia.org/wiki/hip_hop', 'https://en.wikipedia.org/wiki/rhythm'],
				"travel": ['https://en.wikipedia.org/wiki/travel', 'https://en.wikipedia.org/wiki/plane', 'https://en.wikipedia.org/wiki/resort', 'https://en.wikipedia.org/wiki/hotel', 'https://en.wikipedia.org/wiki/road_trip', 'https://en.wikipedia.org/wiki/vacation', 'https://en.wikipedia.org/wiki/city'],
				"tech": ['https://en.wikipedia.org/wiki/technology', 'https://en.wikipedia.org/wiki/innovation', 'https://en.wikipedia.org/wiki/computers', 'https://en.wikipedia.org/wiki/web_development', 'https://en.wikipedia.org/wiki/computer_programming', 'https://en.wikipedia.org/wiki/software_development', 'https://en.wikipedia.org/wiki/machines', 'https://en.wikipedia.org/wiki/artificial_intelligence', 'https://en.wikipedia.org/wiki/machine_learning'],
				"education": ['https://en.wikipedia.org/wiki/school', 'https://en.wikipedia.org/wiki/education', 'https://en.wikipedia.org/wiki/crash_course', 'https://en.wikipedia.org/wiki/university', 'https://en.wikipedia.org/wiki/college', 'https://en.wikipedia.org/wiki/class', 'https://en.wikipedia.org/wiki/learning', 'https://en.wikipedia.org/wiki/'],
				"entertainment": ['https://en.wikipedia.org/wiki/movie', 'https://en.wikipedia.org/wiki/youtube', 'https://en.wikipedia.org/wiki/television', 'https://en.wikipedia.org/wiki/shopping', 'https://en.wikipedia.org/wiki/gaming', 'https://en.wikipedia.org/wiki/videos', 'https://en.wikipedia.org/wiki/anime', 'https://en.wikipedia.org/wiki/cartoons', 'https://en.wikipedia.org/wiki/cable', 'https://en.wikipedia.org/wiki/entertainment'],
				"fashion":['https://en.wikipedia.org/wiki/clothing', 'https://en.wikipedia.org/wiki/shopping', 'https://en.wikipedia.org/wiki/fashion', 'https://en.wikipedia.org/wiki/hypebeast', 'https://en.wikipedia.org/wiki/shoes', 'https://en.wikipedia.org/wiki/brand', 'https://en.wikipedia.org/wiki/branding', 'https://en.wikipedia.org/wiki/style', 'https://en.wikipedia.org/wiki/mainstream']
			}

			for cat in links:
				for url in links[cat]:
					keys = scraper.find_keywords(scraper.scrape(url))
					gen_categories[cat].extend(keys)

			file.write(str(gen_categories))

		else: 
			gen_categories = eval(gen_categories)

		return gen_categories

def transform(url):
	categories = index()
	keys = scraper.find_keywords(scraper.scrape(url))

	match = {}
	for cat in categories:
		compare = set(categories[cat])
		match[cat] = len(compare & set(keys))/len(compare) * 1000

	ordered_match = []
	for cat in ['food', 'sports', 'finance', 'music', 'travel', 'tech', 'education', 'entertainment', 'fashion']:
		ordered_match.append(match[cat])

	return ordered_match

def getData():
	with open('sample_cache.txt', 'w+') as file:
		sample_data = file.read()
		with open('time_cache.txt', 'w+') as tfile:
			final = tfile.read()

		if not sample_data:
			sample = ['https://www.nytimes.com/2017/11/03/technology/silicon-valley-baltimore-schools.html', 'https://www.nytimes.com/2017/11/01/technology/personaltech/apple-iphone-x-review.html', 
			'https://www.livescience.com/60833-robot-cracks-captchas-in-minutes.html', 'http://www.slate.com/articles/technology/technology/2017/11/could_emphasizing_time_well_spent_fix_facebook_s_russia_problem.html',
			'https://en.wikipedia.org/wiki/Bangkok', 'https://en.wikipedia.org/wiki/Boston_Celtics', 'https://en.wikipedia.org/wiki/JetBlue',
			'https://en.wikipedia.org/wiki/Hawaii', 'https://well.blogs.nytimes.com/2010/02/18/how-vacations-affect-your-happiness/', 'https://www.wsj.com/articles/what-you-need-to-know-for-winter-holiday-travel-1509550592',
			'http://time.com/5006845/houston-astros-dodgers-world-series/', 'http://www.espn.com/nfl/story/_/id/21274790/nfl-owners-called-depositions-cellphone-records-colin-kaepernick-collusion-case',
			'http://www.latimes.com/sports/la-sp-dodgers-plaschke-20171104-story.html', 'https://www.tennismindgame.com/tennis-articles.html', 'https://www.nytimes.com/2017/08/25/opinion/sunday/the-honor-of-boxing-is-at-stake.html',
			'http://www.npr.org/sections/therecord/2017/11/03/561150174/tucker-beathard-is-more-than-country-musics-latest-punk', 'http://www.billboard.com/articles/news/dance/8023089/dj-snake-beats-by-dr-dre-paris-video',
			'http://www.billboard.com/articles/news/dance/8015098/kygo-new-song-every-day-kids-in-love', 'http://www.nytimes.com/2013/10/13/opinion/sunday/is-music-the-key-to-success.html', 
			'https://www.nytimes.com/2017/10/30/dining/five-food-stories-with-snacks.html', 'https://www.nytimes.com/2017/11/03/dining/thanksgiving-vegetable-recipes.html', 'https://www.nytimes.com/2017/10/30/dining/shake-shack-chili.html',
			'https://www.nytimes.com/2017/11/03/dining/what-to-cook-this-weekend-newsletter.html', 'http://time.com/4988118/thor-ragnarok-surtur/', 'http://time.com/5010243/kevin-spacey-house-of-cards/', 'http://www.cnn.com/2017/11/04/us/selena-quintanilla-star-hollywood-walk-of-fame/index.html',
			'https://hellogiggles.com/reviews-coverage/tv-shows/brandy-moesha-reboot/', 'https://www.nytimes.com/2017/11/03/education/edlife/choosing-a-college-major.html', 'https://www.nytimes.com/2017/10/31/opinion/adult-learners-college.html',
			'https://psmag.com/education/making-homework-matter-dont-ban-it-fix-it', 'https://www.theatlantic.com/education/archive/2017/11/the-surprising-revolt-at-reed/544682/', 'https://www.vogue.com/article/lagos-fashion-design-week-2017-hat-trend-lakin-ogun',
			'https://www.vogue.com/article/falana-lagos-fashion-design-week-2017', 'http://www.latimes.com/fashion/la-ig-fashion-forward-jenni-kayne-20171103-htmlstory.html', 'http://people.com/style/comfy-cozy-fall-sweaters/comfy-cozy-and-cute/'
			]
	
			sample_data = []
			final = {}

			for key in hosts:
				hits = hosts[key]['hits']
				newkey = key.replace("\\", ".")
				final[newkey] = {}
				final[newkey]["totalTime"] = 0
				final[newkey]["totalHits"] = hosts[key]['totalHits']
				for time in hits:
					final[newkey]["totalTime"] += hits[time]["timespent"]
					sample.append(("https://" + key + hits[time]["path"]).replace("\\", "."))

			i = 1
			for l in sample:
				print('importing {}/{}'.format(i, len(sample)))
				sample_data.append(transform(l))
				i += 1

			file.write(str(sample_data))
			tfile.write(str(final))
		else:
			final = eval(final)
			sample_data = eval(sample_data)

	return sample_data, final, 