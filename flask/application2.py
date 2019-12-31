from flask import Flask, render_template
import datetime

app = Flask(__name__) 

@app.route("/")
def index():
    now = datetime.datetime.now()
    merry_christmas = now.month ==12 and now.day == 25
    return render_template("index2.html", merry_christmas=merry_christmas)
