from flask import Flask, render_template, request, redirect, flash
from models import *
import os
from dotenv import load_dotenv
import oracledb

load_dotenv()
dbuser = os.getenv('DATABASE_USER')
dbpswd = os.getenv('DATABASE_PSWD')
dbdir = os.getenv('DIR_LOCATION')
##CHANGE DEPENDING ON YOUR .ENV FILE!!!
cs = os.getenv('DNS')



print(dbdir)

connection = oracledb.connect(config_dir = dbdir,  user= dbuser,
                              password=dbpswd, dsn=cs,
                              wallet_location = dbdir, wallet_password=dbpswd)

cursor = connection.cursor()

from routes.prescriptionDetails_route import prescriptionDetails_blueprint
from routes.prescriptions_route import prescriptions_blueprint
from routes.patients_route import patients_blueprint
from routes.doctors_route import doctors_blueprint
from routes.medicine_route import medicine_blueprint

app = Flask(__name__)

app.register_blueprint(prescriptionDetails_blueprint, url_prefix='/prescriptionDetails')
app.register_blueprint(prescriptions_blueprint, url_prefix='/prescriptions')
app.register_blueprint(patients_blueprint, url_prefix='/patients')
app.register_blueprint(doctors_blueprint, url_prefix='/doctors')
app.register_blueprint(medicine_blueprint, url_prefix='/medicine')

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/templates/patients.html")
def patients():
    return render_template('patients.html')

@app.route("/templates/ourDoctor.html")
def doctors():
    return render_template('ourDoctor.html')


##Ignore for now, will be used onced front is integrated. This is only the initial structure.
@app.route("/prescriptions/add", methods=["POST"])
def addPrescription():
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
    #app.run(port=7070)
    index()
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)