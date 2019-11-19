from flask_restful import Resource, reqparse, request
from models.computer import ComputerModel
from models.user import UserModel
from models.file import FileModel


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
                        type=dict,
                        required=False,
                        help="Every file- needs a file!"
                        )
    def post(self):
        data = Hids.parser.parse_args()

        # if FileModel.find_by_name(data['name']) and (data['hash']):
        # hier maak ik een log aan voor de analyser

        # return {"message": "A file with that name already exists"}


        # file.save_to_db()
        UserModel(data.uuid).save_to_db()
        ComputerModel(data.computer).save_to_db()
        FileModel(data.files).save_to_db()

        return {"message": "file created successfully"}, 201


class FileList(Resource):
    def get(self):
        return {'items': [item.json() for item in FileModel.query.all()]}
