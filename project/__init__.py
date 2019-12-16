import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy



# instantiate app
app = Flask(__name__)

api = Api(app)

# set configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate db
db = SQLAlchemy(app)

# models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

# route handlers       
class Ping(Resource):
    def get(self):
        return {
            'status': 'successs',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')