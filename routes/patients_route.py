from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor

patients_blueprint = Blueprint('patients', __name__)

# Routes

## GET Ruta Base
@patients_blueprint.route('/')
def patients_home():
    return 'Página de patients', HTTP_OK

## GET Ruta Base
@patients_blueprint.route('/details')
def patients_detail():
    return 'Detalle de patients', HTTP_OK

## GET All patients
@patients_blueprint.route('/data')
def patients_get_all():
    query = "SELECT * FROM Patients"
    cursor.execute(query)
    result = cursor.fetchall()

    patients_list = []
    columns = ['ID_Patient', 'Name', 'Last_name', 'Address', 'Age', 'Phone', 'Email']

    for row in result:
        patient_dict = {columns[i]: row[i] for i in range(len(columns))}
        patients_list.append(patient_dict)

    return jsonify(patients_list), HTTP_OK
