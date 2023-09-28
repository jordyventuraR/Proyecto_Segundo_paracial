from tkinter import*

def etiqueta_y_cuadro_de_texto(variablesL, variablesCT, frame_nueva_cuenta, lienzo_nueva_cuenta, texto, corX, corY):
    #Etiqueta
    variablesL=Label(frame_nueva_cuenta, text=texto)
    variablesL.pack()
    variablesL=lienzo_nueva_cuenta.create_window(corX, corY, anchor=NW, window=variablesL)
    
    
    #Campo de texto
    variablesCT=Entry(frame_nueva_cuenta, textvariable=variablesCT)
    variablesCT.pack()
    variablesCT=lienzo_nueva_cuenta.create_window(corX+200, corY, anchor=NW, window=variablesCT)
    
def pin(passwordL, passwordCT, frame_nueva_cuenta, lienzo_nueva_cuenta, texto, corX, corY):
    #Etiqueta
    passwordL=Label(frame_nueva_cuenta, text=texto)
    passwordL.pack()
    passwordL=lienzo_nueva_cuenta.create_window(corX, corY, anchor=NW, window=passwordL)
    
    #Campo de texto
    passwordCT=Entry(frame_nueva_cuenta, show="*", textvariable=passwordCT)
    passwordCT.pack()
    passwordCT=lienzo_nueva_cuenta.create_window(corX+200, corY, anchor=NW, window=passwordCT)
    

def nueva_cuenta(numero_de_casa_ganadora, imagen, frame_nueva_cuenta):
    global nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion, clavepass_entry
    #fondo del frame
    lienzo_nueva_cuenta = Canvas(frame_nueva_cuenta, width=2160, height=2160)
    lienzo_nueva_cuenta.pack()
    lienzo_nueva_cuenta.create_image(0, 0, anchor=NW, image=imagen)
    
    #Variables globales para Etiquetas
    solicitud_nombre=StringVar
    solicitud_apellido=StringVar
    solicitud_correo=StringVar
    solicitud_username=StringVar 
    solicitud_dpi=StringVar 
    solicitud_telefono=StringVar
    solicitud_fecha=StringVar
    solicitud_password=StringVar
    solicitud_confirmacion=StringVar
    solicitur_clavepass=StringVar

    #Variables globales para Entry
    nombre=StringVar()
    apellido=StringVar() 
    correo=StringVar()
    username=StringVar() 
    dpi=StringVar() 
    telefono=StringVar()
    fecha=StringVar()
    password=StringVar()
    confirmacion=StringVar()
    clavepass_entry=StringVar()
    
    print("Primer print")
    print(clavepass_entry.get())
    print(nombre.get())
    print(apellido.get())
    print(correo.get())
    print(username.get())
    print(dpi.get())
    print(telefono.get())
    print(fecha.get())
    print(password.get())
    print(confirmacion.get())
    # Asigna valores inic.geiales vacíos a las StringVar
    # nombre.set("")
    # apellido.set("")
    # correo.set("")
    # username.set("")
    # dpi.set("")
    # telefono.set("")
    # fecha.set("")
    # password.set("")
    # confirmacion.set("")
    
    print("Segundo print")
    print(clavepass_entry.get())
    print(nombre.get())
    print(apellido.get())
    print(correo.get())
    print(username.get())
    print(dpi.get())
    print(telefono.get())
    print(fecha.get())
    print(password.get())
    print(confirmacion.get())
    
        
    
    etiqueta_y_cuadro_de_texto(solicitud_nombre, nombre, frame_nueva_cuenta, lienzo_nueva_cuenta, "Name: ", 400, 0)
    etiqueta_y_cuadro_de_texto(solicitud_apellido, apellido, frame_nueva_cuenta, lienzo_nueva_cuenta, "Apellido: ", 400, 50)
    etiqueta_y_cuadro_de_texto(solicitud_correo, correo, frame_nueva_cuenta, lienzo_nueva_cuenta, "Direccion de correo electronico: ", 400, 100)
    etiqueta_y_cuadro_de_texto(solicitud_username, username, frame_nueva_cuenta, lienzo_nueva_cuenta, "Nombre de usuario: ", 400, 150)
    etiqueta_y_cuadro_de_texto(solicitud_dpi, dpi, frame_nueva_cuenta, lienzo_nueva_cuenta, "DPI: ", 400, 200)
    etiqueta_y_cuadro_de_texto(solicitud_telefono, telefono, frame_nueva_cuenta, lienzo_nueva_cuenta, "Telefono: ", 400, 250)
    etiqueta_y_cuadro_de_texto(solicitud_fecha, fecha, frame_nueva_cuenta, lienzo_nueva_cuenta, "Ingrese fecha(dd/mm/aa): ", 400, 300)
    #pin(solicitud_password, password, frame_nueva_cuenta, lienzo_nueva_cuenta, "password: ", 400, 350)
    #pin(solicitud_confirmacion, confirmacion,  frame_nueva_cuenta, lienzo_nueva_cuenta, "Confirmacion de password: ", 400, 400)
    #Etiqueta
    clavepass=Label(frame_nueva_cuenta, text="Clave")
    clavepass.pack()
    clavepass=lienzo_nueva_cuenta.create_window(400, 400, anchor=NW, window=clavepass)
    
    #Campo de texto
    clavepass_entry=Entry(frame_nueva_cuenta, show="X", textvariable=clavepass_entry)
    clavepass_entry.pack()
    clavepass_entry=lienzo_nueva_cuenta.create_window(600, 400, anchor=NW, window=clavepass_entry)
    
    
    
    
    lista_recibida = [nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion]
    return lista_recibida
    
    
def recibir_datos_de_crear_cuenta (lista_de_recepcion):
    lista_recibida = []  
    for elemento in lista_de_recepcion:
        valor = elemento.get()
        lista_recibida.append(valor)
    print(lista_recibida)