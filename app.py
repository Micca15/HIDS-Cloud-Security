from settings import *
from resources.user import UserRegister
from resources.file import File, FileList
from resources.computer import Computer, ComputerList
from resources.upload import Upload
from resources.hids import Hids

# create db with the tables in models
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(File, '/file')
api.add_resource(FileList, '/files')
api.add_resource(UserRegister, '/register')
api.add_resource(Computer, '/computer/<string:name>')
api.add_resource(ComputerList, '/computers')
api.add_resource(Upload, '/upload')
api.add_resource(Hids, '/hids')


# Run Server
if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=9000, debug=True)
