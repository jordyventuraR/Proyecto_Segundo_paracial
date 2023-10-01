#La pantalla principal la seleccion de escuela 
from tkinter import*
from  Preguntas import cuestionario, enviar
from Programa_de_crear_cuenta import nueva_cuenta, recibir_datos_de_crear_cuenta
from Alertas_cuenta_python import mensajes


#Botones
def administracion():
    print("Administracion")

#Funciones de los botones
def seleccionar_escuela(escuela):
    print(escuela)

def boton_enviar_cuenta(casa, imagen, frame_nueva_cuenta,  nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion):
    lista_de_recepcion, lienzo = nueva_cuenta(casa, frame_nueva_cuenta, imagen,  nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion)
    lista_recibida, syntaxis_correcta = recibir_datos_de_crear_cuenta(lista_de_recepcion, lienzo, frame_nueva_cuenta, 400, 100, imagen)
    mensajes(lista_recibida, syntaxis_correcta, frame_nueva_cuenta, lienzo)


#Envia a la pantalla de registro de cuentas
def Btn_enviar(lista, frame1, imagen, raiz):
    casa=enviar(lista, frame1)         #Obtiene el valor de la casa con mas puntaje
    frame_nueva_cuenta = Frame(raiz)   #Crea el frame para la pantalla de la nueva cuenta
    frame_nueva_cuenta.pack()
    print(casa)
    nombre=StringVar()
    apellido=StringVar() 
    correo=StringVar()
    username=StringVar() 
    dpi=StringVar() 
    telefono=StringVar()
    fecha=StringVar()
    password=StringVar()
    confirmacion=StringVar()
    
    # Asigna valores inic.geiales vacíos a las StringVar
    nombre.set("Ingrese su nombre: ")
    apellido.set("Ingrese su apellido: ")
    correo.set("Ingrese su correo electronico: ")
    username.set("Ingrese su username: ")
    dpi.set("Ingrese su dpi: ")
    telefono.set("Ingrese su numero telefonico: ")
    fecha.set("Ingrese su fecha de nacimiento: ")
    password.set("")
    confirmacion.set("")
    
    
    lista_de_recepcion_de_datos, lienzo = nueva_cuenta(casa, frame_nueva_cuenta, imagen, nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion)
    botonEnvD = Button(frame_nueva_cuenta, text="Enviar", command=lambda: boton_enviar_cuenta(casa, imagen, frame_nueva_cuenta,  nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion), width=10, height=5) #Coloca el boton para enviar los datos
    botonEnvD.place(x=1278, y=0)
    botonEnvD.lift()
    #mensajes(frame_nueva_cuenta)
    
#La pantalla principal
def regresar(raiz, frame_cuestionario):
    # Crear un frame y agregarlo a la ventana principal
    print("Regreso")
    frame_cuestionario.destroy()
    frame_principal = Frame(raiz)
    frame_principal.pack()

    #Cargar el icono de la imagen
    raiz.iconbitmap("Hogwartsicono.ico")   

    #Cargar imagenes
    imagen = PhotoImage(file="hogwartsFP.png") 
    imagenEsc1=PhotoImage(file="Gryffindor_logo.png")
    imagenEsc2=PhotoImage(file="Hufflepuff.png")
    imagenEsc3=PhotoImage(file="Slytherin.png")
    imagenEsc4=PhotoImage(file="Ravenclaw.png")
    
    # Fondo
    lienzo = Canvas(frame_principal, width=2160, height=2160)
    lienzo.pack()

    # Mostrar la imagen en el lienzo
    lienzo.create_image(0, 0, anchor=NW, image=imagen)

    # Crear botones para las escuelas
    botonEsc1 = Button(frame_principal, image=imagenEsc1, command=lambda: seleccionar_escuela("Gryffindor"))
    botonEsc2 = Button(frame_principal, image=imagenEsc2, command=lambda: seleccionar_escuela("Hufflepuff"))
    botonEsc3 = Button(frame_principal, image=imagenEsc3, command=lambda: seleccionar_escuela("Slytherin"))
    botonEsc4 = Button(frame_principal, image=imagenEsc4, command=lambda: seleccionar_escuela("Ravenclaw"))
    boton5 = Button(frame_principal, text="Crear cuenta", command=lambda: preguntas_cuestionario(frame_principal, raiz, imagen), width=10, height=5)
    boton6 = Button(frame_principal, text="administracion", command=administracion, width=10, height=5)

    #ubicar los botones
    botonEsc1.place(x=493, y=100) 
    botonEsc2.place(x=793, y=100)
    botonEsc3.place(x=493, y=337) 
    botonEsc4.place(x=793, y=337) 
    boton5.place(x=650, y=500) 
    boton6.place(x=650, y=600)

    #Eleva los botones
    botonEsc1.lift()
    botonEsc2.lift()
    botonEsc3.lift()
    botonEsc4.lift()
    boton5.lift()
    boton6.lift()
    raiz.mainloop() 

#Presenta las preguntas
def preguntas_cuestionario(frame_principal,raiz, imagen):
    #! Aqui se va cambiar el frame y se van a poner los dos botones
    frame_principal.destroy()
    
    #Creacion del frame para el cuestionario
    frame_cuestionario = Frame(raiz) 
    frame_cuestionario.pack()
    
    
    #fondo del frame
    lienzo_Cuestionario = Canvas(frame_cuestionario, width=2160, height=2160)
    lienzo_Cuestionario.pack()
    lienzo_Cuestionario.create_image(0, 0, anchor=NW, image=imagen)
    lista_de_datos=cuestionario(raiz, imagen, frame_cuestionario, lienzo_Cuestionario)
    
    #!boton de enviar
    botonenviar = Button(frame_cuestionario, text="enviar", command=lambda: Btn_enviar(lista_de_datos, frame_cuestionario, imagen, raiz), width=10, height=5)
    botonenviar.place(x=1278, y=0)
    botonenviar.lift()
    
    #!Botones
    botonregreso = Button(frame_cuestionario, text="regreso", command=lambda: regresar(raiz, frame_cuestionario), width=10, height=5)
    botonregreso.place(x=0, y=0)
    botonregreso.lift()
    

#Creacion la ventana principal
raiz=Tk()
raiz.title("Hogwarts")                  #Titulo
raiz.resizable(True, True)              #Ajustable
raiz.geometry("2160x2160")              #Tamaño por defecto
global frame_principal, frame_cuestionario
frame_cuestionario = Frame(raiz)
regresar(raiz, frame_cuestionario)
