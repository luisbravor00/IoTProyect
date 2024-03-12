from flask import Blueprint, jsonify, request
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor
import controllers.utilities as ut

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
    query = "SELECT * FROM Doctors"
    cursor.execute(query)
    result = cursor.fetchall()

    doctors_list = ut.get_dictionary_from_query(result, cursor)

    return jsonify(doctors_list), HTTP_OK
