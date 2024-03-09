from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor

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
    return "OK", HTTP_OK 
