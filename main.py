from flask import Flask

#practice - Hello world program at web server home directory
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world!"

if __name__ == "__main__":
	app.run()