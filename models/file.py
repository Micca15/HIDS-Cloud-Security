from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint

from settings import db


class FileModel(db.Model):
    __tablename__ = 'file'

    name = db.Column(db.String(80))
    path = db.Column(db.String(255))
    hash = db.Column(db.String(255))
    uuid = db.Column(db.String(255), db.ForeignKey('user.uuid'))
    pc_id = db.Column(db.String(255), db.ForeignKey('computer.computer'))

    __table_args__ = (
        PrimaryKeyConstraint('path', 'name', 'uuid', 'pc_id'),
        {},
    )

    def __init__(self, file, uuid, pc_id):
        self.path = file["path"]
        self.name = file["name"]
        self.hash = file["hash"]
        self.uuid = uuid
        self.pc_id = pc_id

    def json(self):
        return {'uuid': self.uuid, 'pc_id': self.pc_id, 'file': self.file, 'path': self.path, 'hash': self.hash}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_existing(cls, path, name, uuid, pc_id):
        if cls.query.filter_by(path=path, name=name, uuid=uuid, pc_id=pc_id).first():
            return False
        else:
            return True

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()