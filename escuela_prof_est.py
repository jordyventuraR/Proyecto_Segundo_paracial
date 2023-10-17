from tkinter import*


def comprobar():
    pass


def seleccion_rol(lienzo_general, color):
    """En la funcion se crean los paneles para seleccionar el rol de alumno y el de profesor
    y recibe como argumento de la funcion el lienzo"""
    #El lienzo donde se trabaja las opciones para que se registre el profesor
    lienzo_eleccion_profe = Canvas(lienzo_general, width = 600, height = 600, bg = color)
    lienzo_eleccion_profe.pack()
    lienzo_eleccion_profe.place(x=42, y=84)
    lienzo_eleccion_profe.create_text(342, 90, text = "Profesor", fill="white", font=("Arial", 16))
    
    #El lienzo donde se trabaja las opciones de estudiante
    lienzo_eleccion_estudiante = Canvas(lienzo_general, width = 600, height = 600, bg = color)
    lienzo_eleccion_estudiante.pack()
    lienzo_eleccion_estudiante.place(x=725, y=84)
    lienzo_eleccion_estudiante.create_text(342, 90, text = "Estudiante", fill="white", font=("Arial", 16))
    
    #Variables tipo string
    #Para el uso de widgets en el lienzo de estudiantes
    texto_nombre_e   = StringVar()
    texto_apellido_e = StringVar()
    texto_password_e = StringVar()
    
    #Para el uso de widgets en el lienzo de profesor
    texto_nombre_p   = StringVar()
    texto_apellido_p = StringVar()
    texto_password_p = StringVar()
    
    
    #Etiquetas del lienzo de profesores
    #Usuario
    etiqueta_username = Label(lienzo_general, text="Username: ")
    etiqueta_username.pack()
    lienzo_eleccion_profe.create_window(150, 150, anchor = NW, window = etiqueta_username)
    
    #Apellido
    etiqueta_apellido = Label(lienzo_general, text="Apellido: ")
    etiqueta_apellido.pack()
    lienzo_eleccion_profe.create_window(150, 350, anchor = NW, window = etiqueta_apellido)
    
    #Contraseña
    etiqueta_password = Label(lienzo_general, text="Password: ")
    etiqueta_password.pack()
    lienzo_eleccion_profe.create_window(150, 550, anchor = NW, window = etiqueta_password)
    
    
    #Etiquetas del lienzo de estudiantes
    #Usuario
    etiqueta_username_e = Label(lienzo_general, text="Username: ")
    etiqueta_username_e.pack()
    lienzo_eleccion_estudiante.create_window(150, 150, anchor = NW, window = etiqueta_username_e)
    
    #Apellido
    etiqueta_apellido_e = Label(lienzo_general, text="Apellido: ")
    etiqueta_apellido_e.pack()
    lienzo_eleccion_estudiante.create_window(150, 350, anchor = NW, window = etiqueta_apellido_e)
    
    #Contraseña
    etiqueta_password_e = Label(lienzo_general, text="Password: ")
    etiqueta_password_e.pack()
    lienzo_eleccion_estudiante.create_window(150, 550, anchor = NW, window = etiqueta_password_e)
    

    #Campo de texto de profesores
    #Nombre
    entrada_username_p = Entry(lienzo_general, textvariable = texto_nombre_p)
    entrada_username_p.pack()
    lienzo_eleccion_profe.create_window(450, 150, anchor = NW, window = entrada_username_p)
    
    #Apellido
    entrada_apellido_p = Entry(lienzo_general, textvariable = texto_apellido_p)
    entrada_apellido_p.pack()
    lienzo_eleccion_profe.create_window(450, 350, anchor = NW, window = entrada_apellido_p)
    
    #Contraseña
    entrada_password_p = Entry(lienzo_general, textvariable = texto_password_p)
    entrada_password_p.pack()
    lienzo_eleccion_profe.create_window(450, 550, anchor = NW, window = entrada_password_p)
    
    
    #Campo de texto de estudiantes
    #Nombre
    entrada_username_e = Entry(lienzo_general, textvariable = texto_nombre_e)
    entrada_username_e.pack()
    lienzo_eleccion_estudiante.create_window(450, 150, anchor = NW, window = entrada_username_e)
    
    #Apellido
    entrada_apellido_e = Entry(lienzo_general, textvariable = texto_apellido_e)
    entrada_apellido_e.pack()
    lienzo_eleccion_estudiante.create_window(450, 350, anchor = NW, window = entrada_apellido_e)
    
    #Contraseña
    entrada_password_e = Entry(lienzo_general, textvariable = texto_password_e)
    entrada_password_e.pack()
    lienzo_eleccion_estudiante.create_window(450, 550, anchor = NW, window = entrada_password_e)
    
    
    #Botones
    #Boton que envia los datos de profesor
    botonenvp = Button(lienzo_eleccion_profe, text="Entrar",  command = lambda: comprobar(), width=6, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenvp.place(x=550, y=0)
    botonenvp.lift()
    
    #Boton que envia los datos de estudiante
    botonenve = Button(lienzo_eleccion_estudiante, text="Entrar", command  = lambda: comprobar(), width=6, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botonenve.place(x=550, y=0)
    botonenve.lift()
    
    
    
    