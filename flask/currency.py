import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("currency.html")

@app.route("/convert", methods=["POST"])
def convert():

    # query for currency exchange rate
    currency = request.form.get("currency")
    res = requests.get(f"http://data.fixer.io/latest?access_key=b1d838edcf954525e53384e43f3b10b0")

    # Make suure request succeeded
    if res.status_code != 200:
        return jsonify({"success": false})
    data = res.json()
    return jsonify({"success": True, "rate": data['rates'][currency.upper()]})