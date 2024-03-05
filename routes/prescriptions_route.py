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

## GET All Prescriptions
@prescriptions_blueprint.route('/data')
def prescriptions_get_all():
    prescriptions_cursor = db['prescriptions'].find({})  # Obtener todas las prescripciones
    prescriptions_list = list(prescriptions_cursor)  # Convertir el cursor a lista

    # Convertir los ObjectId a string para la serialización JSON
    for prescription in prescriptions_list:
        prescription["_id"] = str(prescription["_id"])

    return jsonify(prescriptions_list), 200  # HTTP_OK se asume que es 200
