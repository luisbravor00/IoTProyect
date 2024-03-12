from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://admin:pM6XSAkKWteG@adb.us-ashburn-1.oraclecloud.com:1522/?service_name=g4a1d86d8e421b7_iotdatabase_low.adb.oraclecloud.com'
db = SQLAlchemy(app)

class prescription_details(db.Model):
    __tablename__ = 'prescription_details'
    pDetails = db.Column(db.Integer, primary_key=True)
    prescription = db.Column(db.Integer)
    medicine = db.Column(db.Integer)
    dose = db.Column(db.String(50))
    frequency = db.Column(db.String(40))