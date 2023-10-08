#Librerias para el uso de correos
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart  import MIMEMultipart

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
        str: 'OK' si el correo se envió correctamente, de lo contrario, un mensaje de error.
    """
    
    
    destinatario = correo                               #Destinatario
    asunto = "Confirmacion de su registro a Hogwarts"   #Asunto del correo
    
    #Creacion del mensaje
    mensaje = MIMEMultipart()
    mensaje["From"]     = remitente     #El correo que envia el mensaje
    mensaje["To"]       = destinatario  #El correo a donde se envia el mensaje
    mensaje["Subject"]  = asunto        #El asunto del correo
    
    #Cuerpo del correo
    cuerpo = "Felicitaciones: " + nombre + "usted formara parte de Hogworts, bienvenido a: " + casa     #El cuerpo dl mensaje
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
    
    