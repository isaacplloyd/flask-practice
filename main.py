from flask import Flask
import poloniex

polo = poloniex.Poloniex()

#practice - Hello world program at web server home directory
app = Flask(__name__)
@app.route('/')
def hello():
	with open("index.html") as file:
		response = file.read()
	return response

@app.route('/get-ltc')
def get_ltc():
	price = polo('returnTicker')['USDT_LTC']['last']
	display = "<h2>LTC price: $" + price + "</h2>"
	display += "<br> <a href=\"/get-ltc\">Refresh...</a>"
	return display

if __name__ == "__main__":
	app.run(host='127.0.0.1')