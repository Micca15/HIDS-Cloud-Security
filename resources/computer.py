from flask_restful import Resource
from models.computer import ComputerModel


class Computer(Resource):
    def get(self, name):
        store = ComputerModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Computer not found'}, 404

    def post(self, name):
        if ComputerModel.find_by_name(name):
            return {'message': 'A Computer with name {} is alreay there'.format(name)}, 400
        store = ComputerModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred'}, 500
        return store.json(), 201


class ComputerList(Resource):
    def get(self):
        return {'stores': [store.json() for store in ComputerModel.query.all()]}