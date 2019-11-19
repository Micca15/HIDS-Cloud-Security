from settings import db


class FileModel(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String(80))
    path = db.Column(db.String(255))
    hash = db.Column(db.String(255))

    def __init__(self, files):
        self.path = files["path"]
        self.file = files["file"]
        self.hash = files["hash"]

    def json(self):
        return {'id': self.id, 'file': self.file, 'path': self.path, 'hash': self.hash}

    @classmethod
    def find_by_name(cls, file):
        return cls.query.filter_by(file=file).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
