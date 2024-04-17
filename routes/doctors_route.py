from flask import Blueprint, jsonify, request, render_template, request, redirect, flash
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

## GET Doctor By ID
@doctors_blueprint.route('/doctor')
def doctors_get_doctor_by_id():
    id_doctor = request.args.get('id_doctor', type=int)

    if not id_doctor:
        return jsonify({"error": "ID_DOCTOR is required."}), HTTP_BAD_REQUEST

    query = "SELECT * FROM Doctors WHERE ID_DOCTOR = :id_doctor"
    cursor.execute(query, [id_doctor])
    result = cursor.fetchall()

    if not result:
        return jsonify({"error": "Doctor not found."}), HTTP_NOT_FOUND

    doctor = ut.get_dictionary_from_query(result, cursor)

    return jsonify(doctor), HTTP_OK

## POST Doctor
@doctors_blueprint.route('/add', methods=['POST'])
def doctor_post_medicine():
    data = request.json

    if not all(key in data for key in ['certId', 'name', 'last_name', 'phoneNumber', 'OfficeAddress']):
        return jsonify({"error": "Missing data for one or more fields."}), HTTP_BAD_REQUEST

    IdCert = ut.generate_random_number()

    query = "INSERT INTO Doctors (IdCert, name, last_name, phoneNumber, OfficeAddress) VALUES (:IdCert, :name, :last_name, :phoneNumber, :OfficeAddress)"


    try:
        cursor.execute(query, [IdCert, data['name'], data['last_name'], data['phoneNumber'], data['OfficeAddress']])
        connection.commit()
        return jsonify({"success": "Doctor added successfully."}), HTTP_OK

    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), HTTP_INTERNAL_SERVER_ERROR
