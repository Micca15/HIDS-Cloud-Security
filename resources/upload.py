from werkzeug.utils import secure_filename
from flask_restful import Resource
from settings import ALLOWED_EXTENSIONS
from flask import request, send_from_directory
import os


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Upload(Resource):


    def post(self):
        uploaded_file = request.files['File']

        if uploaded_file.filename != 'conf.cfg':
            print('Geen geldig config')
            return ("", 204)

        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join("conf", filename))
            print('nieuwe config geupload')
            return ("", 204)

    def get(self):
        return send_from_directory(os.path.join('conf'), 'conf.cfg', as_attachment=True)