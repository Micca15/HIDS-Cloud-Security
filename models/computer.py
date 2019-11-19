from settings import db


class ComputerModel(db.Model):
    __tablename__ = 'computer'

    id = db.Column(db.Integer, primary_key=True)
    computer = db.Column(db.String(80))

    def __init__(self, computer):
        self.computer = computer

    def json(self):
        return {'id': self.id, 'computer': self.computer, 'items': [x.json() for x in self.items.all()]}

    @classmethod
    def find_by_name(cls, computer):
        return cls.query.filter_by(computer=computer).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()