from flask import Flask, render_template
from routes.prescriptions_route import prescriptions_blueprint
from routes.patients_route import patients_blueprint
from routes.doctors_route import doctors_blueprint
from routes.medicine_route import medicine_blueprint

app = Flask(__name__)

app.register_blueprint(prescriptions_blueprint, url_prefix='/prescriptions')
app.register_blueprint(patients_blueprint, url_prefix='/patients')
app.register_blueprint(doctors_blueprint, url_prefix='/doctors')
app.register_blueprint(medicine_blueprint, url_prefix='/medicine')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    #Uncomment for local use
    app.run(port=7070)
    index()
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)