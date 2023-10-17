from tkinter import*
import sys
import time

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

def bloqueo_cuentas(camtexto2):
    pass
    
    
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
    textconfirpass =  entrada_confirpass.get()
    
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
            fp.write(textconfirpass + '\n')
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
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_administrar_profesor = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_administrar_profesor.pack()
    lienzo_administrar_profesor.place(x=916, y=284)
    lienzo_administrar_profesor.create_text(200, 30, text="Administrador de profesores", fill="white", font=("Arial", 20))

def editar_profesor(lienzo_administrar_profesor, frame_administracion):
    """La funcion que edita el profesor"""
    lienzo_administrar_profesor.destroy()
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_administrar_profesor = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_administrar_profesor.pack()
    lienzo_administrar_profesor.place(x=916, y=284)
    lienzo_administrar_profesor.create_text(200, 30, text="Administrador de profesores", fill="white", font=("Arial", 20))
    

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

def nuevo_cursos():
    pass

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
    lienzo_bloqueo_cuentas.place(x=50, y=50)
    lienzo_bloqueo_cuentas.create_text(200, 30, text="Bloquear cuentas", fill="white", font=("Arial", 18))

    
    #2)Crea el lienzo para el cambio de contraseña
    lienzo_password = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_password.pack()
    lienzo_password.place(x=916, y=50)
    lienzo_password.create_text(200, 30, text="Cambiar contraseña de admin", fill="white", font=("Arial", 20))
    
    #3)Crea el lienzo para el listado de notas
    lienzo_reporte_notas= Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_reporte_notas.pack()
    lienzo_reporte_notas.place(x=50, y=284)
    lienzo_reporte_notas.create_text(200, 30, text="Reportes de notas", fill="white", font=("Arial", 20))
    
    
    #4)Crea el lienzo de administracion de profesores
    lienzo_administrar_profesor = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_administrar_profesor.pack()
    lienzo_administrar_profesor.place(x=916, y=284)
    lienzo_administrar_profesor.create_text(200, 30, text="Administrador de profesores", fill="white", font=("Arial", 20))
    
    
    #5)Lienzo para nuevos cursos
    lienzo_nuevo_curso = Canvas(frame_administracion, width = 400, height = 200, bg = "#900C3F")
    lienzo_nuevo_curso.pack()
    lienzo_nuevo_curso.place(x=483, y=518)
    lienzo_nuevo_curso.create_text(200, 30, text="Creacion de nuevos cursos", fill="white", font=("Arial", 20))
    
    
    #Boton de cerrar cuenta
    botoncerrar = Button(frame_administracion, text="Cerrar secion", command = cerrar_usuario, width=10, height=4) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    botoncerrar.place(x=1300, y=0)
    botoncerrar.lift()
    
    cambio_password(frame_administracion, lienzo_password)
    administracion_profesores(frame_administracion, lienzo_administrar_profesor)
    
    

    
    