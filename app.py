from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os

app = Flask(__name__, template_folder="templates")
# Flask Routes
@app.route("/")
def index():
    return send_from_directory("", "index.html")


@app.route("/landing")
def landing():
    return render_template("landing.html")


@app.route("/cloudiness")
def cloudiness():
    return render_template("cloudiness.html")

@app.route("/humidity")
def humidity():
    return render_template("humidity.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

@app.route("/wind")
def wind():
    return render_template("wind.html")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/data")
def data():
	data = pd.read_csv("static/cities.csv")
	df = data.rename(columns={"id": "City Id",
                "name":"City",
                "clouds.all": "Cloudiness",
                "sys.country": "Country",
                "dt": "Date",
                "main.humidity": "Humidity",
                "coord.lat": "Lat",
                "coord.lon": "Lng",
                "main.temp": "Max Temp",
                "wind.speed": "Wind Speed"})
	df = df.sort_values(by=['City Id'])
	
	return render_template("data.html", column_names=df.columns.values, data=list(df.values.tolist()))


if __name__ == "__main__":
    app.run(debug=True)
