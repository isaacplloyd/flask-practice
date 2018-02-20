from flask import Flask
import os

#practice - Hello world program at web server home directory
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world!"

#practice - Print all environment variables to help understand them
def print_environ():
    for param in os.environ.keys():
        print("%20s %s" % (param,os.environ[param]))



if __name__ == "__main__":
    app.run()
    #print_environ()