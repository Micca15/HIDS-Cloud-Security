import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    parser.add_argument('guid',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_name(data['name']):
            return {"message": "A user with that name already exists"}

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
