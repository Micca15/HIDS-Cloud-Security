from settings import *
from hids import Hids, Upload, ComputerList, FileList

# create db with the tables in models
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Hids, '/hids')
api.add_resource(FileList, '/files')
api.add_resource(ComputerList, '/computers')
api.add_resource(Upload, '/upload')


# Run Server
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=9000, debug=True)
