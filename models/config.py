from settings import db


class ConfigModel(db.Model):
    __tablename__ = 'config'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(255))
    computer_name = db.Column(db.String(255))
    interval = db.Column(db.Integer)
    path = db.Column(db.String(255))
    whitelist = db.Column(db.String(255))
    logger_url = db.Column(db.String(255))

    def __init__(self, uuid, computer_name, interval, path, whitelist, logger_url):
        self.uuid = uuid
        self.computer_name = computer_name
        self.interval = interval
        self.path = path
        self.whitelist = whitelist
        self.logger_url = logger_url


    def json(self):
        return {
            'uuid': self.uuid,
            'computer_name': self.computer_name,
            'interval': self.interval,
            'path': self.path,
            'whitelist': self.whitelist,
            'logger_url': self.logger_url,
        }


    @classmethod
    def find_by_uuid(cls,uuid):
        return cls.query.filter_by(uuid=uuid).first()

    # Insert or Update from db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

