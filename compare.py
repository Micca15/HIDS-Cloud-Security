import sqlite3
from flask_restful import Resource, reqparse
from models.file import UserModel


class FileRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('path',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    parser.add_argument('hash',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )

    def post(self):
        data = FileRegister.parser.parse_args()

        if UserModel.find_by_name(data['hash']):
            return {"message": "This file already exists"}

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
