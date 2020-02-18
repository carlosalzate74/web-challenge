from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Flask Routes
@app.route("/")
def landing():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)