from db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    guid = db.Column(db.String(120), unique=False)

    def __init__(self, user):
        self.name = user["name"]
        self.guid = user["guid"]
