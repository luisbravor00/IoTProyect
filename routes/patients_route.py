from flask import Blueprint, jsonify, request, render_template, request, redirect, flash
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor
import controllers.utilities as ut

patients_blueprint = Blueprint('patients', __name__)

# Routes

## GET Ruta Base
@patients_blueprint.route('/')
def patients_home():
    return render_template('patients.html'), HTTP_OK

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

## GET Doctor By ID
@patients_blueprint.route('/patient')
def doctors_get_doctor_by_id():
    id_patient = request.args.get('id_patient', type=int)

    if not id_patient:
        return jsonify({"error": "ID_PATIENT is required."}), HTTP_BAD_REQUEST

    query = "SELECT * FROM Patients WHERE ID_PATIENT = :id_patient"
    cursor.execute(query, [id_patient])
    result = cursor.fetchall()

    if not result:
        return jsonify({"error": "Patient not found."}), HTTP_NOT_FOUND

    patient = ut.get_dictionary_from_query(result, cursor)

    return jsonify(patient), HTTP_OK

#Post Patients
@patients_blueprint.route('/add', methods=['POST'])
def patient_post_patient():
    data = request.json

    if not all(key in data for key in['Name', 'Last_Name', 'Address', 'Age', 'Phone', 'Email']):
        return jsonify({"error": "Missing data for one or more fields."}), HTTP_BAD_REQUEST

    print(f"Data reaches patient endpoint")

    print(data)

    ID_Patient = ut.generate_random_number()

    query = "INSERT INTO Patients (ID_Patient, Name, Last_Name, Address, Age, Phone, Email) VALUES (:ID_Patient, :Name, :Last_Name, :Address, :Age, :Phone, :Email)"

    print(f"Checkpoint before try")
    try:
        cursor.execute(query, [ID_Patient, data['Name'], data['Last_Name'], data['Address'], data['Age'], data['Phone'], data['Email']])
        connection.commit()
        return jsonify({"newId": ID_Patient}), HTTP_OK

    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), HTTP_INTERNAL_SERVER_ERROR
