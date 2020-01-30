import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgres://postgres:root@localhost:5432/cs50")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("book_db.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a Flight."""

    #Get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")
    #make sure the fligh exists
    if db.execute("SELECT * FROM flights WHERE id =:id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flights with the flight_id")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")

@app.route("/flights/")
def flights():
    #list all flights
    flights = db.execute("SELECT * FROM flights").fetchall()
    if flights is None:
        return render_template("error.html", message="Flight is empty")
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    #list details about a single flight

    #making sure that the flight exists
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="The flight does not exists")
    
    #get all passengers
    passengers = db.execute("SELECT * FROM passengers WHERE flight_id = :flight_id", {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)
