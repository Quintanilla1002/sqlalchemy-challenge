import numpy as np
import datetime as dt
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
        f"Welcome to my Hawaii Weather API! Please see below for available API paths:<br/r>"
        f"/api/v1.0/precipitation<br/r>"
        f"/api/v1.0/stations<br/r>"
        f"/api/v1.0/tobs<br/r>"
        f"/api/v1.0/start<start_date><br/r>"
        f"/api/v1.0/start<start_date>/end<end_date>/<end>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    latestdate=session.query(measurement.date).order_by(measurement.date.desc()).first().date
    latestyear=dt.date(2017, 8, 23)-dt.timedelta(days=365)
    precip_year= session.query(measurement.date, measurement.prcp).\
    filter(measurement.date>=latestyear).\
    filter(measurement.date<=latestdate).\
    order_by(measurement.date).all()
    precip_dict=[]
    for date in precip_year:
        row={}
        row["date"]=precip_year[0]
        row["prcp"]=precip_year[1]
        precip_dict.append(row)
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    station_name=session.query(station.station, station.name).all()
    station_list=list(np.ravel(station_name))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'Tobs' page...")
    latestdate=session.query(measurement.date).order_by(measurement.date.desc()).first().date
    latestyear=dt.date(2017, 8, 23)-dt.timedelta(days=365)
    tobs_year= session.query(measurement.date, measurement.tobs).\
    filter(measurement.date>=latestyear).\
    filter(measurement.date<=latestdate).\
    filter(measurement.station == 'USC00519281')
    tobs_dict=[]
    for row in tobs_year:
        row={}
        row["date"]=tobs_year[0]
        row["tobs"]=tobs_year[1]
        tobs_dict.append(row)
    return jsonify (tobs_dict)
if __name__ == "__main__":
      app.run(debug=True)