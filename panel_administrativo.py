from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import sys
import time
import base64
import io
from email.mime.text import MIMEText
from email.mime.multipart  import MIMEMultipart

import smtplib
import time


remitente = "hogwartsesculademagia@gmail.com"   #Desde el correo que vamos a enviar el mensaje
password = "wksg icol fqnd hvif" 

def cambiar_password(entrada_n1, entrada_n2, frame, lienzo):
    """La funcion que guarda la nueva contraseña"""
    texto1 = entrada_n1.get()
    texto2 = entrada_n2.get()
    if (texto1 == texto2 ):
        with open('usuario_password_admin.txt', 'w') as fp:
            fp.write("administracion\n")
            fp.write(texto2)
    else:
        cambio_password(frame, lienzo)
        
def accion_desbloqueo(opiden):
    """Esta funcion es la que maneja la logica del desbloqueo de cuentas """
    #Obtiene el nombre y el apellido de la cuenta reportada
    usuario = opiden.get()
    print("Banderin: 1")
    print(usuario)
    palabras = usuario.split()
    nombre = palabras[0]+ "X"
    print(nombre)
    apellido = palabras[1]+ "X"
    print(apellido)
    
    #Listas
    lista_antes       = []
    lista_durante     = []
    lista_despues     = []
    lista_durante_cam = []
    lista_editada     = []
    
    lista_antes_G       = []
    lista_durante_G     = []
    lista_despues_G    = []
    lista_editada_G     = []
    
    puntero = 0
    correo  = "Vacio"
    
    #Busca en la lista donde estan todos los usuarios
    with open('Almacenado_todos.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if dato==nombre and datos[index+1]==apellido:
                puntero = index
                break
    #Divide en 3 bloques el documento el que esta antes, el que tiene el nombre y el apellido y el que esta despues       
    with open('Almacenado_todos.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if index<puntero:
                lista_antes.append(dato.strip() + "\n")
            elif puntero<=index<=puntero+1:
                lista_durante.append(dato.strip() + "\n")
            else:
                lista_despues.append(dato)
    
    #al nombre y el apellido le borra el ultimo caracter
    for index, dato in enumerate(lista_durante):
        palabrasG = dato[:-2].split(":")
        lista_durante_cam.append(palabrasG[0]+"\n")
        
    #Rescribe documento donde estan todas las cuentas
    lista_editada = lista_antes + lista_durante_cam +lista_despues
    with open('Almacenado_todos.txt', 'w') as fp:
        for index, dato in enumerate(lista_editada):
            fp.write(dato.strip()+'\n') 
    
    #Borra la cuenta de los reportes 
    with open('todos_reportados.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if dato==nombre and datos[index+1]==apellido:
                puntero = index
            if index<puntero:
                lista_antes_G.append(dato.strip() + "\n")
            elif puntero<=index<=puntero+1:
                lista_durante_G.append(dato.strip() + "\n")
            else:
                lista_despues_G.append(dato)
            
        lista_editada_G = lista_antes_G +lista_despues_G
        with open('todos_reportados.txt', 'w') as fp:
            for index, dato in enumerate(lista_editada_G):
                fp.write(dato.strip()+'\n')
    
    #Busca el correo
    with open('Almacenado_todos.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if dato.strip() == palabras[0] and datos[index+1].strip() == palabras[1]:
                correo = datos[index+5]
                print(correo)
                
    ##########Envia correo######################################
    print(correo)
    try:
        destinatario = correo                               #Destinatario
        asunto = "Recuperacion de su cuenta"   #Asunto del correo
                        
        #Creacion del mensaje
        mensaje = MIMEMultipart()
        mensaje["From"]     = remitente     #El correo que envia el mensaje
        mensaje["To"]       = destinatario  #El correo a donde se envia el mensaje
        mensaje["Subject"]  = asunto        #El asunto del correo
                        
        #Cuerpo del correo
        cuerpo = "Su cuenta ha sido restablecida por el administrador, tenga mas cuidado, en caso de no recordar su password puede hacerlo con el boton 'Olvide mi password'"   #El cuerpo de mensaje
        mensaje.attach(MIMEText(cuerpo, "plain"))       #El contenido del mensaje
                        
        #Iniciar sesion en servidor SMTP de gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)    #Especifica el Host y el puerto al cual conectar
        server.starttls()                               #Hace la conecxion con el servidor SMPT y encripta la secion
        server.login(remitente, password)               #Inisia secion en SMPT, con argumentos elusername y el password 
                        
        #Enviar mensaje
        texto = mensaje.as_string()                                 #Pasa todo el mensaje como texto
        server.sendmail(remitente, destinatario, texto)    #Envia el mensaje
        server.quit()              #Termino la sesion SMPT 
        time.sleep(4)              #Espera 5seg
                        #return True
    except:
        smtplib.SMTPException
                
    
#!Trabajar en esta funcion para desbloquear las cuentas 
def desbloqueo_cuentas(frame_administracion, lienzo_desbloqueo):
    """Esta funcion que tiene el control de desbloquear la cuenta"""
    #Obtiene una lista con la identidad de las cuentas reportadas
    lista_pre_identidad = []
    lista_identidad = []
    opiden = StringVar()
    posiden = 0
    with open('todos_reportados.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if index==posiden and dato.strip():
                posiden+=2
                lista_pre_identidad.append(dato.strip())
                
    if not lista_pre_identidad:
        # Crea una etiqueta para indicar que no hay ningun reportado
        nueva_password = Label(lienzo_desbloqueo, text="No hay cuentas bloqueadas: ")
        nueva_password.pack()
        lienzo_desbloqueo.create_window(50, 50, anchor = NW, window = nueva_password)
    
    else:
        posiden = 0
        print("Banderin 0")
        with open('todos_reportados.txt', 'r') as fp:
            datos = fp.readlines()
            for index, dato in enumerate(datos):
                if index==posiden:
                    print(index)
                    posiden+=2
                    print(dato)
                    print(datos[index+1])
                    lista_identidad.append(dato.strip() + " " + datos[index+1])
        print(lista_identidad)
            
        #Crear un menu desplegable para la eleccion de alumno a desbloquear
        menu = OptionMenu(lienzo_desbloqueo, opiden, *lista_identidad)
        menu.pack()
        menu.place(x=160, y=80)
        
        #El boton que envia una accion para la logica del desbloqueo de cuentas
        botonmostrar = Button(lienzo_desbloqueo, text="Desbloquear", command = lambda: accion_desbloqueo(opiden), width=8, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
        botonmostrar.place(x=0, y=135)
        botonmostrar.lift()
    
    
    
def mostrar_password(entrada1, entrada2, boton):
    """La funcion que pasa la contraseña visible a **** o de **** a visible"""
    #Si la contraseña no esta visible
    if entrada1['show'] == '*':
        entrada1.config(show = '')        #La hace visible
        entrada2.config(show = '')       
        boton.config(text='Ocultar')      #Cambia el texto del boton de ocultar
    #Si la contraseña es visible
    else:
        entrada1.config(show = '*')     #La oculta 
        entrada2.config(show = '*')          
        boton.config(text='Mostrar')    #Cambia el texto del boton a mostrar

def cambio_password(frame, lienzo):
    new_password = StringVar()
    new_password2 = StringVar()
    
    #Contraseña:
    #Etiqueta
    nueva_password = Label(frame, text="Password: ")
    nueva_password.pack()
    lienzo.create_window(50, 50, anchor = NW, window = nueva_password)
        
    #Campo de texto
    entrada_np = Entry(frame, textvariable = new_password, show = "*")
    entrada_np.pack()
    lienzo.create_window(200, 50, anchor = NW, window = entrada_np)
    
    #Confirmacion 
    #Etiqueta
    confirmacion = Label(frame, text="Confirmacion: ")
    confirmacion.pack()
    lienzo.create_window(50, 100, anchor = NW, window = confirmacion)
        
    #Campo de texto
    entrada_cnp = Entry(frame, textvariable = new_password2, show = "*")
    entrada_cnp.pack()
    lienzo.create_window(200, 100, anchor = NW, window = entrada_cnp)
    
    #Boton de mostrar y ocultar la contraseña
    botonmostrar = Button(lienzo, text="mostrar", command  = lambda: mostrar_password(entrada_np, entrada_cnp, botonmostrar), width=5, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonmostrar.place(x=0, y=135)
    botonmostrar.lift()
    
    
    #Boton de cambiar password
    botonchange = Button(lienzo, text="Cambiar", command = lambda: cambiar_password(new_password, new_password2, frame, lienzo), width=5, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonchange.place(x=360, y=135)
    botonchange.lift()
    

def reporte_notas():
    #La funcion que da los reportes de las notas de los estudiantes de determinado curso
    
    pass

def registrar_profesor(entrada_nombre, entrada_apellido, entrada_DPI, entrada_password, entrada_confirpass, lienzo_administrar_profesor, frame_administracion):
    """La funcion que si el password concuerda con la confirmacion lo guarda en un documento txt los argumentos
    son variables tipo StrinVar que estan en el texvariable en los campos de textos:
    1) Entrada de nombre
    2) Entrada de apellido
    3) Entrada de DPI
    4) Entrada de password
    5) Entrada de confirmacion
    Si la concueradan escribe una etiqueta de registrado y sino de error en contraseñas pero en ambas regresa a la escritura de datos"""
    #Obtiene el valor escrito en el campo de texto
    textnom        =  entrada_nombre.get()
    textapellido   =  entrada_apellido.get()
    textdpi        =  entrada_DPI.get()
    textpassword   =  entrada_password.get()
    textconfirpass  = entrada_confirpass.get()
    
    
    lienzo_administrar_profesor.destroy()
    
    #)Crea el lienzo de administracion de profesores
    lienzo_administrar_profesor = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_administrar_profesor.pack()
    lienzo_administrar_profesor.place(x=916, y=284)
    lienzo_administrar_profesor.create_text(200, 30, text = "Guardando...", fill="white", font=("Arial", 16))
    
    if textpassword == textconfirpass:
        with open('todos_profesores.txt', 'a') as fp:
            fp.write(textnom + '\n')
            fp.write(textapellido + '\n')
            fp.write(textdpi + '\n')
            fp.write(textpassword + '\n')
        
        lienzo_administrar_profesor.destroy()  
        nuevo_lienzo_administrar = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
        nuevo_lienzo_administrar.pack()
        nuevo_lienzo_administrar.place(x=916, y=284)
        nuevo_lienzo_administrar.create_text(200, 30, text = "Registrando", fill="white", font=("Arial", 16))
        nuevo_lienzo_administrar.create_text(200, 100, text = "Guardado...", fill="white", font=("Arial", 12))
        
        botonuevo = Button(nuevo_lienzo_administrar, text="nuevo profesor", command  = lambda: registra_profesor(nuevo_lienzo_administrar, frame_administracion), width=15, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
        botonuevo.place(x=170, y=150)
        botonuevo.lift()
        
        
    else:
        lienzo_administrar_profesor.destroy()  
        nuevo_lienzo_administrar = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
        nuevo_lienzo_administrar.pack()
        nuevo_lienzo_administrar.place(x=916, y=284)
        nuevo_lienzo_administrar.create_text(200, 30, text = "Registrando", fill="white", font=("Arial", 16))
        nuevo_lienzo_administrar.create_text(200, 100, text = "Error de password...", fill="white", font=("Arial", 12))
        
        botonuevo = Button(nuevo_lienzo_administrar, text="Intentar de nuevo", command  = lambda: registra_profesor(nuevo_lienzo_administrar, frame_administracion), width=15, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
        botonuevo.place(x=170, y=150)
        botonuevo.lift()  


def registra_profesor(lienzo_administrar_profesor, frame_administracion):
    """La funcion que registra los datos del nuevo profesor recibe como argumentos:
    1) lienzo
    2) El frame y coloca en el lienzo de administrar profesor el campo de:
    1) Nombre
    2) Apellido
    3) DPI
    4)Contraseña
    5) Confirmacion de la contraseña"""
    lienzo_administrar_profesor.destroy()
    
    #)Crea el lienzo de administracion de profesores
    lienzo_administrar_profesor = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_administrar_profesor.pack()
    lienzo_administrar_profesor.place(x=916, y=284)
    lienzo_administrar_profesor.create_text(200, 30, text = "Registrar a nuevo profesor", fill="white", font=("Arial", 16))


    #Variables tipor StringVar()
    entrada_nombre     = StringVar()
    entrada_apellido   = StringVar()
    entrada_DPI        = StringVar()
    entrada_password   = StringVar()
    entrada_confirpass = StringVar()
    
    #Etiquetas
    #Nombre
    etiqueta_namep = Label(frame_administracion, text="nombre: ")
    etiqueta_namep.pack()
    lienzo_administrar_profesor.create_window(100, 45, anchor = NW, window = etiqueta_namep)
    
    #Apellido
    etiqueta_apellidop = Label(frame_administracion, text="apellido: ")
    etiqueta_apellidop.pack()
    lienzo_administrar_profesor.create_window(100, 80, anchor = NW, window = etiqueta_apellidop)
    
    #DPI
    etiqueta_DPIP = Label(frame_administracion, text="DPI: ")
    etiqueta_DPIP.pack()
    lienzo_administrar_profesor.create_window(100, 115, anchor = NW, window = etiqueta_DPIP)
    
    #Contraseña
    etiqueta_passwordp = Label(frame_administracion, text="password: ")
    etiqueta_passwordp.pack()
    lienzo_administrar_profesor.create_window(100, 150, anchor = NW, window = etiqueta_passwordp)
    
    #Confirmacion
    etiqueta_confirmacionp = Label(frame_administracion, text="confirmacion: ")
    etiqueta_confirmacionp.pack()
    lienzo_administrar_profesor.create_window(100, 185, anchor = NW, window = etiqueta_confirmacionp)
    
        
    #Campo de texto
    #Nombre
    campo_namep= Entry(frame_administracion, textvariable = entrada_nombre)
    campo_namep.pack()
    lienzo_administrar_profesor.create_window(200, 45, anchor = NW, window = campo_namep)
    
    #Apellido
    campo_apellidop= Entry(frame_administracion, textvariable = entrada_apellido)
    campo_apellidop.pack()
    lienzo_administrar_profesor.create_window(200, 80, anchor = NW, window = campo_apellidop)
    
    #DPI
    campo_DPIP= Entry(frame_administracion, textvariable = entrada_DPI)
    campo_DPIP.pack()
    lienzo_administrar_profesor.create_window(200, 115, anchor = NW, window = campo_DPIP)
    
    #Password
    campo_passwordp= Entry(frame_administracion, textvariable = entrada_password, show='*')
    campo_passwordp.pack()
    lienzo_administrar_profesor.create_window(200, 150, anchor = NW, window = campo_passwordp)
    
    #Confirmacion
    campo_confirmacionp= Entry(frame_administracion, textvariable = entrada_confirpass, show='*')
    campo_confirmacionp.pack()
    lienzo_administrar_profesor.create_window(200, 185, anchor = NW, window = campo_confirmacionp)
    
    
    botonregistrar = Button(lienzo_administrar_profesor, text="Registrar", command  = lambda: registrar_profesor(entrada_nombre, entrada_apellido, entrada_DPI, entrada_password, entrada_confirpass, lienzo_administrar_profesor, frame_administracion), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonregistrar.place(x=0, y=150)
    botonregistrar.lift()
    
    botonmostrar = Button(lienzo_administrar_profesor, text="mostrar", command  = lambda: mostrar_password(campo_passwordp, campo_confirmacionp, botonmostrar), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonmostrar.place(x=360, y=150)
    botonmostrar.lift()
    

def listado_profesores(lienzo_administrar_profesor, frame_administracion):
    """La funcion que ve el listado de los profesores """
    lienzo_administrar_profesor.destroy()
    
    lista_nombres_profes = []
    opnom = StringVar()
    posicionomp = 0
    
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_listado = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_listado.pack()
    lienzo_listado.place(x=916, y=284)
    lienzo_listado.create_text(200, 30, text="Listado de profesores", fill="white", font=("Arial", 20))
    
    
    with open('todos_profesores.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if index == posicionomp:
                posicionomp += 4
                lista_nombres_profes.append(dato.strip())
                
    
    menu = OptionMenu(lienzo_listado, opnom, *lista_nombres_profes)
    menu.pack()
    menu.place(x=160, y=80)
    
    
def guardar_edicion(lista_antes, lista_despues, new_nombre, new_apellido, new_dpi, new_password, lienzo_administra_profesor, frame_administracion):
    """Esta funcion es la que rescribe los datos en el documento con la edicion guardada"""
    lista_durante = []
    lista_total = []
    nombre = new_nombre.get()
    apellido = new_apellido.get()
    dpi = new_dpi.get()
    password = new_password.get()
    print("Lista: ")
    lista_durante.append(nombre)
    lista_durante.append(apellido)
    lista_durante.append(dpi)
    lista_durante.append(password)
    print(lista_durante)
    
    lista_total = lista_antes + lista_durante + lista_despues
    
    #Todo: Escritura
    # Abre el archivo en modo append
    with open("todos_profesores.txt", "w") as archivo:
        # Agrega valores en el archivo de forma vertical
        for dato in lista_total:
            archivo.write(dato + '\n')
            
    lienzo_administra_profesor.destroy()
    #Crea el lienzo de administracion de profesores
    new_lienzo_editprof = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    new_lienzo_editprof.pack()
    new_lienzo_editprof.place(x=916, y=284)
    new_lienzo_editprof.create_text(200, 30, text="Guardando...", fill="white", font=("Arial", 20))
    

def panel_mostrar_datos(lista_antes, lista_durante, lista_despues, lienzo_administrar_profesor, frame_administracion):
    """Aqui se muestan los widgerst para modificar los datos de un profesor y el boton que cambia los datos"""
    lienzo_administrar_profesor.destroy()
    
    #Variables tipor StringVar()
    entrada_nombre     = StringVar()
    entrada_apellido   = StringVar()
    entrada_DPI        = StringVar()
    entrada_password   = StringVar()
    print(lista_durante)
    
    entrada_nombre.set(lista_durante[0])
    entrada_apellido.set(lista_durante[1])
    entrada_DPI.set(lista_durante[2])
    entrada_password.set(lista_durante[3])
    
    #4)Crea el lienzo de administracion de profesores
    new_lienzo_editprof = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    new_lienzo_editprof.pack()
    new_lienzo_editprof.place(x=916, y=284)
    new_lienzo_editprof.create_text(200, 30, text="Editar profesores", fill="white", font=("Arial", 20))
    
    #Etiquetas
    #Nombre
    etiqueta_namep = Label(new_lienzo_editprof, text="nombre: ")
    etiqueta_namep.pack()
    new_lienzo_editprof.create_window(100, 45, anchor = NW, window = etiqueta_namep)
    
    #Apellido
    etiqueta_apellidop = Label(new_lienzo_editprof, text="apellido: ")
    etiqueta_apellidop.pack()
    new_lienzo_editprof.create_window(100, 80, anchor = NW, window = etiqueta_apellidop)
    
    #DPI
    etiqueta_DPIP = Label(new_lienzo_editprof, text="DPI: ")
    etiqueta_DPIP.pack()
    new_lienzo_editprof.create_window(100, 115, anchor = NW, window = etiqueta_DPIP)
    
    #Contraseña
    etiqueta_passwordp = Label(new_lienzo_editprof, text="password: ")
    etiqueta_passwordp.pack()
    new_lienzo_editprof.create_window(100, 150, anchor = NW, window = etiqueta_passwordp)
    
    #Campo de texto
    #Nombre
    campo_namep= Entry(new_lienzo_editprof, textvariable = entrada_nombre)
    campo_namep.pack()
    new_lienzo_editprof.create_window(200, 45, anchor = NW, window = campo_namep)
    
    #Apellido
    campo_apellidop= Entry(new_lienzo_editprof, textvariable = entrada_apellido)
    campo_apellidop.pack()
    new_lienzo_editprof.create_window(200, 80, anchor = NW, window = campo_apellidop)
    
    #DPI
    campo_DPIP= Entry(new_lienzo_editprof, textvariable = entrada_DPI)
    campo_DPIP.pack()
    new_lienzo_editprof.create_window(200, 115, anchor = NW, window = campo_DPIP)
    
    #Password
    campo_passwordp = Entry(new_lienzo_editprof, textvariable = entrada_password)
    campo_passwordp.pack()
    new_lienzo_editprof.create_window(200, 150, anchor = NW, window = campo_passwordp)
    
    botonmostrar = Button(new_lienzo_editprof, text="Guardad", command  = lambda: guardar_edicion(lista_antes, lista_despues, entrada_nombre, entrada_apellido, entrada_DPI, entrada_password, lienzo_administrar_profesor, frame_administracion), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonmostrar.place(x=360, y=150)
    botonmostrar.lift()
    
    
def editar_divide(clave_dpi, lienzo_administrar_profesor, frame_administracion):
    limite_inferior = 0
    limite_superior = 0
    busqueda_dpi = clave_dpi.get()
    lista_todos = []
    lista_antes = []
    lista_durante = []
    lista_despues = []
    
    #Variables enteras
    posicionomp    = 0         #Posicion asociada al nombre
    posicionappe   = 1         #Posicion asociada al apellido
    posiciondpi    = 2         #Posicion del DPI
    posicionpass   = 3         #Posicion del password
    
    
    #Lee el archivo y guarda el nombre y el DPI de todos los profesores
    with open('todos_profesores.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if index == posicionomp:
                posicionomp += 4
                lista_todos.append(dato.strip())
            if index == posicionappe:
                posicionappe += 4
                lista_todos.append(dato.strip())
            if index == posiciondpi:
                posiciondpi += 4
                lista_todos.append(dato.strip())
            if index == posicionpass:
                posicionpass += 4
                lista_todos.append(dato.strip())
                
    #Crea una lista con solo los DPI que tiene el mismo nombre que el paso anterior
    for index, clave in enumerate(lista_todos):
        if clave == busqueda_dpi:
            limite_inferior = index+1           #Password
            limite_superior = index-2           #Nombre    
    #Lee el archivo y lo divide en tres secciones el antes, los datos y el despues de la modificacion
    with open('todos_profesores.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(lista_todos):
            if index < limite_superior:
                lista_antes.append(dato.strip())
            elif limite_superior <= index <= limite_inferior:
                lista_durante.append(dato.strip())
            else:
                lista_despues.append(dato.strip())
                
    panel_mostrar_datos(lista_antes, lista_durante, lista_despues, lienzo_administrar_profesor, frame_administracion)
                
    
def muestra_busca(variable_nombre, lienzo_administrar_profesor, frame_administracion):
    clave_nombre = variable_nombre.get()            #Obtiene el valor del menu(nombre del profesor)
    lista_datos_profes = []                         #Guarda el nombre de todos los profesores y su DPI
    lista_dpi_profes = []                           #Guarda solo el DPI
    opdpi = StringVar()                             #Guarda el valor del menu del DPI
    #Variables enteras
    posicionNomp   = 0         #Posicion asociada al nombre
    posiciondpi    = 2         #Posicion del DPI
    #Lee el archivo y guarda el nombre y el DPI de todos los profesores
    with open('todos_profesores.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if index == posicionNomp:
                posicionNomp += 4
                lista_datos_profes.append(dato.strip())
            if index == posiciondpi:
                posiciondpi += 4
                lista_datos_profes.append(dato.strip())
                
    #Crea una lista con solo los DPI que tiene el mismo nombre que el paso anterior
    for index, clave in enumerate(lista_datos_profes):
        if clave == clave_nombre:
            lista_dpi_profes.append(lista_datos_profes[index+1])
            
    
    lienzo_administrar_profesor.destroy()                   #Destruye el lienzo
    #Crea el lienzo de administracion de profesores
    new_lienzo_adminiprof = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    new_lienzo_adminiprof.pack()
    new_lienzo_adminiprof.place(x=916, y=284)
    new_lienzo_adminiprof.create_text(200, 30, text="Buscando DPI con esos datos...", fill="white", font=("Arial", 12))
    
    #Crea el menu opciones solo con los DPI        
    menu = OptionMenu(new_lienzo_adminiprof, opdpi, *lista_dpi_profes)
    menu.pack()
    menu.place(x=160, y=80)
    
    #El boton para editar el perfil con ese DPI
    botonmostrarbuscar = Button(new_lienzo_adminiprof, text="Editar", command = lambda: editar_divide(opdpi, lienzo_administrar_profesor, frame_administracion), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonmostrarbuscar.place(x=160, y=150)
    botonmostrarbuscar.lift()
    
    
def editar_profesor(lienzo_administrar_profesor, frame_administracion):
    """La funcion que edita el profesor"""
    lienzo_administrar_profesor.destroy()
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_administrar_profesor = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_administrar_profesor.pack()
    lienzo_administrar_profesor.place(x=916, y=284)
    lienzo_administrar_profesor.create_text(200, 30, text="Editar profesor", fill="white", font=("Arial", 20))
    
    opnom = StringVar()
    posicionomp = 0
    
    lista_nombres_profes = []
    
    with open('todos_profesores.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if index == posicionomp:
                posicionomp += 4
                lista_nombres_profes.append(dato.strip())
                
    
    menu = OptionMenu(lienzo_administrar_profesor, opnom, *lista_nombres_profes)
    menu.pack()
    menu.place(x=160, y=80)
    
    botonmostrarbuscar = Button(lienzo_administrar_profesor, text="Buscar DPI", command  = lambda: muestra_busca(opnom, lienzo_administrar_profesor, frame_administracion), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonmostrarbuscar.place(x=160, y=150)
    botonmostrarbuscar.lift()
    
    

def administracion_profesores(frame_administracion, lienzo_administrar_profesor):
    """La funcion que administra los profesores es decir: 
    1) Envia al registro de nuevos profesores
    2) Ve el listado de profesores
    3) Edita los datos de un profesor especificos.
    Los parametros de la funcion son:
    1) frame
    2) El lienzo"""
    #Boton que registra los nuevos profesores
    botonregistra = Button(lienzo_administrar_profesor, text="Registrar", command  = lambda: registra_profesor(lienzo_administrar_profesor, frame_administracion), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonregistra.place(x=67, y=100)
    botonregistra.lift()
    
    #Boton que ve el listado de los profesores
    botonlistado = Button(lienzo_administrar_profesor, text="listado", command  = lambda: listado_profesores(lienzo_administrar_profesor, frame_administracion), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonlistado.place(x=200, y=100)
    botonlistado.lift()
    
    #Boton que edita los datos de un profesor
    botonedita = Button(lienzo_administrar_profesor, text="editar", command  = lambda: editar_profesor(lienzo_administrar_profesor, frame_administracion), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonedita.place(x=333, y=100)
    botonedita.lift()
    
def guardar_datos(lienzo_imagen, frame_administracion, nombreC, numCupo, opprof, dateInicio, dateFinal, spingbox_hora, cantidad_hora, var1, var2, var3, var4, var5, var6, imagen_perfil, ruta_archivo):
    lienzo_imagen.destroy()
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_guarda = Canvas(frame_administracion, width = 450, height = 250, bg = "#900C3F")
    lienzo_guarda.pack()
    lienzo_guarda.place(x=453, y=418)
    lienzo_guarda.create_text(225, 30, text="Guardando datos...", fill="white", font=("Arial", 20))
    
    
    nombre_curso  = nombreC.get()
    numero_cupo   = numCupo.get()
    profesor      = opprof.get()
    fecha_inicio  = dateInicio.get()
    fecha_final   = dateFinal.get()
    hora_inicio   = spingbox_hora.get()
    cant_hora     = cantidad_hora.get()
    
    if(var1.get() == 1):
        variable1 = "Lunes: si"
    else:
        variable1 = "Lunes: No" 
        
    if(var2.get() == 1):
        variable2 = "Martes: si"
    else:
        variable2 = "Martes: No" 
        
    if(var3.get() == 1):
        variable3 = "Miercoles: si"
    else:
        variable3 = "Miercoles: No" 
        
    if(var4.get() == 1):
        variable4 = "Jueves: si"
    else:
        variable4 = "Jueves: No"
        
    if(var5.get() == 1):
        variable5 = "Viernes: si"
    else:
        variable5 = "Viernes: No"  
        
    if(var6.get() == 1):
        variable6 = "Sabado: si"
    else:
        variable6 = "Sabado: No" 
    
    imagen_c = Image.open(ruta_archivo)  # Reemplaza 'ruta_archivo' con la ruta real de tu archivo de imagen
                    
    # Convierte la imagen a bytes
    with io.BytesIO() as output:
        imagen_c.save(output, format='PNG')
        imagen_bytes = output.getvalue()
        datos_imagen_codificados = base64.b64encode(imagen_bytes).decode("utf-8")
    
    
    nombre_del_titulo = nombre_curso + ".txt"
    with open(nombre_del_titulo, 'a') as fp:
        fp.write(nombre_curso.strip() + '\n')
        fp.write(numero_cupo.strip() + '\n')
        fp.write(profesor.strip() + '\n')
        fp.write(fecha_inicio.strip() + '\n')
        fp.write(fecha_final.strip() + '\n')
        fp.write(cant_hora.strip() + '\n')
        fp.write(variable1.strip() + '\n')
        fp.write(variable2.strip() + '\n')
        fp.write(variable3.strip() + '\n')
        fp.write(variable4.strip() + '\n')
        fp.write(variable5.strip() + '\n')
        fp.write(variable6.strip() + '\n')
        fp.write(datos_imagen_codificados.strip() + '\n')
    
        
        
        
#!Aqui se escoje la imagen de fondo para el curso    
def imagen_fondo(lienzo_horario, frame_administracion, nombreC, numCupo, opprof, dateInicio, dateFinal, spingbox_hora, cantidad_hora, var1, var2, var3, var4, var5, var6):
    lienzo_horario.destroy()
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_imagen = Canvas(frame_administracion, width = 450, height = 250, bg = "#900C3F")
    lienzo_imagen.pack()
    lienzo_imagen.place(x=453, y=418)
    lienzo_imagen.create_text(225, 30, text="Subir imagen...", fill="white", font=("Arial", 20))

    #Etiqueta para el guardado de la imagen del curso para el curso
    
    etiqueta_foto_de_perfil = Label(lienzo_imagen, text="Cargar foto de perfil")
    etiqueta_foto_de_perfil.pack()
    etiqueta_foto_de_perfil.place(x=200, y=100, anchor=NW)
    
    
    #Imagen de perfil:
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp")])
    imagen_perfil = PhotoImage(file=ruta_archivo)
    etiqueta_foto_de_perfil.config(image=imagen_perfil)  # Esto puede estar causando el problema.
    etiqueta_foto_de_perfil.image = imagen_perfil
    
    
    #Boton de cerrar horario
    botonguarda = Button(lienzo_imagen, text="Guardar", command = lambda: guardar_datos(lienzo_imagen, frame_administracion, nombreC, numCupo, opprof, dateInicio, dateFinal, spingbox_hora, cantidad_hora, var1, var2, var3, var4, var5, var6, imagen_perfil, ruta_archivo), width=8, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonguarda.place(x=395, y=195)
    botonguarda.lift()
    
    
    
    
def creacion_horario(lienzo_new_curso, frame_administracion, nombreC, numCupo, opprof, dateInicio, dateFinal):
    #Destruccion del lienzo actual
    lienzo_new_curso.destroy()
    spingbox_hora  = StringVar()
    cantidad_hora  = StringVar()
    var1           = IntVar()
    var2           = IntVar()
    var3           = IntVar()
    var4           = IntVar()
    var5           = IntVar()
    var6           = IntVar()
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_horario = Canvas(frame_administracion, width = 450, height = 250, bg = "#900C3F")
    lienzo_horario.pack()
    lienzo_horario.place(x=453, y=418)
    lienzo_horario.create_text(225, 30, text="Creacion del horario del curso", fill="white", font=("Arial", 20))
    
    #Dias de clase
    #Hora de inicio: 
    etiqueta_hora_inicio = Label(lienzo_horario, text="Hora de inicio: ")
    etiqueta_hora_inicio.pack()
    lienzo_horario.create_window(100, 80, anchor = NW, window = etiqueta_hora_inicio)
    
    #Etiqueta de cantidad de horas: 
    etiqueta_cant_horas = Label(lienzo_horario, text="Cantidad de horas: ")
    etiqueta_cant_horas.pack()
    lienzo_horario.create_window(100, 115, anchor = NW, window = etiqueta_cant_horas)
    
    #Spinbox de Hora de inicio
    spinbox_hora_inicio = Spinbox(lienzo_horario, from_=0, to=50, values=("7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"), textvariable=spingbox_hora, wrap=True)
    spinbox_hora_inicio.pack()
    spinbox_hora_inicio.place(x=250, y=80)
    
    
    #Campo de texto para la cantidad de horas
    campo_cantidad = Entry(lienzo_horario, textvariable = cantidad_hora)
    campo_cantidad.pack()
    lienzo_horario.create_window(250, 115, anchor = NW, window = campo_cantidad)
    
    #Checkbox con los dias de la semana
    c1 = Checkbutton(lienzo_horario, text='Lunes',     variable=var1, onvalue=1, offvalue=0)
    c1.pack()
    c1.place(x=10, y=150)
    c2 = Checkbutton(lienzo_horario, text='Martes',    variable=var2, onvalue=1, offvalue=0)
    c2.pack()
    c2.place(x=90, y=150)
    c3 = Checkbutton(lienzo_horario, text='Miercoles', variable=var3, onvalue=1, offvalue=0)
    c3.pack()
    c3.place(x=170, y=150)
    c4 = Checkbutton(lienzo_horario, text='Jueves',    variable=var4, onvalue=1, offvalue=0)
    c4.pack()
    c4.place(x=10, y=200)
    c5 = Checkbutton(lienzo_horario, text='Viernes',   variable=var5, onvalue=1, offvalue=0)
    c5.pack()
    c5.place(x=90, y=200)
    c6 = Checkbutton(lienzo_horario, text='Sabado',    variable=var6, onvalue=1, offvalue=0)
    c6.pack()
    c6.place(x=170, y=200)
    
    
    #Boton de cerrar horario
    botonhorario = Button(lienzo_horario, text="Fondo", command = lambda: imagen_fondo(lienzo_horario, frame_administracion, nombreC, numCupo, opprof, dateInicio, dateFinal, spingbox_hora, cantidad_hora, var1, var2, var3, var4, var5, var6), width=5, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonhorario.place(x=400, y=190)
    botonhorario.lift()
    
    
#!Aqui vamos a trabajar lo nuevo
def nuevos_cursos(frame_administracion, lienzo_newcurso):
    """Esta funcion sirve para crear nuevos cursos recibe como parametro el frame de administracion
    y el lienzo de nuevos cursos"""
    
    #El tamaño del lienzo es: 400x200
    
    
    #Declaracion de variables StrinVar()
    nombreC    = StringVar()
    numCupo    = StringVar()
    dateInicio = StringVar()
    dateFinal  = StringVar()
    opprof     = StringVar()
    posnombre  = 0
    posdpi     = 2
    
    lista_nomdpi_prof = []
    
    #Etiqueta del nombre del curso
    etiqueta_nombrec = Label(lienzo_newcurso, text="nombre del curso: ")
    etiqueta_nombrec.pack()
    lienzo_newcurso.create_window(50, 45, anchor = NW, window = etiqueta_nombrec)
    
    #Etiqueta Cupo de estudiantes 
    etiqueta_cupo = Label(lienzo_newcurso, text="numero de cupo: ")
    etiqueta_cupo.pack()
    lienzo_newcurso.create_window(50, 80, anchor = NW, window = etiqueta_cupo)
    
    #Etiqueta profesor: 
    etiqueta_profesor = Label(lienzo_newcurso, text="profesor: ")
    etiqueta_profesor.pack()
    lienzo_newcurso.create_window(50, 115, anchor = NW, window = etiqueta_profesor)
    
    #Etiqueta fecha de inicio: 
    etiqueta_inicio = Label(lienzo_newcurso, text="Fecha de inicio: ")
    etiqueta_inicio.pack()
    lienzo_newcurso.create_window(50, 150, anchor = NW, window = etiqueta_inicio)
    
    #Etiqueta fecha de finalizacion: 
    etiqueta_final = Label(lienzo_newcurso, text="Fecha de fin: ")
    etiqueta_final.pack()
    lienzo_newcurso.create_window(50, 185, anchor = NW, window = etiqueta_final)    
    
    #Campo nombre de curso
    campo_nombrec= Entry(lienzo_newcurso, textvariable = nombreC)
    campo_nombrec.pack()
    lienzo_newcurso.create_window(200, 45, anchor = NW, window = campo_nombrec)
    
    #Campo numero de cupo
    campo_num_cupo = Entry(lienzo_newcurso, textvariable = numCupo)
    campo_num_cupo.pack()
    lienzo_newcurso.create_window(200, 80, anchor = NW, window = campo_num_cupo)
    
    #Devuelve una lista de los profesores disponibles
    with open('todos_profesores.txt', 'r') as fp:
        datos = fp.readlines()
        for index, dato in enumerate(datos):
            if index == posnombre:
                posnombre += 4
                nombre = dato.strip()
            
            if index == posdpi:
                posdpi += 4
                dpi = dato.strip()  
                elemento = nombre + " " + dpi
                lista_nomdpi_prof.append(elemento.strip())
    
    #Crea el menu opciones solo con los DPI        
    menu = OptionMenu(lienzo_newcurso, opprof, *lista_nomdpi_prof)
    menu.pack()
    menu.place(x=225, y=115)
    
    #Campo Fecha de inicio
    campo_fecha_inicio = Entry(lienzo_newcurso, textvariable = dateInicio)
    campo_fecha_inicio.pack()
    lienzo_newcurso.create_window(200, 150, anchor = NW, window = campo_fecha_inicio)
    
    #Campo fecha de finalizacion
    campo_fecha_final = Entry(lienzo_newcurso, textvariable = dateFinal)
    campo_fecha_final.pack()
    lienzo_newcurso.create_window(200, 185, anchor = NW, window = campo_fecha_final)
    
    #Boton de cerrar horario
    botonhorario = Button(lienzo_newcurso, text="horario", command = lambda: creacion_horario(lienzo_newcurso, frame_administracion, nombreC, numCupo, opprof, dateInicio, dateFinal), width=5, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonhorario.place(x=400, y=190)
    botonhorario.lift()
    

def cerrar_usuario():
    sys.exit()


def principal(frame_regadmin, raiz, lienzo_panel, imagenadmin):
    frame_regadmin.destroy()
    
    #Creacion del frame para el cuestionario
    frame_administracion = Frame(raiz)       
    frame_administracion.pack()
    
    
    #Crea el lienzo con la imagen de fondo
    lienzo_nueva_cuenta = Canvas(frame_administracion, width = 2160, height = 2160)
    lienzo_nueva_cuenta.pack()
    lienzo_nueva_cuenta.create_image(0, 0, anchor=NW, image = imagenadmin)
    
    
    #1)Crea el lienzo para bloqueo de cuentas
    lienzo_bloqueo_cuentas = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_bloqueo_cuentas.pack()
    lienzo_bloqueo_cuentas.place(x=40, y=50)
    lienzo_bloqueo_cuentas.create_text(200, 30, text="Desbloquear cuenta", fill="white", font=("Arial", 18))

    
    #2)Crea el lienzo para el cambio de contraseña
    lienzo_password = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_password.pack()
    lienzo_password.place(x=916, y=50)
    lienzo_password.create_text(200, 30, text="Cambiar contraseña de admin", fill="white", font=("Arial", 20))
    
    #3)Crea el lienzo para el listado de notas
    lienzo_reporte_notas= Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_reporte_notas.pack()
    lienzo_reporte_notas.place(x=40, y=284)
    lienzo_reporte_notas.create_text(200, 30, text="Reportes de notas", fill="white", font=("Arial", 20))
    
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_administrar_profesor = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_administrar_profesor.pack()
    lienzo_administrar_profesor.place(x=916, y=284)
    lienzo_administrar_profesor.create_text(200, 30, text="Administrador de profesores", fill="white", font=("Arial", 20))
    
    
    #5)Lienzo para nuevos cursos
    lienzo_nuevo_curso = Canvas(frame_administracion, width = 445, height = 250, bg = "#900C3F")
    lienzo_nuevo_curso.pack()
    lienzo_nuevo_curso.place(x=453, y=418)
    lienzo_nuevo_curso.create_text(225, 30, text="Creacion de nuevos cursos", fill="white", font=("Arial", 20))
    
    
    #Boton de cerrar cuenta
    botoncerrar = Button(frame_administracion, text="Cerrar secion", command = cerrar_usuario, width=10, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botoncerrar.place(x=1300, y=0)
    botoncerrar.lift()
    
    cambio_password(frame_administracion, lienzo_password)
    administracion_profesores(frame_administracion, lienzo_administrar_profesor)
    nuevos_cursos(frame_administracion, lienzo_nuevo_curso)
    desbloqueo_cuentas(frame_administracion, lienzo_bloqueo_cuentas)
    
    

    
    