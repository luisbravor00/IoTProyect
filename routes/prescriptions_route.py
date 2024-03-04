from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from config.config import *

prescriptions_blueprint = Blueprint('prescriptions', __name__)

# MongoDB

mongoConnection = f'mongodb+srv://{username}:{password}@test.mygbwdt.mongodb.net/'
client = MongoClient(mongoConnection)

db = client['IoT']
users_collection = db['prescriptions']

# Routes

## GET Ruta Base
@prescriptions_blueprint.route('/')
def prescriptions_home():
    return 'Página de prescriptions', HTTP_OK

## GET Ruta Base
@prescriptions_blueprint.route('/details')
def prescriptions_detail():
    return 'Detalle de prescriptions', HTTP_OK
