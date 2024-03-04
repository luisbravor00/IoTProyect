from flask import Flask
from routes.prescriptions_route import prescriptions_blueprint
from routes.users_route import users_blueprint

app = Flask(__name__)

app.register_blueprint(prescriptions_blueprint, url_prefix='/prescriptions')
app.register_blueprint(users_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(port=7070)