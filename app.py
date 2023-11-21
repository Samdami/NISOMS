# app.py
from flask import Flask, render_template, request

# import requests

app = Flask(__name__)

# Replace with your own API key from https://openweathermap.org/api
# API_KEY = "269ee17023aaa4f9dbf0dd12f5ab9311"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)
