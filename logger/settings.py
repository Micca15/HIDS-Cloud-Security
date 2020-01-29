from flask import Flask
import os
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# Init app
app = Flask(__name__)
db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

FILE_DELETION_TIMEOUT= 5000
ANALYZER_URL= '127.0.0.1:9000/upload'