from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb+srv://iotadmin:iotadmin@test.mygbwdt.mongodb.net/', 27017)
db = client['IoT']  # Reemplaza 'tu_base_de_datos' con el nombre de tu base de datos
collection = db['usuarios']  # Nombre de la colección donde se guardarán los datos

@app.route('/datos', methods=['GET'])
def obtener_usuarios():
    # Consulta para obtener todos los usuarios
    usuarios = collection.find()
    # Convertir el resultado en una lista de diccionarios
    lista_usuarios = [usuario for usuario in usuarios]
    return lista_usuarios

if __name__ == '__main__':
    app.run(port=3000)