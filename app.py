from flask_restful import Resource, reqparse
from flask import request, send_from_directory
from werkzeug.utils import secure_filename
from settings import *
from resources.user import UserRegister
from resources.file import File, FileList
from resources.computer import Computer, ComputerList

# create db with the tables in models
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(File, '/file')
api.add_resource(FileList, '/files')
api.add_resource(UserRegister, '/register')
api.add_resource(Computer, '/computer/<string:name>')
api.add_resource(ComputerList, '/computers')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=["GET", 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['File']

        if uploaded_file.filename != 'conf.cfg':
            print('Geen geldig config')
            return ("", 204)

        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join("conf", filename))
            print('nieuwe config geupload')
            return ("", 204)

    if request.method == 'GET':
        return send_from_directory(os.path.join('conf'), 'conf.cfg', as_attachment=True)


# Run Server
if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=9000, debug=True)
