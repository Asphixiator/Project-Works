import requests
import json 
from datetime import datetime

def placeName():

	while True:
		try:
			name = input("Enter a city/country name: ")
		except:
			print("Please enter a valid name!")
		else:
			return name 

def geoCoder():
	
	place = placeName()

	url = "https://api.opencagedata.com/geocode/v1/json?q="
	key = "&key=24639a9e0dd94739a54d8a95df714553"

	final_url = url + place.lower() + key

	location_data = requests.get(final_url)
	geometry = location_data.json()['results'][1]['geometry']

	return geometry

def jprint(obj):

	text = json.dumps(obj, sort_keys = True, indent = 4)
	print(text)



geometry = geoCoder()
geometry['lon'] = geometry.pop('lng')

passover = requests.get("http://api.open-notify.org/iss-pass.json", params = geometry)

pass_times = passover.json()['response']
jprint(pass_times)

risetimes = []

for i in pass_times:
	time = i['risetime']
	risetimes.append(time)

print(risetimes)

times = []

for each in risetimes:
	time = datetime.fromtimestamp(each)
	times.append(time)
	print(time)

# inspace = requests.get("http://api.open-notify.org/astros.json", params = geometry)
# jprint(passover.json())
# jprint(inspace.json())