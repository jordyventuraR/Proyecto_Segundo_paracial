#Programa para la busqueda de datos
def validacion2_DPI(numero_busqueda):
    busqueda_DPI = []
    print("Validacion 2 de DPI")
    try:
        with open('Almacenado_DPI.txt', 'r') as fp:
            busqueda_DPI = fp.readlines()
            if numero_busqueda in busqueda_DPI:
                resultado_DPI = True
            else:
                resultado_DPI = False
    except FileNotFoundError:
        print("No se pudo leer el archivo")
        resultado_DPI = False
    return resultado_DPI

def validacion2_telefono(clave_busqueda):
    busqueda_telefono = []
    print("Validacion 2 de telefono")
    try:
        with open('Almacenado_telefono.txt', 'r') as fp:
            busqueda_telefono = fp.readlines()
            if clave_busqueda in busqueda_telefono:
                resultado_telefono = True
            else:
                resultado_telefono = False
    except FileNotFoundError:
        print("No se pudo leer el archivo")
        resultado_telefono = False
    return resultado_telefono

def validacion2_correo(clave_busqueda):
    busqueda_correo = []
    print("Validacion 2 de correo")
    try:
        with open('almacenado_correo.txt', 'r') as fp:
            busqueda_correo = fp.readlines()
            if clave_busqueda in busqueda_correo:
                resultado_correo = True
            else:
                resultado_correo = False
    except FileNotFoundError:
        print("No se pudo leer el archivo")
        resultado_correo = False
    return resultado_correo

def validacion2_username(clave_busqueda):
    busqueda_username = []
    print("Validacion 2 de username")
    try:
        with open('Almacenado_username.txt', 'r') as fp:
            busqueda_username = fp.readlines()
            if clave_busqueda in busqueda_username:
                resultado_username = True
            else:
                resultado_username = False
    except FileNotFoundError:
        print("No se pudo leer el archivo")
        resultado_username = False
    return resultado_username
