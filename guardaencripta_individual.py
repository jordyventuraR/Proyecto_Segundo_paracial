
def guardado_estudiante(datos_estudiantes):
    #!Aqui te quedaste trabajando anoche
    """Guarda todos los datos y la contraseña la guarda como un dato encriptado
    recibe como parametro: 
    1) datos del estudiante
    2) password """
    #Encripta la contraseña 
    
    # Genera el nombre del archivo con el número incrementado
    nombre_archivo = f"{datos_estudiantes[0]}.txt"
    
    # Abre el archivo en modo de texto para los primeros 5 datos
    # y en modo binario para el último dato cifrado
    with open(nombre_archivo, "w") as archivo:
        for dato in datos_estudiantes[:6]:
            archivo.write(dato + '\n')

    with open(nombre_archivo, "ab") as archivo:
        archivo.write(datos_estudiantes[6] + b'\n')
        
    print("13 banderin")
