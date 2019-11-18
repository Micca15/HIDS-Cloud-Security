from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# Init ma
ma = Marshmallow()

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user', 'computer', 'file')


user_schema = UserSchema()
users_schema = UserSchema(many=True)