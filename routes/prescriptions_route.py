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
                    Prescription_Details.Dose,
                    Prescription_Details.Frequency
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

## GET All Prescriptions
@prescriptions_blueprint.route('/prescription')
def prescriptions_get_prescription_by_id_patient():

    id_patient = request.args.get('id_patient', type=int)

    if not id_patient:
        return jsonify({"error": "ID_PATIENT is required."}), HTTP_BAD_REQUEST

    query = """ SELECT
                    Patients.Name || ' ' || Patients.Last_name AS "Patient_Name",
                    Patients.Address AS Patient_Address,
                    Patients.Age AS Patient_Age,
                    Patients.Phone AS Patient_Phone,
                    Patients.Email AS Patient_Email,
                    Doctors.Name || ' ' || Doctors.Last_name AS "Doctor_Name",
                    Doctors.Phone_num AS Doctor_Phone,
                    Doctors.Office_add AS Doctor_Address,
                    Prescription.ID_Prescription,
                    Prescription.Date_prescribed,
                    Medicine.Name AS Medication_Name,
                    Prescription_Details.Dose,
                    Prescription_Details.Frequency
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
                WHERE Patients.ID_Patient = :id_patient
            """
    cursor.execute(query, [id_patient])
    result = cursor.fetchall()
    
    if not result:
        return jsonify({"error": "Patient not found."}), HTTP_NOT_FOUND

    prescriptions_list = ut.get_dictionary_from_query(result, cursor)

    return jsonify(prescriptions_list), HTTP_OK