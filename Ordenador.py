import os
import shutil

# Define el directorio que quieres ordenar
directorio = 'C:/Users/Eduardo/Downloads'

# Crea un diccionario vacío para almacenar los archivos por extensión
archivos_por_extension = {}

# Recorre todos los archivos en el directorio
for archivo in os.listdir(directorio):
    # Obtiene la extensión del archivo
    _, extension = os.path.splitext(archivo)
    # Agrega el archivo al diccionario correspondiente a su extensión
    if extension not in archivos_por_extension:
        archivos_por_extension[extension] = [archivo]
    else:
        archivos_por_extension[extension].append(archivo)

# Crea una carpeta para cada extensión y mueve los archivos a su carpeta correspondiente
for extension, archivos in archivos_por_extension.items():
    # Crea la carpeta si no existe
    carpeta = os.path.join(directorio, extension[1:].lower())
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
    # Mueve los archivos a la carpeta correspondiente
    for archivo in archivos:
        origen = os.path.join(directorio, archivo)
        destino = os.path.join(carpeta, archivo)
        shutil.move(origen, destino)