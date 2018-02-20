from flask import Flask
import os

#practice - Hello world program at web server home directory
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world!"

app.run()