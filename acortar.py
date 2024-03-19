import json
import secrets
import string

def generar_codigo():
    # Definir los caracteres posibles para generar el código aleatorio
    alfanumerica = string.ascii_letters + string.digits

    # Generar una cadena de 8 caracteres aleatorios
    random_string = "".join(secrets.choice(alfanumerica) for i in range(8))

    return random_string

def acortar_enlace(enlace):
    # Generar un nuevo código único
    codigo = generar_codigo()

    # Cargar los datos existentes desde el archivo (si existe)
    try:
        with open("codigos.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        # Si el archivo no existe, inicializamos una lista vacía
        data = []

    # Verificar si el código generado ya existe en los datos cargados
    while any(item["codigo"] == codigo for item in data):
        codigo = generar_codigo()  # Si existe, generamos un nuevo código único

    # Agregar el nuevo enlace acortado al conjunto de datos
    data.append({
        "codigo": codigo,  # Nuevo código generado
        "sitio_web": f"http://localhost:5000/{codigo}",  # URL del enlace acortado
        "redireccion": enlace,  # URL original que será redirigida
    })

    # Escribir los datos actualizados de vuelta al archivo JSON
    with open("codigos.json", "w") as f:
        json.dump(data, f, indent=4)

# Llamar a la función con un ejemplo de enlace para acortarlo
acortar_enlace("https://www.linkedin.com/in/andres-ramirez-4a677023b/")
