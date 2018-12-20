import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2970c1a6756bba7908f811f806b6f7a7'
	if request.method == 'POST':
		city = request.form.get('city')
	else: 
		city = 'New Delhi'
		
	r = requests.get(url.format(city)).json()

	weather = {
		'city': r['name'],
		'temperature' : r['main']['temp'],
		'description' : r['weather'][0]['description'], 
		'wind_speed' : r['wind']['speed'],
	}
	
	return render_template('weather.html', weather=weather)

if __name__ == '__main__':
	app.run(debug=True)