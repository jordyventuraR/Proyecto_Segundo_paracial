from tkinter import*


def nueva_cuenta(numero_de_casa_ganadora, frame_nueva_cuenta, imagen, nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion):
    cortx = 400
    cory = 100
    
    
    #Lienzo
    lienzo_nueva_cuenta = Canvas(frame_nueva_cuenta, width = 2160, height = 2160)
    lienzo_nueva_cuenta.pack()
    lienzo_nueva_cuenta.create_image(0, 0, anchor=NW, image = imagen)
    
    
    #Nombre:
    #Etiqueta
    etiqueta1 = Label(frame_nueva_cuenta, text="Ingrese su nombre: ")
    etiqueta1.pack()
    etiqueta1 = lienzo_nueva_cuenta.create_window(cortx, cory, anchor = NW, window = etiqueta1)
    
    
    #Campo de texto
    entrada1 = Entry(frame_nueva_cuenta, textvariable = nombre)
    entrada1.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory, anchor = NW, window = entrada1)
    
    
    #Apellido:
    #Etiqueta
    etiqueta2=Label(frame_nueva_cuenta, text="Ingrese su apellido: ")
    etiqueta2.pack()
    etiqueta2=lienzo_nueva_cuenta.create_window(cortx, cory+50, anchor = NW, window = etiqueta2)
    
    #Campo de texto
    entrada2 = Entry(frame_nueva_cuenta, textvariable = apellido)
    entrada2.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+50, anchor = NW, window = entrada2)
    
    
    #DPI:
    #Etiqueta
    etiqueta3 = Label(frame_nueva_cuenta, text = "Ingrese su dpi: ")
    etiqueta3.pack()
    etiqueta3 = lienzo_nueva_cuenta.create_window(cortx, cory+100, anchor = NW, window = etiqueta3)
    
    #Campo de texto
    entrada3=Entry(frame_nueva_cuenta, textvariable = dpi)
    entrada3.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+100, anchor = NW, window = entrada3)
    
    
    #Fecha de nacimiento:
    #Etiqueta
    etiqueta4 = Label(frame_nueva_cuenta, text = "Ingrese la fecha de su nacimiento: ")
    etiqueta4.pack()
    etiqueta4 = lienzo_nueva_cuenta.create_window(cortx, cory+150, anchor = NW, window = etiqueta4)
        
    #Campo de texto
    entrada4 = Entry(frame_nueva_cuenta, textvariable = fecha)
    entrada4.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+150, anchor = NW, window = entrada4)
    
    
    #Telefono:
    #Etiqueta
    etiqueta5 = Label(frame_nueva_cuenta, text = "Ingrese su telefono: ")
    etiqueta5.pack()
    etiqueta5 = lienzo_nueva_cuenta.create_window(cortx, cory+200, anchor = NW, window = etiqueta5)
        
    #Campo de texto
    entrada5 = Entry(frame_nueva_cuenta, textvariable = telefono)
    entrada5.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+200, anchor = NW, window = entrada5)
    
    
    #Nombre de usuario: 
    #Etiqueta
    etiqueta6 = Label(frame_nueva_cuenta, text = "Ingrese su nombre de usuario: ")
    etiqueta6.pack()
    etiqueta6 = lienzo_nueva_cuenta.create_window(cortx, cory+250, anchor = NW, window = etiqueta6)
        
    #Campo de texto
    entrada6 = Entry(frame_nueva_cuenta, textvariable = username)
    entrada6.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+250, anchor = NW, window = entrada6)
    
    
    #Direccion de correo:
    #Etiqueta
    etiqueta7 = Label(frame_nueva_cuenta, text="Ingrese su direccion de correo: ")
    etiqueta7.pack()
    etiqueta7 = lienzo_nueva_cuenta.create_window(cortx, cory+300, anchor = NW, window = etiqueta7)
        
    #Campo de texto
    entrada7 = Entry(frame_nueva_cuenta, textvariable = correo)
    entrada7.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+300, anchor = NW, window = entrada7)
    
    
    #Contraseña:
    #Etiqueta
    etiqueta8 = Label(frame_nueva_cuenta, text="Ingrese su contraseña: ")
    etiqueta8.pack()
    etiqueta8 = lienzo_nueva_cuenta.create_window(cortx, cory+350, anchor = NW, window = etiqueta8)
        
    #Campo de texto
    entrada8 = Entry(frame_nueva_cuenta, textvariable = password, show = "*")
    entrada8.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+350, anchor = NW, window = entrada8)
    
    
    #Confirmacion:
    #Etiqueta
    etiqueta9 = Label(frame_nueva_cuenta, text="Reafirme su password: ")
    etiqueta9.pack()
    etiqueta9 = lienzo_nueva_cuenta.create_window(cortx, cory+400, anchor = NW, window = etiqueta9)
        
    #Campo de texto
    entrada9 = Entry(frame_nueva_cuenta, textvariable = confirmacion, show = "*")
    entrada9.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+400, anchor = NW, window = entrada9)
    
    
    #fondo del frame
    lista_recibida = [nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion]
    return lista_recibida
    
    
def recibir_datos_de_crear_cuenta (lista_de_recepcion):
    lista_recibida = []
    for elemento in lista_de_recepcion:
        valor = elemento.get()
        lista_recibida.append(valor)  # No necesitas .get() aquí
    print(lista_recibida)