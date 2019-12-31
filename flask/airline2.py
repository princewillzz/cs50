#model2
from flask import Flask, render_template, request
from model.model2 import * 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:root@localhost:5432/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
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
    flight = Flight.query.get(flight_id)
    if flight == 0:
        return render_template("error.html", message="No such flights with the flight_id")
    # Add passenger
    flight.add_passenger(name=name)
    return render_template("success.html")

@app.route("/flights/")
def flights():
    #list all flights
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    #list details about a single flight

    #making sure that the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="The flight does not exists")
    
    #get all passengers
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight.html", flight=flight, passengers=passengers)
