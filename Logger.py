from flask import Flask, jsonify, request, Response
import json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
print(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

hids_entities = [
    {
        'name' : 'Danesh',
        'hash' : 12311111111,
        'date_modified' : '19.01.1931'
    },
    {
        'name': 'Thomas',
        'hash': 12311231611,
        'date_modified': '15.04.1918'
    }
]

def valid_hids_entity(hids_entity):
    if (
        "name" in hids_entity and
        "hash" in hids_entity and
        "date_modified" in hids_entity):
        return True
    else:
        return False

#GET /hids
@app.route('/hids')
def get_all_hids_entities():
    return jsonify({'hids' : hids_entities})

#GET /hids/<hash_file>
@app.route('/hids/<int:hash_file>')
def get_hids_entity(hash_file):
    return_value = {}
    for hids_entity in hids_entities:
        if hids_entity['hash'] == hash_file:
            return_value = {
                'name': hids_entity['name'],
                'hash': hids_entity['hash'],
                'date_modified': hids_entity['date_modified']
            }
    return jsonify(return_value)

#POST /hids
@app.route('/hids', methods = ['POST'])
def add_hids_entity():
    request_data = request.get_json()
    if(valid_hids_entity(request_data)):
        new_hids_entity = {
            'name': request_data['name'],
            'hash': request_data['hash'],
            'date_modified': request_data['date_modified']
        }
        hids_entities.insert(0, new_hids_entity)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/hids/" + str(new_hids_entity['hash'])
        return response
    else:
        invalid_hids_object_error_message = {
            "error" : "Invalid hids object passed in request",
        }
        response = Response(json.dumps(invalid_hids_object_error_message), 400, mimetype='application/json')
        return (response)

#PUT /hids/<hash>
@app.route('/hids/<int:hash_file>', methods = ['PUT'])
def replace_hids_entity(hash_file):
    request_data = request.get_json()
    new_hids_entity = {
        'name': request_data['name'],
        'hash': hash_file,
        'date_modified': request_data['date_modified']
    }
    i = 0
    for hids_entity in hids_entities:
        current_hash = hids_entity["hash"]
        if current_hash == hash_file:
            hids_entities[i] = new_hids_entity
        i += 1
    response = Response("", 204)


if __name__ == "__main__":
    app.run(port=5000)

