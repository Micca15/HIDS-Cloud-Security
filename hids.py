from flask_restful import Resource, reqparse
from models.computer import ComputerModel
from models.user import UserModel
from models.file import FileModel
from flask_restful import Resource


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
        uuid = data["uuid"]
        pc_id = data["computer"]

        # hier maak ik een log aan voor de analyser

        # return {"message": "A file with that name already exists"}

        # create user
        if UserModel.find_by_uuid(uuid) is None:
            UserModel(data.uuid).save_to_db()

        # create pc_name
        if ComputerModel.find_by_name(pc_id) is None:
            ComputerModel(data.computer).save_to_db()

        # add files to user/pc
        for file in data["files"]:
            file_path = file["path"]
            file_name = file["name"]
            file_hash = file["hash"]
            file_exists = FileModel.find_existing(file_path, file_name, uuid, pc_id)
            if file_exists:
                FileModel(file, uuid, pc_id).save_to_db()
            else:
                print(file_exists)

        return {"message": "file created successfully"}, 201


class ComputerList(Resource):
    def get(self):
        return {'stores': [store.json() for store in ComputerModel.query.all()]}


class FileList(Resource):
    def get(self):
        return {'items': [item.json() for item in FileModel.query.all()]}
