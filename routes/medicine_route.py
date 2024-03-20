from flask import Blueprint, jsonify, request
from datetime import datetime
from config.config import *
from controllers.conn import connection, cursor
import controllers.utilities as ut
import random

medicine_blueprint = Blueprint('medicine', __name__)

# Routes

## GET Ruta Base
@medicine_blueprint.route('/')
def medicine_home():
    return 'Página de medicine', HTTP_OK

## GET Ruta Base
@medicine_blueprint.route('/details')
def medicine_detail():
    return 'Detalle de medicine', HTTP_OK

## GET All medicine
@medicine_blueprint.route('/data')
def medicine_get_all():
    query = "SELECT * FROM Medicine"
    cursor.execute(query)
    result = cursor.fetchall()

    medicine_list = ut.get_dictionary_from_query(result, cursor)

    return jsonify(medicine_list), HTTP_OK

## GET Doctor By ID
@medicine_blueprint.route('/medicines')
def medicine_get_medicine_by_id():
    id_medicine = request.args.get('id_medication', type=int)

    if not id_medicine:
        return jsonify({"error": "ID_MEDICINE is required."}), HTTP_BAD_REQUEST

    query = "SELECT * FROM medicine WHERE ID_MEDICATION = :id_medication"
    cursor.execute(query, [id_medicine])
    result = cursor.fetchall()

    if not result:
        return jsonify({"error": "Medicine not found."}), HTTP_NOT_FOUND

    medicine = ut.get_dictionary_from_query(result, cursor)

    return jsonify(medicine), HTTP_OK

## POST Medicine
@medicine_blueprint.route('/add', methods=['POST'])
def medicine_post_medicine():
    # Obtén los datos del cuerpo de la solicitud
    data = request.json

    # Valida que los datos necesarios estén presentes
    if not all(key in data for key in ['Name', 'Active_Ingredient', 'Dosage_Form']):
        return jsonify({"error": "Missing data for one or more fields."}), HTTP_BAD_REQUEST

    ID_Medication = ut.generate_random_number()

    # Prepara la consulta SQL utilizando parámetros con nombre para evitar inyecciones SQL
    query = "INSERT INTO Medicine (ID_Medication, Name, Active_Ingredient, Dosage_Form) VALUES (:id_medication, :name, :active_ingredient, :dosage_form)"

    try:
        # Ejecuta la consulta
        cursor.execute(query, [ID_Medication, data['Name'], data['Active_Ingredient'], data['Dosage_Form']])

        # Confirma los cambios si la inserción es exitosa
        connection.commit()
        return jsonify({"success": "Medicine added successfully."}), HTTP_OK

    except Exception as e:
        # En caso de un error, realiza un rollback y devuelve un error
        connection.rollback()
        return jsonify({"error": str(e)}), HTTP_INTERNAL_SERVER_ERROR