from logger.settings import db


class ComputerModel(db.Model):
    __tablename__ = 'computer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    user_uid = db.Column(db.String(255), db.ForeignKey('user.uuid'))

    user = db.relationship('UserModel')

    def __init__(self, name, uuid):
        self.name = name
        self.user_uid = uuid

    def json(self):
        return {'id': self.id, 'name': self.name, 'user_uid': self.user_uid }

    @classmethod
    def find_by_name(cls, name, uuid):
        return cls.query.filter_by(name=name, user_uid=uuid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()