from flask_restful import Resource, reqparse
from models.computer import ComputerModel
from models.user import UserModel
from models.file import FileModel
from werkzeug.utils import secure_filename
from flask_restful import Resource
from settings import ALLOWED_EXTENSIONS
from flask import request, send_from_directory
import os


class Hids(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('uuid',
                        type=str,
                        required=False,
                        help="Every file- needs a guid!"
                        )
    parser.add_argument('computer',
                        type=str,
                        required=False,
                        help="Every file- needs a computer!"
                        )
    parser.add_argument('files',
                        type=list,
                        required=False,
                        location='json',
                        help="Every file- needs a file!"
                        )

    def post(self):
        data = Hids.parser.parse_args()

        # if FileModel.find_by_name(data['name']) and (data['hash']):
        # hier maak ik een log aan voor de analyser

        # return {"message": "A file with that name already exists"}
        print(data)
        # file.save_to_db()
        UserModel(data.uuid).save_to_db()
        ComputerModel(data.computer).save_to_db()
        for file in data["files"]:
            FileModel(file).save_to_db()
            print(file)

        return {"message": "file created successfully"}, 201


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


class ComputerList(Resource):
    def get(self):
        return {'stores': [store.json() for store in ComputerModel.query.all()]}


class FileList(Resource):
    def get(self):
        return {'items': [item.json() for item in FileModel.query.all()]}
