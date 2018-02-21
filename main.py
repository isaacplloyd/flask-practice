from flask import Flask
import poloniex

polo = poloniex.Poloniex()

#practice - Hello world program at web server home directory
app = Flask(__name__)
@app.route('/')
def hello():
	response = "<h3>Hello world!</h3><br><br>"
	response += "<a href=\"/get-ltc\">Get LTC price</a><br>"
	response += "<a href=\"/get-prices\">Get prices</a><br>"
	return response

@app.route('/get-ltc')
def get_ltc():
	price = polo('returnTicker')['USDT_LTC']['last']
	display = "<h2>LTC price: $" + price + "</h2>"
	display += "<br> <a href=\"/\">home</a>"
	display += "<br> <a href=\"/get-ltc\">Refresh...</a>"
	return display

@app.route('/get-prices')
def get_prices():
	tickers = polo('returnTicker')
	price_btc = tickers['USDT_BTC']['last']
	price_ltc = tickers['USDT_LTC']['last']
	price_xrp = tickers['USDT_XRP']['last']
	display = "<h2>LTC price: $" + price_ltc + "</h2><br>"
	display += "<h2>BTC price: $" + price_btc + "</h2><br>"
	display += "<h2>XRP price: $" + price_xrp + "</h2><br>"
	display += "<br> <a href=\"/\">home</a>"
	display += "<br> <a href=\"/get-prices\">Refresh...</a>"
	return display

if __name__ == "__main__":
	app.run(host='127.0.0.1')