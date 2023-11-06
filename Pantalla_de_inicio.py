#Jordy Ventura
#La pantalla principal la seleccion de escuela
#Librerias nativas
from tkinter import*            #Libreria para el manejo de graficos

#Carga de modulos propios de python
from  Preguntas import cuestionario, enviar                                         #Libreria para hacer el cuestionario
from Programa_de_crear_cuenta import nueva_cuenta, recibir_datos_de_crear_cuenta    #Libreria que crea la pantalla de registros y valida la syntaxis de los datos ingresados
from Alertas_cuenta_python import mensajes, mensajes_validacion_2                   #Libreria que coloca los errores de manera visual
from almacenamiento_todos import guardado                                           #Libreria que se almacena y se encripta la contraseña
from Enviar_correo import confirmacion_new, correo_adv                              #Libreria que envia el correo de confirmacion
from guardaencripta_individual import  guardado_estudiante                          #Libreria que guarda en un documento la informacion de un estudiante y encripta su contraseña
from cuenta_administracion import admin                                             #Libreria que crea la administracion
from panel_administrativo import principal                                          #Libreria que desarrolla el panel principal de administracion  
from select_roles import roles                                                      #Libreria que maneja el ingreso de profesores y estudiantes                                                                         
from Busqueda_datos import*                                                         #Libreria que busca que ciertos datos sean unicos
import time
import sys



def administracion(raiz, frame_principal, imagenadmin):
    """Cuando se presiona el boton de administracion lo dirige al portal del rol de administracion, recibe como parametro:
    1)raiz
    2) frame principal
    3) La imagen del porfal de administracion
    Y no tiene retorno"""
    frame_principal.destroy()                       #Se destruye el frame principal
    
    #Creacion del frame para el cuestionario
    frame_administracion = Frame(raiz)              
    frame_administracion.pack()
    
    
    #Crea el lienzo con la imagen de fondo
    lienzo_nueva_cuenta = Canvas(frame_administracion, width = 2160, height = 2160)
    lienzo_nueva_cuenta.pack()
    lienzo_nueva_cuenta.create_image(0, 0, anchor=NW, image = imagenadmin)
    
    admin(raiz, frame_administracion, lienzo_nueva_cuenta, imagenadmin)
    
    #Boton que regresa a la pantalla principal
    botonregresar = Button(frame_administracion, text="Regresar", command  = lambda: regresar(raiz, frame_administracion), width=6, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonregresar.place(x=0, y=0)
    botonregresar.lift()
        

#Funciones de los botones
def seleccionar_escuela(imagen_fondo, frame, raiz, casa):
    frame.destroy()
    
    #Creacion del frame para el cuestionario
    frame_escuela = Frame(raiz)              
    frame_escuela.pack()
    
    
    #Crea el lienzo con la imagen de fondo
    lienzo_select_rol = Canvas(frame_escuela, width = 2160, height = 2160)
    lienzo_select_rol.pack()
    lienzo_select_rol.create_image(0, 0, anchor=NW, image = imagen_fondo)
    
    
    if casa==1:
        roles(lienzo_select_rol, "#F70000")          #Rojo Gryffindor
    elif casa==2:
        roles(lienzo_select_rol, "#D3E522")          #Amarillo Hufflepuff
    elif casa==3:
        roles(lienzo_select_rol, "#43E522")          #Verde Slidering
    else:
        roles(lienzo_select_rol, "#2257E5")          #Azul Ravenclaw
    
    #Boton de regresar
    #Boton que regresa a la pantalla principal
    botonregreso = Button(lienzo_select_rol, text="Regresar", command  = lambda: regresar(raiz, frame_escuela), width=6, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonregreso.place(x=0, y=0)
    botonregreso.lift()

        
def validacion2(casa, frame_nueva_cuenta, lienzo_nueva_cuenta, primera_validacion, raiz, imagen):
    lista_DPI, lista_nombre_apellido, lista_telefono, lista_correo = generacion_sublistas()
    print(lista_DPI)
    print(lista_nombre_apellido)
    print(lista_correo)
    #lista_de_datos = cuestionario(raiz, imagen, frame_cuestionario, lienzo_nueva_cuenta)
    if validacion2_DPI(primera_validacion[2], lista_DPI) == False:                 #Si el DPI es unico
        if  validacion2_identidad(primera_validacion[0], primera_validacion[1], lista_nombre_apellido) == False:       #Si el username es unico
            if validacion2_telefono(primera_validacion[4], lista_telefono) == False:    #Si el numero de telefono es unico
                if validacion2_correo(primera_validacion[5], lista_correo) == False:  #Si el correo es unico
                    if guardado(primera_validacion, "Almacenado_todos.txt") == True:                      #Si los datos ya fueron almacenados
                        guardado_estudiante(primera_validacion)
                        envio_correo = confirmacion_new(primera_validacion[5], primera_validacion[0], casa)
                        if envio_correo == True:                       #Si el correo fue enviado correctamente
                            guardado_estudiante(primera_validacion)
                            #Muestra un boton que envia a la aceptacion
                            lienzo_nueva_cuenta.destroy()
                            #Crea el lienzo con la imagen de fondo
                            lienzo_guarda_registro = Canvas(frame_nueva_cuenta, width = 1366, height = 768)
                            lienzo_guarda_registro.pack()
                            lienzo_guarda_registro.create_image(0, 0, anchor=NW, image = imagen)
                            lienzo_guarda_registro.create_text(683, 90, text = "Se ha guardado con exito...", fill="white", font=("Arial", 20))
                            
                            #Se verifican que se datos unicos
                            botonregreso = Button(lienzo_guarda_registro, text="Ok", command=lambda: regresar(raiz, frame_nueva_cuenta), width=10, height=5)
                            botonregreso.place(x=683, y=384)
                            botonregreso.lift()        #Regresa a la pantalla principal
                        else:
                            
                            mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "No se pudo enviar el correo", 800, 500)
                            time.sleep(2)
                            sys.exit()
                    else:
                        mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "No se pudo guardar los datos", 800, 500)
                        time.sleep(2)
                        sys.exit()
                else:
                    mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "El correo ya existe en el sistema", 800, 400)
                    time.sleep(2)
                    sys.exit()
            else:
                mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "El numero de celular ya existe en el sistema", 800, 300)
                time.sleep(2)
                sys.exit()
        else:
            mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "Esa identidad ya existe en el sistema", 800, 350)
            if validacion2_correo(primera_validacion[5], lista_correo) == True:
                envio_correo2 =  correo_adv(primera_validacion[5], primera_validacion[0])                                 #Si el nombre el apellido y el correo son iguales se le advierte a usuario original
            else:
                sys.exit()
    else:
        mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "El DPI ya existe en el sistema", 800, 200)
        time.sleep(2)
        sys.exit()
        
def boton_enviar_cuenta(casa, imagen, lienzo_nueva_cuenta, frame_nueva_cuenta, lista, raiz,  nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion):
    lista_de_recepcion = nueva_cuenta(casa, frame_nueva_cuenta, lienzo_nueva_cuenta, imagen,  nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion) #Obtiene el valor de lo que se escribio actualmente en los campos de textos
    primera_validacion, syntaxis_correcta = recibir_datos_de_crear_cuenta(lista_de_recepcion, frame_nueva_cuenta, 400, 100, imagen)                 #Devuelve la lista con la syntaxis correcta de los datos que tiene los campos de texto
    
    enviar_error = mensajes(frame_nueva_cuenta, lienzo_nueva_cuenta, primera_validacion, syntaxis_correcta, 750,  100)                              #Devuelve los errores por pantalla
    #Si hay errores de syntaxis: 
    if enviar_error == True:
        # se deben de corregir estos errores
        botonEnvD = Button(frame_nueva_cuenta, text="Enviar", command=lambda: Btn_enviar(lista, frame_nueva_cuenta, imagen, raiz), width=10, height=5)
        botonEnvD.place(x=1278, y=0)
        botonEnvD.lift()
    #Si no hay errores de syntaxis:
    else:
        #Se verifican que se datos unicos
        botonEnvD = Button(frame_nueva_cuenta, text="Enviar", command=lambda: validacion2(casa, frame_nueva_cuenta, lienzo_nueva_cuenta, primera_validacion, raiz, imagen), width=10, height=5)
        botonEnvD.place(x=1278, y=0)
        botonEnvD.lift()

#Envia a la pantalla de registro de cuentas
def Btn_enviar(lista, frame1, imagen, raiz):
    casa = enviar(lista, frame1)   #Obtiene el valor de la casa con mas puntaje
    
    #Creacion freame y del lienzo
    frame_nueva_cuenta = Frame(raiz)
    frame_nueva_cuenta.pack()
    
    #Crea el lienzo con la misma imagen de fondo
    lienzo_nueva_cuenta = Canvas(frame_nueva_cuenta, width = 2160, height = 2160)
    lienzo_nueva_cuenta.pack()
    lienzo_nueva_cuenta.create_image(0, 0, anchor=NW, image = imagen)
    
    #Crea las variables tipo VarString que sirve para enviar como argumento para los Entry
    nombre = StringVar()
    apellido = StringVar() 
    correo = StringVar()
    username = StringVar() 
    dpi = StringVar() 
    telefono = StringVar()
    fecha = StringVar()
    password = StringVar()
    confirmacion = StringVar()
    
    # Asigna valores iniciales para el  StringVar
    nombre.set("Ingrese su nombre: ")
    apellido.set("Ingrese su apellido: ")
    correo.set("Ingrese su correo electronico: ")
    username.set("Ingrese su username: ")
    dpi.set("Ingrese su dpi: ")
    telefono.set("Ingrese su numero telefonico: ")
    fecha.set("Ingrese su fecha de nacimiento: ")
    password.set("")
    confirmacion.set("")
    
    
    lista_recibida = nueva_cuenta(casa, frame_nueva_cuenta, lienzo_nueva_cuenta, imagen, nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion)      #Llama a la funcion que crea las etiquetas y los campos de texto y que devuelve las VarSting de los campos de texto 
    
    #Crea el boton para enviar los datos de los entry
    botonEnvD = Button(frame_nueva_cuenta, text="Enviar", command=lambda: boton_enviar_cuenta(casa, imagen, lienzo_nueva_cuenta, frame_nueva_cuenta, lista, raiz, nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion), width=10, height=5) #Coloca el boton para enviar los datos
    botonEnvD.place(x=1278, y=0)
    botonEnvD.lift()
    
    
#La pantalla principal
def regresar(raiz, frame_cuestionario):
    # Destruye el frame actual
    frame_cuestionario.destroy()
    #Crea el nuevo frame de la pantalla principal
    frame_principal = Frame(raiz)
    frame_principal.pack()

    #Cargar el logo en la pestaña
    raiz.iconbitmap("Hogwartsicono.ico")   
    
    #Crea el lienzo
    lienzo = Canvas(frame_principal, width=2160, height=2160)
    lienzo.pack()
    
    #Carga de imagenes
    imagen      = PhotoImage(file = "hogwartsFP.png") 
    imagenadmin = PhotoImage(file = "Administracion.png")
    imagenEsc1  = PhotoImage(file = "Gryffindor_logo.png")
    imagenEsc2  = PhotoImage(file = "Hufflepuff.png")
    imagenEsc3  = PhotoImage(file = "Slytherin.png")
    imagenEsc4  = PhotoImage(file = "Ravenclaw.png")
    imagenfon1  = PhotoImage(file = "Gryffindor_fondo.png")
    imagenfon2  = PhotoImage(file = "Hufflepuff_fondo.png")
    imagenfon3  = PhotoImage(file = "Slytherin_fondo.png")
    imagenfon4  = PhotoImage(file = "Ravenclaw_fondo.png")
    
    

    #Coloca la imagen de fondo
    lienzo.create_image(0, 0, anchor=NW, image=imagen)

    # Crear botones para las escuelas y cambia el parametro de la escuela
    botonEsc1 = Button(frame_principal, image=imagenEsc1, command=lambda: seleccionar_escuela(imagenfon1, frame_principal, raiz, 1))
    botonEsc2 = Button(frame_principal, image=imagenEsc2, command=lambda: seleccionar_escuela(imagenfon2, frame_principal, raiz, 2))
    botonEsc3 = Button(frame_principal, image=imagenEsc3, command=lambda: seleccionar_escuela(imagenfon3, frame_principal, raiz, 3))
    botonEsc4 = Button(frame_principal, image=imagenEsc4, command=lambda: seleccionar_escuela(imagenfon4, frame_principal, raiz, 4))
    # Crea el boton para el de crear cuenta y el de administracion
    boton5 = Button(frame_principal, text="Crear cuenta", command=lambda: preguntas_cuestionario(frame_principal, raiz, imagen), width=10, height=5)
    boton6 = Button(frame_principal, text="administracion", command=lambda: administracion(raiz, frame_principal, imagenadmin), width=10, height=5)

    #Posiciona los botones en cordenadas X, Y
    botonEsc1.place(x=493, y=100) 
    botonEsc2.place(x=793, y=100)
    botonEsc3.place(x=493, y=337) 
    botonEsc4.place(x=793, y=337) 
    boton5.place(x=650, y=500) 
    boton6.place(x=650, y=600)

    #Eleva los botones por encima del lienzo
    botonEsc1.lift()
    botonEsc2.lift()
    botonEsc3.lift()
    botonEsc4.lift()
    boton5.lift()
    boton6.lift()
    raiz.mainloop() 


#Presenta el cuestionario que sirve de cuestionario de admision
def preguntas_cuestionario(frame_principal, raiz, imagen):
    #Se destruye el frame actual
    frame_principal.destroy()
    
    #Creacion del frame para el cuestionario
    frame_cuestionario = Frame(raiz) 
    frame_cuestionario.pack()
    
    
    #fondo del frame
    lienzo_Cuestionario = Canvas(frame_cuestionario, width=2160, height=2160)
    lienzo_Cuestionario.pack()
    lienzo_Cuestionario.create_image(0, 0, anchor=NW, image=imagen)
    lista_de_datos = cuestionario(raiz, imagen, frame_cuestionario, lienzo_Cuestionario)    #Llama a la funcion que presenta las preguntas y que retorna las respuestas
    
    #Crea el boton que sirve para enviar las respuestas
    botonenviar = Button(frame_cuestionario, text="enviar", command = lambda: Btn_enviar(lista_de_datos, frame_cuestionario, imagen, raiz), width=10, height=5) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenviar.place(x=1278, y=0)
    botonenviar.lift()
    
    #Crea el boton para regresar a la pantalla principal
    botonregreso = Button(frame_cuestionario, text="regreso", command = lambda: regresar(raiz, frame_cuestionario), width=10, height=5)
    botonregreso.place(x=0, y=0)
    botonregreso.lift()
    

#Programa principal
raiz=Tk()                               #Crea la ventana
raiz.title("Hogwarts")                  #Titulo de la pestaña
raiz.resizable(True, True)              #Ajustable en tamaño
raiz.geometry("2160x2160")              #Tamaño por defecto
global frame_principal, frame_cuestionario
frame_cuestionario = Frame(raiz)
regresar(raiz, frame_cuestionario)      #Envia un frame
