import os
from flask import Flask, redirect
import json

# Creamos una instancia de la aplicación web usando Flask
app = Flask(__name__)

# Definimos la función para redirigir los enlaces acortados
@app.route('/<string:codigo>')
def redireccion(codigo: str):
    # Inicializamos una lista vacía para almacenar los datos de los enlaces acortados
    data = []

    # Abrimos el archivo que contiene los datos de los enlaces acortados (codigos.json)
    # y cargamos su contenido en la variable 'data'
    with open("codigos.json", "r") as f:
        data = json.load(f)

    # Buscamos en los datos cargados un enlace que coincida con el código proporcionado en la URL
    resp = list(filter(lambda x: x['codigo'] == codigo, data))

    # Verificamos si encontramos un enlace con el código proporcionado
    if resp:
        # Si encontramos un enlace, redirigimos al usuario al destino original del enlace
        return redirect(resp[0]['redireccion'], code=302)

    # Si no encontramos un enlace con el código proporcionado, devolvemos un mensaje indicando que no se encontró ningún enlace
    return {
        "message": "No se encontró ningún enlace con el código proporcionado."
    }

# Iniciamos el servidor web Flask
if __name__ == "__main__":
    # Configuramos el servidor para que esté disponible en todas las interfaces de red
    # y en el puerto 5000, con la opción de depuración habilitada
    app.run(host="0.0.0.0", port=5000, debug=True)
