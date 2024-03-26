from flask import Blueprint, jsonify, request
from config.config import *
from controllers.conn import conenection, cursor
import controllers.utilities as ut

prescriptionsDetails_blueprint = Blueprint('prescriptions', __name__)

@prescriptionsDetails_blueprint.route('/')
def prescriptionDetails_home():
    return 'Página de detalles de prescriptions', HTTP_OK

@prescriptionsDetails_blueprint.route('/details')
def prescriptionsDetails_detail():
    return 'Detalles de prescriptions', HTTP_OK

#GET ALL
@prescriptionsDetails_blueprint.route('/data')
def prescriptionsDetails_get_all():
    query = """
        SELECT
            M.Name as Medication_Name,
            PD.Times_Per_Day AS Times_Per_Day(2=every 12 hours, 3=every 8 hours)
            PD.Dose
        
        FROM Prescription_Details as PD
        INNER JOIN 
            Prescription as P on Prescription_Details.ID_Prescription = Prescription.ID_Prescription
        INNER JOIN
            Medicine as M on Prescription_Details.ID_Medicine = Medicine.ID_Medicine
    """
    cursor.execute(query)
    result = cursor.fetchall()

    prescriptionDetails_lists = ut.get_dictionary_from_quer(result, cursor)

    return jsonify(prescriptionDetails_lists), HTTP_OK



