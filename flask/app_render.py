from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/")

#def index():
#   return render_template("index.html")
def index():
    headline = "hello, world!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "goodbye!"
    return render_template("index.html", headline=headline)





