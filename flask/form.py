from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index5.html")

@app.route("/hello", methods=["POST", "GET"])
def hello():
    if request.method == "GET":
        return "<h1>Please submit the form instead </h1>"
    else:
        name = request.form.get("name")
        return render_template("hello_form.html", name=name)


