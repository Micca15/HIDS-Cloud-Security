from settings import db


class FileModel(db.Model):
    __tablename__ = 'file'

    id = db.Column(db.Integer, primary_key=True)
    pc_id = db.Column(db.Integer, db.ForeignKey('computer.id'))
    name = db.Column(db.String(80))
    path = db.Column(db.String(255))
    curr_hash = db.Column(db.String(255))
    prev_hash = db.Column(db.String(255))
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp())

    pc = db.relationship('ComputerModel')

    def __init__(self, file, pc_id):
        self.path = file["path"]
        self.name = file["name"]
        self.curr_hash = file["hash"]
        self.pc_id = pc_id

    def json(self):
        return {'pc_name': self.pc.name, 'name': self.name, 'path': self.path, 'curr_hash': self.curr_hash, 'prev_hash': self.prev_hash, 'last_updated': self.last_updated.strftime('%Y,%m,%d,%H:%M:%S')}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_changes_by_pc_id(cls, pc_id):
        return cls.query.filter_by(pc_id=pc_id).filter(cls.curr_hash != cls.prev_hash).all()

    @classmethod
    def find_existing(cls, path, name, pc_id):
        return cls.query.filter_by(path=path, name=name, pc_id=pc_id).first()

    @classmethod
    def find_and_replace(cls, file_id, new_hash):
        file = cls.query.get(file_id)
        file.prev_hash=file.curr_hash
        file.curr_hash=new_hash
        db.session.commit()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
