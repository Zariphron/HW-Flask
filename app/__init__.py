import flask
import os
from flask_sqlalchemy import SQLAlchemy

myapp_obj = flask.Flask(__name__)
myapp_obj.config.from_mapping(
        SECRET_KEY = 'it-dont-matter'
        )

db = SQLAlchemy(myapp_obj)

from app import routes, models
