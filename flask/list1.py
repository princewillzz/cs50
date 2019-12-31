import os, csv

from flask import Flask, render_template, request
from model.models import * # importing everything from the models.py

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenvs("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost:5432/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # binding our database with the Flask app


def main():
    #Flight.query.filter_aby(id=23) = Flight.query.get(23)
    flights = Flight.query.filter_by(origin="New York").first()/.count()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, in {flight.duration} minutes")
    #print(flights.origin)
    
if __name__ == '__main__':
    with app.app_context(): # Flask way to deal with in cmd line
        main()