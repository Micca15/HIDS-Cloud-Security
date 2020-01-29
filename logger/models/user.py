from settings import db


class UserModel(db.Model):
    __tablename__ = 'user'

    name = db.Column(db.String(80))
    uuid = db.Column(db.String(80), primary_key=True)

    def __init__(self, uuid: str):
        self.uuid = uuid

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first()