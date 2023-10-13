#Librerias para el uso de correos
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart  import MIMEMultipart
import time

remitente = "hogwartsesculademagia@gmail.com"   #Desde el correo que vamos a enviar el mensaje
password = "wksg icol fqnd hvif"                #La contraseña de verificacion en dos pasos


def confirmacion_new(correo, nombre, casa) ->str:
    """
    Esta función envía una confirmación por correo electrónico.

    Args:
        correo (Any): La dirección de correo electrónico del destinatario.
        nombre (Any): El nombre del destinatario.
        casa (Any): El nombre de la casa.

    Returns:
        True si el correo se envió correctamente, de lo contrario False.
    """
    try:
        print("15 banderin")
        destinatario = correo                               #Destinatario
        asunto = "Confirmacion de su registro a Hogwarts"   #Asunto del correo
        
        #Creacion del mensaje
        mensaje = MIMEMultipart()
        mensaje["From"]     = remitente     #El correo que envia el mensaje
        mensaje["To"]       = destinatario  #El correo a donde se envia el mensaje
        mensaje["Subject"]  = asunto        #El asunto del correo
        
        #Cuerpo del correo
        cuerpo = "Felicitaciones: " + nombre + " usted formara parte de Hogworts, bienvenido a: " + casa     #El cuerpo dl mensaje
        mensaje.attach(MIMEText(cuerpo, "plain"))       #El contenido del mensaje
        
        #Iniciar sesion en servidor SMTP de gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)    #Especifica el Host y el puerto al cual conectar
        server.starttls()                               #Hace la conecxion con el servidor SMPT y encripta la secion
        server.login(remitente, password)               #Inisia secion en SMPT, con argumentos elusername y el password 
        
        #Enviar mensaje
        texto = mensaje.as_string()                                 #Pasa todo el mensaje como texto
        server.sendmail(remitente, destinatario, texto)    #Envia el mensaje
        server.quit()              #Termino la sesion SMPT 
        time.sleep(7)              #Espera 10seg
        return True
    
    except:
        smtplib.SMTPException
        return False

def correo_adv(correo, nombre):
    """Esta funcion envia un correo al usuario que posee los mismos datos con los cuales se estan creando la nueva cuenta
    en caso de que el nuevo usuario quiera registrar con mismo nombre, apellido y correo en caso contrario solo no deja crear 
    la cuenta pero no advierte al dueño original de estos datos, recibe como argumento:
    1)El correo electronico
    2)El nombre
    """  
    
    destinatario = correo                                                       #Destinatario
    asunto = "Alguien esta ingresando tus datos para nueva cuenta, eres tu?"    #Asunto del correo
    
    #Creacion del mensaje
    mensaje = MIMEMultipart()
    mensaje["From"]     = remitente     #El correo que envia el mensaje
    mensaje["To"]       = destinatario  #El correo a donde se envia el mensaje
    mensaje["Subject"]  = asunto        #El asunto del correo
    
    #Cuerpo del correo
    cuerpo = "Mucho gusto disculpe el inconveniente: " + nombre + "pero al parecer alguien esta intentando crear una cuente de Hogworts, bajo su nombre, apellido y correo... le recuerdo que las cuentas son unicas asi que le recomiendo comunicarse con administracion."  #El cuerpo dl mensaje
    mensaje.attach(MIMEText(cuerpo, "plain"))       #El contenido del mensaje
    
    #Iniciar sesion en servidor SMTP de gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)    #Especifica el Host y el puerto al cual conectar
    server.starttls()                               #Hace la conecxion con el servidor SMPT y encripta la secion
    server.login(remitente, password)               #Inisia secion en SMPT, con argumentos elusername y el password 
    
    #Enviar mensaje
    texto = mensaje.as_string()                                 #Pasa todo el mensaje como texto
    estado = server.sendmail(remitente, destinatario, texto)    #Envia el mensaje
    server.quit()                                               #Termino la sesion SMPT
    return estado
    
    
    
    