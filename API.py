from flask import Flask
from routes.prescriptions_route import prescriptions_blueprint
from routes.patients_route import patients_blueprint
from routes.doctors_route import doctors_blueprint
from routes.medicine_route import medicine_blueprint

app = Flask(__name__)

app.register_blueprint(prescriptions_blueprint, url_prefix='/prescriptions')
app.register_blueprint(patients_blueprint, url_prefix='/patients')
app.register_blueprint(doctors_blueprint, url_prefix='/doctors')
app.register_blueprint(medicine_blueprint, url_prefix='/medicine')

if __name__ == '__main__':
    app.run(port=7070)