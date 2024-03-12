from flask import Blueprint, jsonify, request
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor
import controllers.utilities as ut

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

    patients_list = ut.get_dictionary_from_query(result, cursor)

    return jsonify(patients_list), HTTP_OK
