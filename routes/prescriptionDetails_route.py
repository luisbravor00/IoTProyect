from flask import Blueprint, jsonify, request, render_template, request, redirect, flash
from config.config import *
from controllers.conn import connection, cursor
import controllers.utilities as ut

prescriptionDetails_blueprint = Blueprint('prescriptionDetails', __name__)

@prescriptionDetails_blueprint.route('/')
def prescriptionDetails_home():
    return 'Página de detalles de prescriptions', HTTP_OK

@prescriptionDetails_blueprint.route('/details')
def prescriptionsDetails_detail():
    return 'Detalles de prescriptions', HTTP_OK

#GET ALL
@prescriptionDetails_blueprint.route('/prescriptions')
def prescriptionsDetails_get_all():
    #parameters = {}
    #where_clauses = []
    id_prescription = request.args.get('id_prescription', type=int)

    if not id_prescription:
        return jsonify({"error": "Prescription ID is required bozo."}), HTTP_IM_A_TEAPOT

    #if id_prescription:
    #    where_clauses.append("Prescription.ID_Prescription = :id_prescription")
    #    parameters['id_prescription'] = id_prescription

    query = """
        SELECT
            M.Active_Ingredient as Medication_Name,
            PD.DOSE,
            PD.TIMES_PER_DAY
        FROM Prescription_Details PD
        INNER JOIN 
            Prescription on PD.ID_Prescription = Prescription.ID_Prescription
        INNER JOIN
            Medicine M on PD.ID_Medication = M.ID_Medication
        WHERE Prescription.ID_Prescription = :id_prescription
    """

    #if not where_clauses:
    #    return jsonify({"error": "No results found."}), HTTP_NOT_FOUND
    #query += " WHERE " + " AND ".join(where_clauses)

    #cursor.execute(query, parameters)
    cursor.execute(query, [id_prescription])
    result = cursor.fetchall()

    if not result:
        return jsonify({"error": "No prescription found bucko."}), HTTP_NOT_FOUND

    prescriptionDetails_list = ut.get_dictionary_from_query(result, cursor)

    #prescriptionDetails_list = [
    #    {
    #        "MEDICATION_ACTIVE_INGREDIENT": row[0],
    #        "TIMES_PER_DAY": row[1],
    #        "DOSE": row[2]

    #    }
    #    for row in result
    #]

    return jsonify(prescriptionDetails_list), HTTP_OK

##Post pDetails
@prescriptionDetails_blueprint.route('/add', methods=['POST'])
def prescriptionDetails_post_prescriptionDetails():
    data = request.json
    ID_Detail = ut.generate_random_number()
    print(f"Data is sent to details endpoint")
    print(data)

    if not all(key in data for key in ['ID_Prescription', 'ID_Medication', 'Times_Per_Day', 'Dose']):
        return jsonify({"error": "Missing data from one or more fields"}), HTTP_IM_A_TEAPOT

    query = "INSERT INTO Prescription_Details (ID_Detail, ID_Prescription, ID_Medication, Times_Per_Day, Dose) VALUES (:ID_Detail, :ID_Prescription, :ID_Medication, :Times_Per_Day, :Dose)"

    try:
        cursor.execute(query,  [ID_Detail ,data['ID_Prescription'], data['ID_Medication'], data['Times_Per_Day'], data['Dose']])
        connection.commit()
        return jsonify({"success": "Prescription added successfully"})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}, HTTP_IM_A_TEAPOT)


