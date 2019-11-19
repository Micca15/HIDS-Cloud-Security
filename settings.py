from flask import Flask
import os
from flask_restful import Api
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mikey'
api = Api(app)

# Allowed extensions for the config file
ALLOWED_EXTENSIONS = {'cfg'}