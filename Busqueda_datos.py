def generacion_sublistas():
    """Esta funcion toma el archivo completo y lo va subdividiendo en listas, retorna->:
    1) Lista_DPI: En esta lista van a estar todos los numeros de DPI de los estudiantes
    2) Lista_nombre_apellidos: En esta lista van a esta solo  los nombres y los apellidos de los estudiantes
    3) Lista_telefono: En esta lista van a estar el numero de telefono de los estudiantes
    4) Lista correo: En esta lista van a estar solo los correos de los estudiantes
    """
    #Listas vacias
    lista_identidad = []  #Guarda el nombre y el apellido
    lista_DPI = []
    lista_telefonos = []
    lista_correo = []
    
    #Variables enteras
    numeroNom = 0       #Posicion asociada al nombre
    numeroApe = 1       #Posicion asociada al apellido
    numeroDPI = 2       #Posicion DPI
    numeroTel = 4       #Posicion del Telefono
    numeroCorreo = 5    #Posicion del correo
    
    
    with open('Base_datos_estudiantes.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            #Guarda el nombre en una lista
            if index == numeroNom:
                numeroNom += 8
                lista_identidad.append(dato)
                
            #Guarda el apellido en una lista    
            if index == numeroApe:
                numeroApe += 8
                lista_identidad.append(dato)
                
            #Guarda el numero de DPI en una lista
            if index == numeroDPI:
                numeroDPI += 8
                lista_DPI.append(dato)
            
            #Guarda el numero de telefono en una lista
            if index == numeroTel:
                numeroTel += 8
                lista_telefonos.append(dato)
                
            #Gurda el numero de correo en una lista
            if index == numeroCorreo:
                numeroCorreo += 8
                lista_correo.append(dato)
                lista_identidad.append(dato)
            
    
    return lista_DPI, lista_identidad, lista_telefonos, lista_correo


#Funcion para la busqueda de datos
def validacion2_DPI(clave, lista):
    """La funcion sirve para buscar un dato en este caso busca un numero de DPI en la lista DPI 
    retorna: -> True si el numero buscado aparece en la lista y False sino aparece (es unico)"""
    if clave in lista:           #Busca si el numero existe en el documento
        resultado_DPI = True     #El numero da error por no ser unico
    else:
        resultado_DPI = False    #El numero es unico
    return resultado_DPI         #Retorna si es unico o no

#Busca si el numero de telefono existe en la base
def validacion2_telefono(clave, lista):
    """La funcion sirve para buscar un dato en este caso busca un numero de telefono  en la lista numeros de los estudiantes 
    retorna: -> True si el numero buscado aparece en la lista y False sino aparece"""
    if clave in lista:
        resultado_telefono = True
    else:
        resultado_telefono = False
    return resultado_telefono

#Busca si el correo es unico
def validacion2_correo(clave, lista):
    """La funcion sirve para buscar un dato en este caso busca el correo  en la lista de correos de  los estudiantes 
    retorna: -> True si el correo buscado aparece en la lista y False sino aparece"""
    if clave in lista:
        resultado_correo = True
    else:
        resultado_correo = False
    return resultado_correo

def validacion2_identidad(clave_nombre, clave_apellido, lista_identidad):
    """La funcion sirve para buscar un dato en este caso busca el nombre y el apellido  en la lista de correos de  los estudiantes 
    retorna: -> True si el correo buscado aparece en la lista y False sino aparece"""
    for index, busqueda in enumerate(lista_identidad):          #Obtiene el index de la lista 
        if clave_nombre == busqueda:                            #busca el nombre dentro de la lista
            if clave_apellido == lista_identidad(index+1):      #Si lo encuentra revisa que el apellido siguiente sea igual
                return True
    else:
        return False                                            #Si no todo lo anterior esta correcto