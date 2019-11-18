from db import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80), unique=False)
    name = db.Column(db.String(120), unique=False)
    hash = db.Column(db.String(300), unique=False)

    def __init__(self, file):
        self.path = file["path"]
        self.name = file["name"]
        self.hash = file["hash"]