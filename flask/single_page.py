from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #return render_template("single_page.html")
    return render_template("single_page1.html")
texts = ["Lorem epsum and Iwas thinking that bullbull is a ",
    "that is going to let me do whatever i like. She once also told me that I am that one and ",
        "only that she loves and is going to love for the rest of my life"]
@app.route("/first")
def first():
    return texts[0]

@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]