# Set up dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up database
# Access SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)
# Save references to each table in variables
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link
session = Session(engine)

# Set up Flask
app = Flask(__name__)