from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://admin:pM6XSAkKWteG@adb.us-ashburn-1.oraclecloud.com:1522/?service_name=g4a1d86d8e421b7_iotdatabase_low.adb.oraclecloud.com'
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patient'
    patientId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50))

