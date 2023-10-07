#Jordy Ventura
#La pantalla principal la seleccion de escuela
#Librerias nativas
from tkinter import*            #Libreria para el manejo de graficos

#Carga de modulos propios de python
from  Preguntas import cuestionario, enviar                                         #Libreria para hacer el cuestionario
from Programa_de_crear_cuenta import nueva_cuenta, recibir_datos_de_crear_cuenta    #Libreria que crea la pantalla de registros y valida la syntaxis de los datos ingresados
from Alertas_cuenta_python import mensajes, mensajes_validacion_2                   #Libreria que coloca los errores de manera visual
from almacenado_datos import alamacenamiento                                        #Libreria que se almacena y se encripta la contraseña
from Enviar_correo import confirmacion_new                                          #Libreria que envia el correo de confirmacion
from Busqueda_datos import*                                                         #Libreria que busca que ciertos datos sean unicos


#Botones
def administracion():
    print("Administracion")

#Funciones de los botones
def seleccionar_escuela(escuela):
    print(escuela)
    
def validacion2(frame_nueva_cuenta, lienzo_nueva_cuenta, primera_validacion, raiz):
    if validacion2_DPI(primera_validacion[2]) == True:                 #Si el DPI es unico
        if validacion2_username(primera_validacion[5]) == True:        #Si el username es unico
            if validacion2_telefono(primera_validacion[4]) == True:    #Si el numero de telefono es unico
                if validacion2_correo(primera_validacion[6]) == True:  #Si el correo es unico
                    if alamacenamiento() == True:                      #Si los datos ya fueron almacenados
                        if confirmacion_new == True:
                            regresar(raiz, frame_nueva_cuenta)         #Regresa a la pantalla principal
                        else:
                            mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "No se pudo enviar el correo", 800, 500)
                    else:
                        mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "No se pudo guardar los datos", 800, 500)
                else:
                    mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "El correo ya existe en el sistema", 800, 400)
                    return False
            else:
                mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "El numero de celular ya existe en el sistema", 800, 300)
                return False
        else:
            mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "El username ya existe en el sistema", 800, 350)
            return False
    else:
        mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, "El DPI ya existe en el sistema", 800, 200)
        return False
    
        
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
        #Se verifican que sena datos unicos
        botonEnvD = Button(frame_nueva_cuenta, text="Enviar", command=lambda: validacion2(frame_nueva_cuenta, lienzo_nueva_cuenta, primera_validacion, raiz), width=10, height=5)
        botonEnvD.place(x=1278, y=0)
        botonEnvD.lift()

#Envia a la pantalla de registro de cuentas
def Btn_enviar(lista, frame1, imagen, raiz):
    casa = enviar(lista, frame1)         #Obtiene el valor de la casa con mas puntaje
    
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

    #Cargar imagenes que sirven de botones y de fondo
    imagen = PhotoImage(file="hogwartsFP.png") 
    imagenEsc1=PhotoImage(file="Gryffindor_logo.png")
    imagenEsc2=PhotoImage(file="Hufflepuff.png")
    imagenEsc3=PhotoImage(file="Slytherin.png")
    imagenEsc4=PhotoImage(file="Ravenclaw.png")
    
    #Crea el lienzo
    lienzo = Canvas(frame_principal, width=2160, height=2160)
    lienzo.pack()

    #Coloca la imagen de fondo
    lienzo.create_image(0, 0, anchor=NW, image=imagen)

    # Crear botones para las escuelas y cambia el parametro de la escuela
    botonEsc1 = Button(frame_principal, image=imagenEsc1, command=lambda: seleccionar_escuela("Gryffindor"))
    botonEsc2 = Button(frame_principal, image=imagenEsc2, command=lambda: seleccionar_escuela("Hufflepuff"))
    botonEsc3 = Button(frame_principal, image=imagenEsc3, command=lambda: seleccionar_escuela("Slytherin"))
    botonEsc4 = Button(frame_principal, image=imagenEsc4, command=lambda: seleccionar_escuela("Ravenclaw"))
    # Crea el boton para el de crear cuenta y el de administracion
    boton5 = Button(frame_principal, text="Crear cuenta", command=lambda: preguntas_cuestionario(frame_principal, raiz, imagen), width=10, height=5)
    boton6 = Button(frame_principal, text="administracion", command=administracion, width=10, height=5)

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
def preguntas_cuestionario(frame_principal,raiz, imagen):
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
