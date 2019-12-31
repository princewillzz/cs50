import os, csv

from flask import Flask, render_template, request
from model.models import * # importing everything from the models.py

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenvs("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost:5432/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # binding our database with the Flask app


def main():
    f = open("files/flights.csv")
    r = csv.reader(f)
    for origin, destination, duration in r:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes")
    db.session.commit()
    
if __name__ == '__main__':
    with app.app_context(): # Flask way to deal with in cmd line
        main()