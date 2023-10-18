from cryptography.fernet import Fernet

# La clave
clave_cifrado = b'd3iXJXBhYZ0ZasXWw_lIafJ3HyDHZoAmsD7ysmEbjtA='
fernet = Fernet(clave_cifrado)

#!A partir de aqui surge el error
def guardado(datos, nombre_de_arcivo):
    password_cifrado = fernet.encrypt(datos[6].encode())
    datos[6]=password_cifrado
    
    # Especifica el nombre del archivo
    nombre_archivo = nombre_de_arcivo
    try:
        # Abre el archivo en modo append
        with open(nombre_archivo, "a") as archivo:
            # Agrega valores en el archivo de forma vertical
            for dato in datos[:6]:
                archivo.write(dato + '\n')
                
                
        # Abre el archivo en modo append y escritura de bytes ("ab") solo para la contraseña cifrada
        with open(nombre_archivo, "ab") as archivo_binario:
            archivo_binario.write(datos[6] + b'\n')  # Almacena la contraseña cifrada como bytes
            
        return True
    except FileNotFoundError:
        return False
    
