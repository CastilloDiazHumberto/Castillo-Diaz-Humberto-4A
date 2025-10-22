#Controlador encargado de la logica de autenticación.
#Nos sirvc para separar la logica del login para mantener limpio el codigo de la interfaz

from database import crear_conexion

def validar_credenciales (usuarios, password):

    conexion = crear_conexion()

    if not conexion:
        return False
    
    cursor = conexion.cursor()
    