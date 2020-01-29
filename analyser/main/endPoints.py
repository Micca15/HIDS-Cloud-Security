import os
from flask import Flask, flash, request, redirect, send_file
from werkzeug.utils import secure_filename
from flask_restful import Resource

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = ['txt', 'log'] # TODO: make central place for config
CLIENTS = {'client1': 'conf1.ini',
           'client2': 'blacklist.ini'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Upload(Resource):
    def __init__(self):
        self.filename = Resource

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return {'message': request.url}, 302
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and self.allowed_file(str(file.filename)):
            filename = 'clientLog.json'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return {'message': 'uploaded_file'}, 302


class GetConfig(Resource):
    def __init__(self):
        self.client = Resource

    @staticmethod
    def get(client):
        if client not in CLIENTS:
            return 404
        else:
            filename = 'config\\' + CLIENTS[client]
            return send_file(filename, mimetype='text/plain')
