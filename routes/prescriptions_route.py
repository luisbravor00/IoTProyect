from flask import Blueprint, jsonify, request, render_template, request, redirect, flash
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
    query = """ SELECT
                    Patients.Name AS Patient_Name,
                    Patients.Last_name AS Patient_Last_name,
                    Patients.Address AS Patient_Address,
                    Patients.Age AS Patient_Age,
                    Patients.Phone AS Patient_Phone,
                    Patients.Email AS Patient_Email,
                    Doctors.Name AS Doctor_Name,
                    Doctors.Last_name AS Doctor_Last_name,
                    Doctors.Phone_num AS Doctor_Phone,
                    Doctors.Office_add AS Doctor_Address,
                    Prescription.ID_Prescription,
                    Prescription.Date_prescribed,
                    Medicine.Name AS Medication_Name,
                    Medicine.Active_Ingredient AS Medication_Active_Ingredient,
                    Prescription_Details.DOSE,
                    Prescription_Details.TIMES_PER_DAY
                FROM
                    Prescription
                INNER JOIN
                    Patients ON Prescription.ID_Patient = Patients.ID_Patient
                INNER JOIN
                    Doctors ON Prescription.ID_Doctor = Doctors.ID_Doctor
                INNER JOIN
                    Prescription_Details ON Prescription.ID_Prescription = Prescription_Details.ID_Prescription
                INNER JOIN
                    Medicine ON Prescription_Details.ID_Medication = Medicine.ID_Medication
            """
    cursor.execute(query)
    result = cursor.fetchall()

    prescriptions_list = ut.get_dictionary_from_query(result, cursor)

    return jsonify(prescriptions_list), HTTP_OK

@prescriptions_blueprint.route('/<int:id_prescription>')
def prescriptions_get_prescription_by_id(id_prescription):
    parameters = {}
    where_clauses = []

    #id_patient = request.args.get('id_patient', type=int)
    #if id_patient:
    #    where_clauses.append("Patients.ID_Patient = :id_patient")
    #    parameters['id_patient'] = id_patient

    #id_doctor = request.args.get('id_doctor', type=int)
    #if id_doctor:
    #    where_clauses.append("Doctors.ID_Doctor = :id_doctor")
    #    parameters['id_doctor'] = id_doctor

    #id_prescription = request.args.get('id_prescription', type=int)
    print(id_prescription)

    if id_prescription:
        where_clauses.append("Prescription.ID_Prescription = :id_prescription")
        parameters['id_prescription'] = id_prescription

    query = """ SELECT
                    Patients.Name || ' ' || Patients.Last_name AS "PATIENT_NAME",
                    Patients.Address AS Patient_Address,
                    Patients.Age AS Patient_Age,
                    Patients.Phone AS Patient_Phone,
                    Patients.Email AS Patient_Email,
                    Doctors.Name || ' ' || Doctors.Last_name AS "DOCTOR_NAME",
                    Doctors.Phone_num AS Doctor_Phone,
                    Doctors.Office_add AS Doctor_Address,
                    Prescription.ID_Prescription,
                    Prescription.Date_prescribed,
                    Medicine.Name AS Medication_Name,
                    Medicine.ActiveIngredient AS Medication_Active_Ingredient,
                    Prescription_Details.DOSE,
                    Prescription_Details.TIMES_PER_DAY
                FROM
                    Prescription
                INNER JOIN
                    Patients ON Prescription.ID_Patient = Patients.ID_Patient
                INNER JOIN
                    Doctors ON Prescription.ID_Doctor = Doctors.ID_Doctor
                INNER JOIN
                    Prescription_Details ON Prescription.ID_Prescription = Prescription_Details.ID_Prescription
                INNER JOIN
                    Medicine ON Prescription_Details.ID_Medication = Medicine.ID_Medication
             """

    if not where_clauses:
        return jsonify({"error": "No results found."}), HTTP_NOT_FOUND

    query += " WHERE " + " AND ".join(where_clauses)

    cursor.execute(query, parameters)
    result = cursor.fetchall()

    if not result:
        return jsonify({"error": "No results found."}), HTTP_NOT_FOUND

    prescriptions_list = ut.get_dictionary_from_query(result, cursor)

    return jsonify(prescriptions_list), HTTP_OK

#Post Prescriptions
@prescriptions_blueprint.route('/add', methods=['POST'])
def prescription_post_prescription():
    data = request.json
    print(data)
    print(f"Data is sent to this endpoint")
    

    if not all(key in data for key in ['ID_Doctor', 'ID_Patient', 'Date_Prescribed']):
        return jsonify({"error": "Missing data from one or more fields"}), HTTP_BAD_REQUEST
    ID_Prescription = ut.generate_random_number()


    query = "INSERT INTO Prescription (ID_Prescription, ID_Doctor, ID_Patient, Date_Prescribed) VALUES (:ID_Prescription, :ID_Doctor, :ID_Patient, TO_DATE(:Date_Prescribed, 'YYYY-MM-DD'))"


    print(f"prescription route checkpoint before commit")

    try:
        print(f"Enters try ")
        cursor.execute(query, [ID_Prescription, data['ID_Doctor'], data['ID_Patient'], data['Date_Prescribed']])
        connection.commit()
        return jsonify({"newId": ID_Prescription}), HTTP_OK

    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), HTTP_BAD_REQUEST
