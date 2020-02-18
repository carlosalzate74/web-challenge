from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder="templates")
# Flask Routes
@app.route("/")
def index():
    return send_from_directory('','index.html')

@app.route("/landing")
def landing():
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(debug=True)