from flask_restful import Resource, reqparse
from logger.models.config import ConfigModel


class Config(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
                        type=str,
                        required=True,
                        help="Every config needs a uuid!"
                        )
    parser.add_argument('computer_name',
                        type=str,
                        required=False,
                        help="Every config needs a computer_name!"
                        )
    parser.add_argument('interval',
                        type=int,
                        required=False,
                        help="Every config needs a interval!"
                        )
    parser.add_argument('path',
                        type=str,
                        required=False,
                        help="Every config needs a path!"
                        )
    parser.add_argument('whitelist',
                        type=str,
                        required=False,
                        location='json',
                        help="Every config needs a whitelist!"
                        )
    parser.add_argument('logger_url',
                        type=str,
                        required=False,
                        help="Every config needs a logger_url!"
                        )

    def get(self, uuid):
        item = ConfigModel.find_by_uuid(uuid)
        if item:
            return item.json()
        return {'message': 'config not found'}, 404

    def put(self, uuid):
        data = Config.parser.parse_args()
        item = ConfigModel.find_by_uuid(uuid)
        if item is None:
            item = ConfigModel(**data)
        else:
            item.computer_name = data['computer_name']
            item.interval = data['interval']
            item.path = data['path']
            item.whitelist = data['whitelist']
            item.logger_url = data['logger_url']
        item.save_to_db()
        return item.json(), 201
