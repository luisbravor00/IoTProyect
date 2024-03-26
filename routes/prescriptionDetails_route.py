from flask import Blueprint, jsonify, request
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
@prescriptionDetails_blueprint.route('/<int:id_prescription>')
def prescriptionsDetails_get_all(id_prescription):
    parameters = {}
    where_clauses = []

    if id_prescription:
        where_clauses.append("Prescription.ID_Prescription = :id_prescription")
        parameters['id_prescription'] = id_prescription

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
    """

    if not where_clauses:
        return jsonify({"error": "No results found."}), HTTP_NOT_FOUND
    query += " WHERE " + " AND ".join(where_clauses)

    cursor.execute(query, parameters)
    result = cursor.fetchall()

    if not result:
        return jsonify({"error": "No results found."}), HTTP_NOT_FOUND

    #prescriptionDetails_list = ut.get_dictionary_from_query(result, cursor)

    prescriptionDetails_list = [
        {
            "MEDICATION_ACTIVE_INGREDIENT": row[0],
            "TIMES_PER_DAY": row[1],
            "DOSE": row[2]

        }
        for row in result
    ]

    return jsonify(prescriptionDetails_list), HTTP_OK


