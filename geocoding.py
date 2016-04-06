import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__) 

my_key = "AqbfQgdDj0oHogXKLAAG1dTzQzsTzNGH"



@app.route('/')
def index():
    '''Shows index page at localhost:5000'''
    return render_template('index.html')

@app.route("/AQI_Analysis")
def aqi_analysis():
	targetcity = request.args.get('target_city')
	print targetcity
	my_key = "AqbfQgdDj0oHogXKLAAG1dTzQzsTzNGH"

	base_url = "http://www.mapquestapi.com/geocoding/v1/address"
	#URL = base_url + "?" + "key=" + my_key + "&" + "country=" + country + "&" + "city=" + city
	URL = base_url + "?" + "key=" + my_key + "&" + "city=" + targetcity
	r = requests.get(URL)
	data = json.loads(r.text)
	lat =  data['results'][0]['locations'][0]['displayLatLng']['lat']
	lon =  data['results'][0]['locations'][0]['displayLatLng']['lng']

	#air quality part
	my_key_aqi = "0bcb46fd56ff4a069c8327279f31ae13"
	base_url_2 = "http://api.breezometer.com/baqi/"
	URL = base_url_2 + "?" + "lat=" + str(lat) + "&" + "lon=" + str(lon) + "&" + "key=" + my_key_aqi
	r= requests.get(URL)
	data = json.loads(r.text)
	#print type(json.loads(r))
	aqi_value = data['breezometer_aqi']
	print aqi_value
	return json.dumps({'lat':lat,'lon':lon,'aqi':aqi_value})

if __name__ == '__main__':
    app.run(debug=True)
