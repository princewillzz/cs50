''' For windows:-
1. set FLASK_APP=application.py ----> for registering flask app to the flask server
2. set FLASK_ENV=development ----> for switching on debug mode
'''


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world!"

@app.route("/harsh")
def harsh():
    return "hello, harsh!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1> hello, {name}!</h1>"