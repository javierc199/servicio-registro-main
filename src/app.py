from flask import Flask
from config import config
from flask_cors import CORS
from routes import routeregistro
from keras.models import load_model

app = Flask(__name__)

model = load_model('C:/Users/javie/Videos/modelosh5/modeloInceptionV3(3clases).h5')
modelosino = load_model('C:/Users/javie/Videos/modelosh5/validacion_imagen.h5')

# Configuración CORS
CORS(app)

# Configuración de las rutas
app.register_blueprint(routeregistro.main, url_prefix='/api/resultados')

# Manejador de error 404
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Not found page</h1>", 404

# Configuración de la aplicación
app.config.from_object(config['development'])

if __name__ == '__main__':
    app.run(host='192.168.100.35', port=8000)

    