from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from models import *
from routes.prescriptionDetails_route import prescriptionDetails_blueprint
from routes.prescriptions_route import prescriptions_blueprint
from routes.patients_route import patients_blueprint
from routes.doctors_route import doctors_blueprint
from routes.medicine_route import medicine_blueprint
from controllers.conn import connection, cursor
from config.config import *

app = Flask(__name__)

###
app.secret_key = b'hfsdoahifhaosdhf'

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

@app.route("/doctorInterface")
def doctor_interface():
    doctor_id = request.args.get('doctor_id')
    doctor_name = authenticate_user(doctor_id)[1]
    return render_template('doctorInterface.html', doctor_name=doctor_name, doctor_id=doctor_id)

@app.route("/patient_interface/<int:patient_id>")
def patient_interface():
    patient_name = authenticate_user(patient_id)[1]
    return render_template('patientInterface.html', patient_name=patient_name, patient_id=patient_id)



##fetching patients that belong to the doctor
@app.route("/doctorInterface/<int:doctor_id>", methods=["GET"])
def getPatients(doctor_id):
    #data = request.get_json()
    #doctor_id = data.get('user')

    ##QUERY
    fetchQuery = """SELECT PT.name, PT.last_name, PT.age, PT.phone
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
            'name': patient[0],
            'last_name': patient[1],
            'age': patient[2],
            'phone': patient[3]
        }
        patientData.append(patient_info)
    print(f"Patient Data")
    print(patientData)

    return jsonify(patientData)
    

##Ignore for now, will be used onced front is integrated. This is only the initial structure.
@app.route("/doctorInterface/<int:doctor_id>", methods=["POST"])
def addPrescription(doctor_id):
    try:
        patientId = request.form.get("patientId")
        doctorId = request.form.get("doctorId")
        medicineId = request.form.get("medicineId")
        Times_Per_day = request.form.get("timesPD")
        Dose = request.form.get("dose")

        if not patientId or not doctorId or not medicineId:
            #flash is kinda like alert from js i guess
            flash("Please enter a valid patient, doctor or medicine ID please", "Error")
            return redirect("prescription/add")

        ##NOT COMPLETE
        newPrescription = prescriptions_blueprint(patientId=patientId, doctorId=doctorId, medicineId=medicineId, Times_Per_day=Times_Per_day, Dose=Dose)
        cursor.execute(newPrescription)
        connection.commit()

        flash("Prescription added successfully!", "success")
        return redirect("/prescriptions")
    except Exception as e:
        flash(f"An error ocurred: {str(e)}", "error")
        return redirect("/prescription/add")


if __name__ == '__main__':
    #Uncomment for local use
    app.run(port=7070)
    index()
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)