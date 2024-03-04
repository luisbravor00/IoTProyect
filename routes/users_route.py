from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from config.config import *

users_blueprint = Blueprint('users', __name__)

# MongoDB

mongoConnection = f'mongodb+srv://{username}:{password}@test.mygbwdt.mongodb.net/'
client = MongoClient(mongoConnection)

db = client['IoT']
users_collection = db['users']

# Routes

## GET Ruta Base
@users_blueprint.route('/')
def users_home():
    return 'Página de users', HTTP_OK

## GET Ruta Base
@users_blueprint.route('/details')
def users_detail():
    return 'Detalle de users', HTTP_OK
