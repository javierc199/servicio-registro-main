from flask import Flask, request, jsonify
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
from io import BytesIO


# Cargar el modelo
model = load_model('C:/Users/javie/Videos/modelosh5/modeloInceptionV3(3clases).h5')

# Inicializar Flask
app = Flask(__name__)


# Función para preprocesar la imagen antes de pasarla al modelo
def preprocess_image(img):
    # Convertir el archivo subido a un objeto BytesIO
    img_stream = BytesIO(img.read())

    # Cambiar tamaño de la imagen a 300x300
    img = image.load_img(img_stream, target_size=(300, 300))

    # Convertir la imagen a un array numpy
    img_array = image.img_to_array(img)

    # Normalizar los valores de píxeles al rango [0, 1]
    img_array /= 255.0
    return img_array


# Ruta para realizar la inferencia
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener la imagen de la solicitud
    imagen = request.files['image']

    # Preprocesar la imagen
    processed_image = preprocess_image(imagen)

    # Realizar la inferencia
    predictions = model.predict(np.expand_dims(processed_image, axis=0))

    # Mapear las clases a los nombres de las etiquetas
    class_names = ['result_tb', 'result_no_tb', 'result_normal']

    # Crear un diccionario de resultados en formato JSON
    results = {
        class_names[i]: float(predictions[0][i]) for i in range(len(class_names))
    }

    return jsonify(results)


if __name__ == '__main__':
       # Ejecutar la aplicación Flask en el puerto 5000
       app.run(port=5000)