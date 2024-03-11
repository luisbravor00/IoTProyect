from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor

doctors_blueprint = Blueprint('doctors', __name__)

# Routes

## GET Ruta Base
@doctors_blueprint.route('/')
def doctors_home():
    return 'Página de doctors', HTTP_OK

## GET Ruta Base
@doctors_blueprint.route('/details')
def doctors_detail():
    return 'Detalle de doctors', HTTP_OK

## GET All doctors
@doctors_blueprint.route('/data')
def doctors_get_all():

    query = "SELECT * FROM doctors"
    cursor.execute(query)
    result = cursor.fetchall()

    doctorInfo = []
    columns = ['certId', 'name', 'last_name', 'phoneNumber', 'OfficeAddress']

    for row in result:
        doctor_dict = {columns[i]: row[i] for i in range(len(columns))}
        doctorInfo.append(doctor_dict)

    return jsonify(doctorInfo), HTTP_OK
