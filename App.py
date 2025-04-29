from flask import Flask

App = Flask(__name__)

@App.route('/')
def home():
    return "Hello World from Flask"