from tkinter import*

from panel_administrativo import principal

import time



def enviar_administracion(entrada1, entrada2, frame_administracion, raiz, imagen, lienzo_cuenta_administracion):
    """ La funcion obtiene el nombre de usuario y la contraseña del documento y lo compara con los campos de textos
    ingresados por el usuario y si amboos son iguales entra en el panel de administracion sino borra los datos para que 
    sean reingresados, los parametros son:
    1) Entrada de campo de texto 1: Que obtiene el username
    2) Entrada de campo de texto 2: Que obtiene el password 
    3) frame
    4) raiz
    5) la imagen de fondo
    6) El lienzo"""
    #Abre el documento de en modo lectura y guarda la segunda linea(username) y la tercera linea(password)
    with open('usuario_password_admin.txt', 'r') as fp:
        datos = fp.readlines()
        username_admin = datos[0]
        password_admin  = datos[1]
    
    
    username = entrada1.get()
    password = entrada2.get()
        
    #Lectura
    if(password_admin == password):
        principal(frame_administracion, raiz, lienzo_cuenta_administracion, imagen)
    else:
        #Etiqueta
        time.sleep(2)
        admin(raiz, frame_administracion, lienzo_cuenta_administracion,  imagen)


def mostrar_password(entrada2, boton):
    """La funcion que pasa la contraseña visible a **** o de **** a visible"""
    #Si la contraseña no esta visible
    if entrada2['show'] == '*':
        entrada2.config(show='')        #La hace visible
        boton.config(text='Ocultar')    #Cambia el texto del boton de ocultar
    #Si la contraseña es visible
    else:
        entrada2.config(show='*')       #La oculta              
        boton.config(text='Mostrar')    #Cambia el texto del boton a mostrar
    
        
def admin(raiz, frame_administracion, lienzo_cuenta_administracion, imagen):
    """Esta funcion crear los campos para ingresar como administrador, recibe como registros:
    1) Raiz
    2) frame
    3) Lienzo
    4) imagen de la pantalla de administracion
    y envia a su confirmacion"""
    
    #Declaracion de las variables tipo StrinVar para los campos de textos
    username = StringVar()
    password = StringVar()
    
    #Etiqueta de username
    etiqueta1 = Label(frame_administracion, text="Ingrese su nombre: ")
    etiqueta1.pack()
    etiqueta1 = lienzo_cuenta_administracion.create_window(500, 300, anchor = NW, window = etiqueta1)
    
    
    #Campo de username
    entrada1 = Entry(frame_administracion, textvariable = username)
    entrada1.pack()
    lienzo_cuenta_administracion.create_window(700, 300, anchor = NW, window = entrada1)
    
    #Etiqueta de contraseña
    etiqueta2 = Label(frame_administracion, text="Ingrese su password: ")
    etiqueta2.pack()
    etiqueta2 = lienzo_cuenta_administracion.create_window(500, 500, anchor = NW, window = etiqueta2)
    
    #Campo de texto de contraseña
    entrada2 = Entry(frame_administracion, textvariable = password, show="*")
    entrada2.pack()
    lienzo_cuenta_administracion.create_window(700, 500, anchor = NW, window = entrada2)
    
    #Boton que sirve para mostrar u ocultar la contraseña ingresada en el campo de contraseña
    botonmostrar = Button(frame_administracion, text="mostrar", command = lambda: mostrar_password(entrada2, botonmostrar), width=5, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonmostrar.place(x=900, y=500)
    botonmostrar.lift()
    
    #Boton que sirve para confirmar que la contraseña ingresada sea correcta
    botonenviar = Button(frame_administracion, text="Enviar", command = lambda: enviar_administracion(entrada1, entrada2, frame_administracion, raiz, imagen, lienzo_cuenta_administracion), width=5, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenviar.place(x=700, y=600)
    botonenviar.lift()
    
        
    