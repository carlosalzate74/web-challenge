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
	

	# females = data.loc[data.Gender=='F']
	# return render_template('data.html', target=data)
	print(df[:2])
	return render_template("data.html", column_names=df.columns.values, data=list(df.values.tolist()))
	# return render_template('data.html',  table=[df], titles=df.columns.values)
	# return render_template("data.html", table=[df[:2].to_html(classes='data')])
	# return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True)
