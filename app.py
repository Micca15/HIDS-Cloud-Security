from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Hids Class/Model
class Hids(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  file = db.Column(db.String(200))
  hash = db.Column(db.String(200))

  def __init__(self, name, file, hash):
    self.name = name
    self.file = file
    self.hash = hash

# Hids Schema
class HidsSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'file', 'hash')

# Init schema
hids_schema = HidsSchema
hidss_schema = HidsSchema

# Create a Hids
@app.route('/hids', methods=['POST'])
def add_hids():
  name = request.json['name']
  file = request.json['file']
  hash = request.json['hash']
  qty = request.json['qty']

  new_hids = Hids(name, file, hash)

  db.session.add(new_hids)
  db.session.commit()

  return hids_schema.jsonify(new_hids)

# Get All Hids
@app.route('/hids', methods=['GET'])
def get_hidss():
  all_hidss = Hids.query.all()
  result = hidss_schema.dump(all_hidss)
  return jsonify(result.data)

# Get Single Hids
@app.route('/hids/<id>', methods=['GET'])
def get_hids(id):
  hids = Hids.query.get(id)
  return hids_schema.jsonify(hids)

# Update a hids
@app.route('/hids/<id>', methods=['PUT'])
def update_hids(id):
  hids = Hids.query.get(id)

  name = request.json['name']
  file = request.json['file']
  hash = request.json['hash']

  hids.name = name
  hids.file = file
  hids.hash = hash

  db.session.commit()

  return hids_schema.jsonify(hids)

# Delete Hids
@app.route('/hids/<id>', methods=['DELETE'])
def delete_hids(id):
  hids = Hids.query.get(id)
  db.session.delete(hids)
  db.session.commit()

  return hids_schema.jsonify(hids)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)