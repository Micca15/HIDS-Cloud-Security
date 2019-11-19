from db import db


class FileModel(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    path = db.Column(db.String(255))
    hash = db.Column(db.String(255))


    def __init__(self, name, path, hash):
        self.name = name
        self.path = path
        self.hash = hash

    def json(self):
        return {'id': self.id, 'name': self.name, 'path': self.path, 'hash': self.hash}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()