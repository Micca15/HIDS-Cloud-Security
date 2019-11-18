from db import db


class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    guid = db.Column(db.String(120), unique=False)

    def __init__(self, computer):
        self.name = computer["name"]
        # self.guid = computer["guid"]
