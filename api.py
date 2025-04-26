from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields
import joblib
import pandas as pd

# Inicializar Flask
app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='API de Predicción',
          description='Predicciones del modelo de Árbol de Decisión para canciones')

# Cargar el modelo entrenado
modelo = joblib.load('decision_tree_model.pkl')

# Definir el namespace
ns = api.namespace('predict', description='Predicciones del modelo')

# Definir el modelo de entrada (ajustado a las variables de su modelo)
input_model = api.model('InputModel', {
    'duration_ms': fields.Integer(required=True, description='Duración de la canción en milisegundos'),
    'explicit': fields.Integer(required=True, description='Es explícita la canción (1) o no (0)'),
    'danceability': fields.Float(required=True, description='Nivel de bailabilidad'),
    'energy': fields.Float(required=True, description='Nivel de energía'),
    'key': fields.Integer(required=True, description='Tonalidad de la canción'),
    'loudness': fields.Float(required=True, description='Volumen promedio en decibeles'),
    'mode': fields.Integer(required=True, description='Modo mayor (1) o menor (0)'),
    'speechiness': fields.Float(required=True, description='Cantidad de palabras habladas'),
    'acousticness': fields.Float(required=True, description='Nivel de acústica'),
    'instrumentalness': fields.Float(required=True, description='Nivel instrumental'),
    'liveness': fields.Float(required=True, description='Presencia de audiencia en vivo'),
    'valence': fields.Float(required=True, description='Nivel de positividad emocional'),
    'tempo': fields.Float(required=True, description='Tempo en BPM'),
    'time_signature': fields.Integer(required=True, description='Compás musical'),
    'track_genre_encoded': fields.Float(required=True, description='Género codificado de la pista')
})

# Definir el endpoint de predicción
@ns.route('/')
class Predict(Resource):
    @ns.expect(input_model)
    def post(self):
        try:
            # Obtener los datos del request
            data = request.get_json()
            # Convertir a DataFrame
            input_df = pd.DataFrame([data])
            # Hacer la predicción
            pred = modelo.predict(input_df)
            # Retornar la predicción
            return jsonify({'prediction': pred.tolist()})
        except Exception as e:
            return {'error': str(e)}, 400

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
