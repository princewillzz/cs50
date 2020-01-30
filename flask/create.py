import os

from flask import Flask, render_template, request
from model.model3 import * # importing everything from the models.py

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenvs("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost:5432/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # binding our database with the Flask app

# Creates all the tables that has been defined
def main():
    db.create_all() 
    
if __name__ == '__main__':
    with app.app_context(): # Flask way to deal with in cmd line
        main()

