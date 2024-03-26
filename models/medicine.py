from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://admin:pM6XSAkKWteG@adb.us-ashburn-1.oraclecloud.com:1522/?service_name=g4a1d86d8e421b7_iotdatabase_low.adb.oraclecloud.com'
db = SQLAlchemy(app)

class Medicine(db.Model):
    __tablename__ = 'medicine'
    medicineId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    active_ingredient = db.Column(db.String(50))
    dosage_form = db.Column(db.String(30))
    prescriptionDetails = db.relationship('prescriptionDetails', backref='medicine')


