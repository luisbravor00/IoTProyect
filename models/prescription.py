from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://admin:pM6XSAkKWteG@adb.us-ashburn-1.oraclecloud.com:1522/?service_name=g4a1d86d8e421b7_iotdatabase_low.adb.oraclecloud.com'
db = SQLAlchemy(app)

class Prescription(db.Model):
    __tablename__ = 'prescription'
    prescriptionId = db.Column(db.Integer, primary_key=True)
    docterId = db.Column(db.ForeignKey('doctors.certId'))
    patientId = db.Column(db.ForeignKey('patient.patientId'))
    medicineId = db.relationship('medicine', backref='prescription')
    TimesPerDay = db.Column(db.Integer)
    Date = db.Column(db.Date)

