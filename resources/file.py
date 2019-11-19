from flask_restful import Resource, reqparse
from models.file import FileModel


class File(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('path',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('hash',
                        type=str,
                        required=False,
                        help="Every file- needs a store id!"
                        )

    def post(self):
        data = File.parser.parse_args()

        if FileModel.find_by_name(data['name']):
            return {"message": "A file with that name already exists"}

        user = FileModel(**data)
        user.save_to_db()

        return {"message": "file created successfully"}, 201


class FileList(Resource):
    def get(self):
        return {'items': [item.json() for item in FileModel.query.all()]}
