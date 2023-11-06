from tkinter import *
from cryptography.fernet import Fernet
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import alumnos_interfaz
import profesor_interfaz
import modulo_compartido


import smtplib
import time


# La clave
clave_cifrado = b'd3iXJXBhYZ0ZasXWw_lIafJ3HyDHZoAmsD7ysmEbjtA='
fernet = Fernet(clave_cifrado)


intento = 0


def reportar_cuenta(nombre, apellido):
    # Guarda las cuentas que pueden ser bloqueadas
    pass


def enviar_correo(correo, clavepass):
    """Esta funcion es la que envia el correo con la contraseña que se ingreso en el registro de cuenta, recibe como parametro:
    1)Correo
    2)Password de la cuenta"""

    # Desencriptacion
    password_descifrado = fernet.decrypt(clavepass)
    password_descifrado_string = password_descifrado.decode('utf-8')

    # Correo
    # Desde el correo que vamos a enviar el mensaje
    remitente = "hogwartsesculademagia@gmail.com"
    password = "wksg icol fqnd hvif"

    try:
        destinatario = correo  # Destinatario
        asunto = "Recuperacion de su contraseña"  # Asunto del correo

        # Creacion del mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = remitente  # El correo que envia el mensaje
        mensaje["To"] = destinatario  # El correo a donde se envia el mensaje
        mensaje["Subject"] = asunto  # El asunto del correo

        # Cuerpo del correo
        cuerpo = "Usted acaba de tratar de recuperar su contraseña, su password es: " + \
            password_descifrado_string  # El cuerpo dl mensaje
        mensaje.attach(MIMEText(cuerpo, "plain"))  # El contenido del mensaje

        # Iniciar sesion en servidor SMTP de gmail
        # Especifica el Host y el puerto al cual conectar
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Hace la conecxion con el servidor SMPT y encripta la secion
        # Inisia secion en SMPT, con argumentos elusername y el password
        server.login(remitente, password)

        # Enviar mensaje
        texto = mensaje.as_string()  # Pasa todo el mensaje como texto
        server.sendmail(remitente, destinatario, texto)  # Envia el mensaje
        server.quit()  # Termino la sesion SMPT
        time.sleep(7)  # Espera 10seg
        return True

    except:
        smtplib.SMTPException
        return False


def recuperacion_password(roll, T_nom, T_ape, T_DPI, lienzo_recpass, lienzo_general, color):
    """Es la funcion que toma los datos de los campos de textos que revisa si existen y devuelve el password"""
    Texnom = T_nom.get() + "\n"
    Texape = T_ape.get() + "\n"
    Texdpi = T_DPI.get() + "\n"

    lista_ctdatos = []

    if roll == "estudiante":

        # Variables enteras
        posicionNomp = 0  # Posicion asociada al nombre
        posicionApep = 1  # Posicion asociada al apellido
        posiciondpi = 2  # Posicion del DPI
        posicioncorreo = 5  # Posicion del correo
        posicionpass = 6  # Posicion de la contraseña encriptada

        with open('Almacenado_todos.txt', 'r') as fp:
            datos = fp.readlines()
            for index, dato in enumerate(datos):
                # Guarda el nombre en una lista
                if index == posicionNomp:
                    posicionNomp += 7
                    lista_ctdatos.append(dato)

                # Guarda el apellido en una lista
                if index == posicionApep:
                    posicionApep += 7
                    lista_ctdatos.append(dato)

                # Guarda el password en la lista
                if index == posiciondpi:
                    posiciondpi += 7
                    lista_ctdatos.append(dato)

                if index == posicioncorreo:
                    posiciondpi += 7
                    lista_ctdatos.append(dato)

                if index == posicionpass:
                    posicionpass += 7
                    lista_ctdatos.append(dato)

        for index, clave in enumerate(lista_ctdatos):
            print(clave)
            print(Texnom)
            if clave == Texnom:  # Si se toma con el mismo nombre en los datos
                if lista_ctdatos[index+1] == Texape:
                    if lista_ctdatos[index+2] == Texdpi:
                        if enviar_correo(lista_ctdatos[index+3], lista_ctdatos[index+4]) == True:
                            lienzo_recpass.create_text(
                                300, 300, text="Se le envio un correo", fill="Black", font=("Arial", 14))
                            time.sleep(2)
                            return True
                        else:
                            lienzo_recpass.create_text(
                                300, 300, text="No encontramos su correo", fill="Black", font=("Arial", 14))
                            time.sleep(2)
                            return False
                    else:
                        lienzo_recpass.create_text(
                            300, 300, text="DPI no encontrado", fill="Black", font=("Arial", 14))
                        time.sleep(2)
                        return False
                else:
                    lienzo_recpass.create_text(
                        300, 300, text="Apellido no encontrado", fill="Black", font=("Arial", 14))
                    time.sleep(2)
                    return False
            else:
                lienzo_recpass.create_text(
                    300, 300, text="Nombre no encontrado", fill="Black", font=("Arial", 14))
                time.sleep(2)
                return False
    else:
        # Variables enteras
        posicionNomp = 0  # Posicion asociada al nombre
        posicionApep = 1  # Posicion asociada al apellido
        posiciondpi = 2  # Posicion del DPI
        posicionpass = 3  # Posicion de la contraseña
        with open('todos_profesores.txt', 'r') as fp:
            datos = fp.readlines()
            for index, dato in enumerate(datos):
                if index == posicionNomp:
                    posicionNomp += 4
                    lista_ctdatos.append(dato)
                if index == posicionApep:
                    posicionApep += 4
                    lista_ctdatos.append(dato)
                if index == posiciondpi:
                    posiciondpi += 4
                    lista_ctdatos.append(dato)
                if index == posicionpass:
                    posicionpass += 4
                    lista_ctdatos.append(dato)
        for index, clave in enumerate(lista_ctdatos):
            if clave == Texnom:  # Si se toma con el mismo nombre en los datos
                if lista_ctdatos[index+1] == Texape:
                    print(Texdpi)
                    print(lista_ctdatos[index+2])
                    if lista_ctdatos[index+2] == Texdpi:
                        lienzo_recpass.create_text(
                            300, 300, text="Su contraseña es: " + lista_ctdatos[index+3], fill="Black", font=("Arial", 14))
                        return True
        else:
            lienzo_recpass.create_text(
                300, 300, text="datos no encontrado", fill="Black", font=("Arial", 14))
            return False


def olvide_password(color, lienzo_estudiante, lienzo_profe, lienzo_general, roll):
    """Esta funcion es en el caso de que el profesor haya olvidado su contraseña recibe como parametro:
    1)Color
    2)Lienzo del bloque estudiante
    3)Lienzo del bloque de profesor
    4)Lienzo de toda la pantalla"""
    # Destruye el lienzo del bloque estudiante del profesor
    lienzo_estudiante.destroy()
    lienzo_profe.destroy()

    # El lienzo para recuperar contraseña
    lienzo_recpass = Canvas(lienzo_general, width=600, height=600, bg=color)
    lienzo_recpass.pack()
    lienzo_recpass.place(x=383, y=84)
    lienzo_recpass.create_text(
        342, 90, text="Recuperar password", fill="white", font=("Arial", 16))

    # Variables tipo StringVar
    T_nom = StringVar()
    T_ape = StringVar()
    T_dpi = StringVar()

    # Widgets
    # Pregunta etiqueta por el nombre
    etiqueta_nombre = Label(lienzo_recpass, text="nombre: ")
    etiqueta_nombre.pack()
    lienzo_recpass.create_window(150, 150, anchor=NW, window=etiqueta_nombre)

    # Pregunta etiqueta por el Apellido
    etiqueta_ape = Label(lienzo_recpass, text="apellido: ")
    etiqueta_ape.pack()
    lienzo_recpass.create_window(150, 350, anchor=NW, window=etiqueta_ape)

    # Pregunta etiqueta por el DPI
    etiqueta_dpi = Label(lienzo_recpass, text="DPI: ")
    etiqueta_dpi.pack()
    lienzo_recpass.create_window(150, 500, anchor=NW, window=etiqueta_dpi)

    # Campo de texto por el nombre
    entrada_nombre = Entry(lienzo_recpass, textvariable=T_nom)
    entrada_nombre.pack()
    lienzo_recpass.create_window(450, 150, anchor=NW, window=entrada_nombre)

    # Campo de texto por el apellido
    entrada_ape = Entry(lienzo_recpass, textvariable=T_ape)
    entrada_ape.pack()
    lienzo_recpass.create_window(450, 350, anchor=NW, window=entrada_ape)

    # Campo de texto por el DPI
    entrada_dpi = Entry(lienzo_recpass, textvariable=T_dpi)
    entrada_dpi.pack()
    lienzo_recpass.create_window(450, 500, anchor=NW, window=entrada_dpi)

    # Boton de obtener los datos para devolver la contraseña
    botonenvconf = Button(lienzo_recpass, text="Recuperar",  command=lambda: recuperacion_password(roll, T_nom, T_ape, T_dpi, lienzo_recpass,
                          lienzo_general, color), width=6, height=4)  # Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenvconf.place(x=550, y=0)
    botonenvconf.lift()


def comprobar(lista, nombre, apellido, password, n, palabra):
    """Esta funcion comprueba que existan esos datos en el documento y en caso de existir
    lleva a la interfaz y sino lo va contando
    y va bloqueando cuentas"""
    # Generar una clave de cifrado
    textnombre = nombre.get() + "\n"
    textapellido = apellido.get() + "\n"

    for index, dato in enumerate(lista):
        if dato == textnombre:
            if (lista[index+1] == textapellido):
                if palabra == "estudiante":
                    textpassword = password.get()
                    password_descifrado = fernet.decrypt(lista[index+n])
                    password_descifrado_string = password_descifrado.decode(
                        'utf-8')
                    if (password_descifrado_string == textpassword):
                        return True
                else:
                    textpassword = password.get() + "\n"
                    if (lista[index+n] == textpassword):
                        return True
    else:
        print("False")
        return False


profesor_ver = False  # Mala práctica :/
alumno_ver = False  # Mala práctica :/


def entrada(lienzo_estudiante, lienzo_profesor, lienzo_general, color, nombre):
    global profesor_ver
    global alumno_ver

    lienzo_estudiante.destroy()
    lienzo_profesor.destroy()
    lienzo_interfaz = Canvas(lienzo_general, width=1408, height=708, bg=color)
    lienzo_interfaz.pack()
    lienzo_interfaz.place(x=60, y=40)

    nombre_ingreso = nombre.get()
    modulo_compartido.nombre_ingreso = nombre_ingreso

    if alumno_ver == True:
        # Aquí se llama a la función que contiene todo el código de alumnos
        modulo_compartido.funcion_alumnos(lienzo_interfaz, color)
    elif profesor_ver == True:
        # Aquí se llama a la función que contiene todo el código de profesor
        modulo_compartido.funcion_profesor(lienzo_interfaz, color)
    else:
        print("Error en el inicio de sesión")

    # lienzo_de_entrada = Canvas(lienzo_general, width=600, height=600, bg=color)
    # lienzo_de_entrada.pack()
    # lienzo_de_entrada.place(x=383, y=84)
    # lienzo_de_entrada.create_text(
    #     342, 90, text="Bienvenido", fill="white", font=("Arial", 16))
    # lienzo_de_entrada.create_text(
    #     342, 300, text=nombre_ingreso, fill="white", font=("Arial", 18))


def divide_listas_profesor(lienzo_general, lienzo_estudiante,  lienzo_profesor, color, nombre, apellido, password):
    global profesor_ver
    """Esta funcion toma el archivo donde estan todos  los estudiantes y lo va subdividiendo en listas
    para enviar a la funcion que comprueba que existan los datos que coloca en los campos de entrada:"""
    # Listas vacias
    lista_identidad = []  # Guarda el nombre y el apellido
    global intento

    # Variables enteras
    posicionNomp = 0  # Posicion asociada al nombre
    posicionApep = 1  # Posicion asociada al apellido
    posicionpasswordp = 3  # Posicion de la contraseña encriptada

    with open('todos_profesores.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            # Guarda el nombre en una lista
            if index == posicionNomp:
                posicionNomp += 4
                lista_identidad.append(dato)

            # Guarda el apellido en una lista
            if index == posicionApep:
                posicionApep += 4
                lista_identidad.append(dato)

            # Guarda el password en la lista
            if index == posicionpasswordp:
                posicionpasswordp += 4
                lista_identidad.append(dato)

    if comprobar(lista_identidad, nombre, apellido, password, 2, "Profesor") == True:
        profesor_ver = True
        entrada(lienzo_estudiante, lienzo_profesor,
                lienzo_general, color, nombre)
        print("El profesor entro a su portal")
    else:
        intento += 1
        if intento == 3:
            # Aqui se van a guardar las cuentas que hay que bloquear
            print("Al profesor se le va bloquear su cuenta")
            reportar_cuenta(nombre, apellido)
            roles(lienzo_general, color)
        else:
            roles(lienzo_general, color)


def divide_listas_estudiante(lienzo_general, lienzo_profesor, lienzo_estudiante, color, nombre, apellido, password):
    global alumno_ver
    """Esta funcion toma el archivo donde estan todos  los estudiantes y lo va subdividiendo en listas
    para enviar a la funcion que comprueba que existan los datos que coloca en los campos de entrada:"""
    # Listas vacias
    lista_identidad = []  # Guarda el nombre y el apellido
    global intento

    # Variables enteras
    posicionNom = 0  # Posicion asociada al nombre
    posicionApe = 1  # Posicion asociada al apellido
    posicionCorreo = 5  # Posicion asociada al correo del estudiante
    posicionpassword = 6  # Posicion de la contraseña encriptada

    with open('Almacenado_todos.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            # Guarda el nombre en una lista
            if index == posicionNom:
                posicionNom += 7
                lista_identidad.append(dato)

            # Guarda el apellido en una lista
            if index == posicionApe:
                posicionApe += 7
                lista_identidad.append(dato)

            # Guarda el numero de correo en una lista
            if index == posicionCorreo:
                posicionCorreo += 7
                lista_identidad.append(dato)

            # Guarda el password en una lista
            if index == posicionpassword:
                posicionpassword += 7
                lista_identidad.append(dato)

    if comprobar(lista_identidad, nombre, apellido, password, 3, "estudiante") == True:
        alumno_ver = True
        entrada(lienzo_estudiante, lienzo_profesor,
                lienzo_general, color, nombre)
        print("El estudiante entro a su clase ")
    else:
        intento += 1
        if intento == 3:
            # Aqui se van a guardar las cuentas que hay que bloquear
            print("Al estudiante se le va reportar su cuenta")
            reportar_cuenta(nombre, apellido)

            roles(lienzo_general, color)
        else:
            roles(lienzo_general, color)


def roles(lienzo_general, color):
    """En la funcion se crean los paneles para seleccionar el rol de alumno y el de profesor
    y recibe como argumento de la funcion el lienzo"""
    # El lienzo donde se trabaja las opciones para que se registre el profesor
    lienzo_eleccion_profe = Canvas(
        lienzo_general, width=600, height=600, bg=color)
    lienzo_eleccion_profe.pack()
    lienzo_eleccion_profe.place(x=42, y=84)
    lienzo_eleccion_profe.create_text(
        342, 90, text="Profesor", fill="white", font=("Arial", 16))

    # El lienzo donde se trabaja las opciones de estudiante
    lienzo_eleccion_estudiante = Canvas(
        lienzo_general, width=600, height=600, bg=color)
    lienzo_eleccion_estudiante.pack()
    lienzo_eleccion_estudiante.place(x=725, y=84)
    lienzo_eleccion_estudiante.create_text(
        342, 90, text="Estudiante", fill="white", font=("Arial", 16))

    # Variables tipo string
    # Para el uso de widgets en el lienzo de estudiantes
    texto_nombre_e = StringVar()
    texto_apellido_e = StringVar()
    texto_password_e = StringVar()

    # Para el uso de widgets en el lienzo de profesor
    texto_nombre_p = StringVar()
    texto_apellido_p = StringVar()
    texto_password_p = StringVar()

    # Etiquetas del lienzo de profesores
    # Usuario
    etiqueta_username = Label(lienzo_general, text="Username: ")
    etiqueta_username.pack()
    lienzo_eleccion_profe.create_window(
        150, 150, anchor=NW, window=etiqueta_username)

    # Apellido
    etiqueta_apellido = Label(lienzo_general, text="Apellido: ")
    etiqueta_apellido.pack()
    lienzo_eleccion_profe.create_window(
        150, 350, anchor=NW, window=etiqueta_apellido)

    # Contraseña
    etiqueta_password = Label(lienzo_general, text="Password: ")
    etiqueta_password.pack()
    lienzo_eleccion_profe.create_window(
        150, 500, anchor=NW, window=etiqueta_password)

    # Etiquetas del lienzo de estudiantes
    # Usuario
    etiqueta_username_e = Label(lienzo_general, text="Username: ")
    etiqueta_username_e.pack()
    lienzo_eleccion_estudiante.create_window(
        150, 150, anchor=NW, window=etiqueta_username_e)

    # Apellido
    etiqueta_apellido_e = Label(lienzo_general, text="Apellido: ")
    etiqueta_apellido_e.pack()
    lienzo_eleccion_estudiante.create_window(
        150, 350, anchor=NW, window=etiqueta_apellido_e)

    # Contraseña
    etiqueta_password_e = Label(lienzo_general, text="Password: ")
    etiqueta_password_e.pack()
    lienzo_eleccion_estudiante.create_window(
        150, 500, anchor=NW, window=etiqueta_password_e)

    # Campo de texto de profesores
    # Nombre
    entrada_username_p = Entry(lienzo_general, textvariable=texto_nombre_p)
    entrada_username_p.pack()
    lienzo_eleccion_profe.create_window(
        450, 150, anchor=NW, window=entrada_username_p)

    # Apellido
    entrada_apellido_p = Entry(lienzo_general, textvariable=texto_apellido_p)
    entrada_apellido_p.pack()
    lienzo_eleccion_profe.create_window(
        450, 350, anchor=NW, window=entrada_apellido_p)

    # Contraseña
    entrada_password_p = Entry(lienzo_general, textvariable=texto_password_p)
    entrada_password_p.pack()
    lienzo_eleccion_profe.create_window(
        450, 500, anchor=NW, window=entrada_password_p)

    # Campo de texto de estudiantes
    # Nombre
    entrada_username_e = Entry(lienzo_general, textvariable=texto_nombre_e)
    entrada_username_e.pack()
    lienzo_eleccion_estudiante.create_window(
        450, 150, anchor=NW, window=entrada_username_e)

    # Apellido
    entrada_apellido_e = Entry(lienzo_general, textvariable=texto_apellido_e)
    entrada_apellido_e.pack()
    lienzo_eleccion_estudiante.create_window(
        450, 350, anchor=NW, window=entrada_apellido_e)

    # Contraseña
    entrada_password_e = Entry(lienzo_general, textvariable=texto_password_e)
    entrada_password_e.pack()
    lienzo_eleccion_estudiante.create_window(
        450, 500, anchor=NW, window=entrada_password_e)

    # Botones
    # Boton que envia los datos de profesor
    botonenvp = Button(lienzo_eleccion_profe, text="Entrar",  command=lambda: divide_listas_profesor(lienzo_general, lienzo_eleccion_estudiante, lienzo_eleccion_profe,   color,
                       texto_nombre_p, texto_apellido_p, texto_password_p), width=6, height=4)  # Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenvp.place(x=550, y=0)
    botonenvp.lift()

    # Boton que envia los datos de estudiante
    botonenve = Button(lienzo_eleccion_estudiante, text="Entrar", command=lambda: divide_listas_estudiante(lienzo_general, lienzo_eleccion_estudiante, lienzo_eleccion_profe, color,
                       texto_nombre_e, texto_apellido_e, texto_password_e), width=6, height=4)  # Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenve.place(x=550, y=0)
    botonenve.lift()

    # Boton de se me olvio la contraseña de estudiante
    botonenve = Button(lienzo_eleccion_estudiante, text="olvide el password", command=lambda: olvide_password(color, lienzo_eleccion_estudiante, lienzo_eleccion_profe,
                       lienzo_general, "estudiante"), width=20, height=3)  # Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenve.place(x=0, y=550)
    botonenve.lift()

    # Boton de se me olvio la contraseña del profesot
    botonenve = Button(lienzo_eleccion_profe, text="olvide el password", command=lambda: olvide_password(color, lienzo_eleccion_estudiante, lienzo_eleccion_profe,
                       lienzo_general, "profesor"), width=20, height=3)  # Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenve.place(x=0, y=550)
    botonenve.lift()
