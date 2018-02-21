from flask import Flask
import poloniex

polo = poloniex.Poloniex()

#practice - Hello world program at web server home directory
app = Flask(__name__)
@app.route('/')
def hello():
	return "Hello world!"

@app.route('/get-ltc')
def get_ltc():
	price = polo('returnTicker')['USDT_LTC']['last']
	display = "<h2>LTC price: $" + price + "</h2>"
	return display

if __name__ == "__main__":
	app.run(host='127.0.0.1')