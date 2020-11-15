import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
measurement = Base.classes.measurement
station=Base.classes.station

#Session Link
session = Session(engine)



# Flask Setup

app = Flask(__name__)



# Flask Routes

@app.route("/")
    def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to my Hawaii Weather API! Please see below for available API routes:<br/r>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"

@app.route("/api/v1.0/precipitation")
    def precipitation():
        