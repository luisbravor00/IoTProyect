from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from flask_cors import CORS
import os 
from dotenv import load_dotenv
from models import *
from routes.prescriptionDetails_route import prescriptionDetails_blueprint
from routes.prescriptions_route import prescriptions_blueprint
from routes.patients_route import patients_blueprint
from routes.doctors_route import doctors_blueprint
from routes.medicine_route import medicine_blueprint
from controllers.conn import connection, cursor
from controllers import utilities as ut
from config.config import *

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['APP_URL'] = os.getenv('APP_URL')

###
app.secret_key = os.getenv("APP_SECRET_KEY")

app.register_blueprint(prescriptionDetails_blueprint, url_prefix='/prescriptionDetails')
app.register_blueprint(prescriptions_blueprint, url_prefix='/prescriptions')
app.register_blueprint(patients_blueprint, url_prefix='/patients')
app.register_blueprint(doctors_blueprint, url_prefix='/doctors')
app.register_blueprint(medicine_blueprint, url_prefix='/medicine')




###Authentication for user
def authenticate_user(id):
   ##check to see if the user is a doctor or patient
    doctorQuery = "SELECT name FROM Doctors WHERE ID_DOCTOR = :1"
    cursor.execute(doctorQuery,(id,))
    doctor = cursor.fetchone()

    patientQuery = "SELECT name FROM Patients WHERE ID_PATIENT = :1"
    cursor.execute(patientQuery, (id,))
    patient = cursor.fetchone()

    if doctor:
        return 'doctor', doctor[0]
    elif patient:
        return 'patient', patient[0]
    else:
        return 0, 0  

@app.route("/")
def index():
    return render_template('index.html'), HTTP_OK

@app.route("/about")
def doctors():
    return render_template('our_doctors.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.get_json()
        id = data.get('user')
    else:
        id = request.args.get('user')
    
    role, name = authenticate_user(id)
    if role == 'doctor':
        return jsonify({'redirect': url_for('doctor_interface', doctor_id=id)})
        #doctor_name = name
        #return render_template('doctorInterface.html', doctor_name = doctor_name)
    elif role == 'patient':
        return jsonify({'redirect': url_for('patient_interface', patient_id=id)})
        #patient_name = name
        #return render_template('patientInterface.html', patient_name = patient_name)
    else:
        flash(f"Error ocurred, please try again.")

    return render_template('login.html')

@app.route("/doctorInterface/<int:doctor_id>", methods=["GET", "POST"])
def doctor_interface(doctor_id):
    #doctor_id = request.args.get('doctor_id')
    doctor_name = authenticate_user(doctor_id)[1]
    #fetch the list of patients for the doctor
    patientData = getPatients(doctor_id)
    patients = patientData
    #fetch medicine
    fetchMedicineQuery = """ SELECT DISTINCT(name) as name, ID_MEDICATION, active_ingredient, dosage_form 
                            FROM Medicine
                        """
    cursor.execute(fetchMedicineQuery)
    medicines = cursor.fetchall()

    medicineData = []
    for medicine in medicines:
        medicine_info = {
            'name': medicine[0],
            'medicineId': medicine[1],
            'activeIngredient': medicine[2],
            'Dosage': medicine[3]
        }
        medicineData.append(medicine_info)
    #print(f"Medicine Data")
    #print(medicineData)
    #print("\n")
    medicine=medicineData

    return render_template('doctorInterface.html', doctor_name=doctor_name, doctor_id=doctor_id, patients=patients, medicines=medicine)

@app.route("/patient_interface/<int:patient_id>")
def patient_interface():
    patient_name = authenticate_user(patient_id)[1]
    return render_template('patientInterface.html', patient_name=patient_name, patient_id=patient_id)

#post contact form, i just don't want to make another file 
@app.route('/contact', methods=['POST'])
def post_contact_form():
    data = request.json
    if not all(key in data for key in['name', 'email', 'message']):
        return jsonify({'error':'Missing data for one or more fields'}), HTTP_BAD_REQUEST
    query = 'INSERT INTO contactUs (name, email, message) values(:name, :email, :message)'
    
    try:
        cursor.execute(query, [ data['name'], data['email'], data['message']])

        connection.commit()
        return jsonify({"success": "Patient added successfully."}), HTTP_OK

    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), HTTP_INTERNAL_SERVER_ERROR
    

##fetching patients that belong to the doctor
#@app.route("/doctorInterface/<int:doctor_id>", methods=["GET", "POST"])
def getPatients(doctor_id):
    #data = request.get_json()
    #doctor_id = data.get('user')

    ##QUERY
    fetchQuery = """SELECT DISTINCT(PT.name), PT.ID_Patient, PT.last_name, PT.age, PT.phone
                  FROM Prescription P
                  LEFT JOIN Patients PT ON PT.ID_PATIENT = P.ID_PATIENT
                  WHERE P.ID_DOCTOR = :doctor_id
                  """

    cursor.execute(fetchQuery, {'doctor_id': doctor_id})
    patients = cursor.fetchall()
    print(f"Query")
    print(patients)

    patientData = []
    for patient in patients:
        print(patient)
        patient_info = {
            'patientId': patient[1],
            'name': patient[0],
            'last_name': patient[2],
            'age': patient[3],
            'phone': patient[4]
        }
        patientData.append(patient_info)
    print(f"Patient Data")
    print(patientData)
    print("\n")

    return patientData
    


if __name__ == '__main__':
    #Uncomment for local use
    app.run(port=7070)
    index()
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)