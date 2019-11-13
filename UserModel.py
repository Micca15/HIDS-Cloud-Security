from settings import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    guid = db.Column(db.String(120), unique=False)

    def __init__(self, user):
        self.name = user["name"]
        self.guid = user["guid"]


class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    guid = db.Column(db.String(120), unique=False)

    def __init__(self, computer):
        self.name = computer["name"]
        # self.guid = computer["guid"]


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80), unique=False)
    name = db.Column(db.String(120), unique=False)
    hash = db.Column(db.String(300), unique=False)

    def __init__(self, file):
        self.path = file["path"]
        self.name = file["name"]
        self.hash = file["hash"]


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user', 'computer', 'file')


user_schema = UserSchema()
users_schema = UserSchema(many=True)