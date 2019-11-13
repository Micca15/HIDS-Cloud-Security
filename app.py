from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import pprint
"""
{
    "user" : {"name" : "Thomas", "guid" : "1337x"},
    "computer" : {"name" : "DESKTOP-1337"},
    "file" : {"name" : "virus.exe", "path":"/roet", "hash" : "hhhh"  }
}
"""
# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


# endpoint to create new user
@app.route("/hids", methods=["POST"])
def add_user():
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(request.__dict__)
    user = request.json['user']
    computer = request.json['computer']
    file = request.json['file']

    new_user = User(user)
    new_computer = Computer(computer)
    new_file = File(file)
    db.session.add(new_user)
    db.session.add(new_computer)
    db.session.add(new_file)
    db.session.commit()
    return("ok")
    # return jsonify({"user": new_user, "computer": new_computer, "file": new_file})



# Run Server
if __name__ == '__main__':
    app.run(debug=True)

