from flask import Blueprint, jsonify, request
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor
import controllers.utilities as ut

prescriptions_blueprint = Blueprint('prescriptions', __name__)

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
    query = "SELECT * FROM Prescription"
    cursor.execute(query)
    result = cursor.fetchall()

    prescriptions_list = ut.get_dictionary_from_query(result, cursor)

    return jsonify(prescriptions_list), HTTP_OK
