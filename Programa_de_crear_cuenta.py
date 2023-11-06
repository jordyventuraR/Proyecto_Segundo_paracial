from tkinter import *
from tkinter import filedialog
import re
import datetime
import io
from PIL import Image, ImageTk

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

def nueva_cuenta(numero_de_casa_ganadora, frame_nueva_cuenta, lienzo_nueva_cuenta, imagen, nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion):
    """La función de la nueva cuenta crea las etiquetas y los campos de texto para el registro con la entrada de: 
    1) Nombre completo 
    2) Apellido completo 
    3) DPI
    4) Fecha de nacimiento
    5) Teléfono
    6) Dirección de correo
    7) Contraseña
    8) Confirmación
    Y retorna -> el valor de los campos de texto """
    # Posición de los widgets en la pantalla (X, Y y la posición va dependiendo de la etiqueta y el campo de texto)
    cortx = 400
    cory = 100
    
    imagen_perfil = None
    
    # Nombre:
    # Etiqueta
    etiqueta1 = Label(frame_nueva_cuenta, text="Ingrese su nombre: ")
    etiqueta1.pack()
    etiqueta1 = lienzo_nueva_cuenta.create_window(cortx, cory, anchor=NW, window=etiqueta1)

    # Campo de texto
    entrada1 = Entry(frame_nueva_cuenta, textvariable=nombre)
    entrada1.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory, anchor=NW, window=entrada1)

    # Apellido:
    # Etiqueta
    etiqueta2 = Label(frame_nueva_cuenta, text="Ingrese su apellido: ")
    etiqueta2.pack()
    etiqueta2 = lienzo_nueva_cuenta.create_window(cortx, cory+50, anchor=NW, window=etiqueta2)

    # Campo de texto
    entrada2 = Entry(frame_nueva_cuenta, textvariable=apellido)
    entrada2.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+50, anchor=NW, window=entrada2)

    # DPI:
    # Etiqueta
    etiqueta3 = Label(frame_nueva_cuenta, text="Ingrese su DPI: ")
    etiqueta3.pack()
    etiqueta3 = lienzo_nueva_cuenta.create_window(cortx, cory+100, anchor=NW, window=etiqueta3)

    # Campo de texto
    entrada3 = Entry(frame_nueva_cuenta, textvariable=dpi)
    entrada3.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+100, anchor=NW, window=entrada3)

    # Fecha de nacimiento:
    # Etiqueta
    etiqueta4 = Label(frame_nueva_cuenta, text="Ingrese la fecha de su nacimiento: ")
    etiqueta4.pack()
    etiqueta4 = lienzo_nueva_cuenta.create_window(cortx, cory+150, anchor=NW, window=etiqueta4)

    # Campo de texto
    entrada4 = Entry(frame_nueva_cuenta, textvariable=fecha)
    entrada4.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+150, anchor=NW, window=entrada4)

    # Teléfono:
    # Etiqueta
    etiqueta5 = Label(frame_nueva_cuenta, text="Ingrese su teléfono: ")
    etiqueta5.pack()
    etiqueta5 = lienzo_nueva_cuenta.create_window(cortx, cory+200, anchor=NW, window=etiqueta5)

    # Campo de texto
    entrada5 = Entry(frame_nueva_cuenta, textvariable=telefono)
    entrada5.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+200, anchor=NW, window=entrada5)

    # Dirección de correo:
    # Etiqueta
    etiqueta7 = Label(frame_nueva_cuenta, text="Ingrese su dirección de correo: ")
    etiqueta7.pack()
    etiqueta7 = lienzo_nueva_cuenta.create_window(cortx, cory+250, anchor=NW, window=etiqueta7)

    # Campo de texto
    entrada7 = Entry(frame_nueva_cuenta, textvariable=correo)
    entrada7.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+250, anchor=NW, window=entrada7)

    # Contraseña:
    # Etiqueta
    etiqueta8 = Label(frame_nueva_cuenta, text="Ingrese su contraseña: ")
    etiqueta8.pack()
    etiqueta8 = lienzo_nueva_cuenta.create_window(cortx, cory+300, anchor=NW, window=etiqueta8)

    # Campo de texto
    entrada8 = Entry(frame_nueva_cuenta, textvariable=password, show="*")
    entrada8.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+300, anchor=NW, window=entrada8)

    # Confirmación:
    # Etiqueta
    etiqueta9 = Label(frame_nueva_cuenta, text="Reafirme su contraseña: ")
    etiqueta9.pack()
    etiqueta9 = lienzo_nueva_cuenta.create_window(cortx, cory+350, anchor=NW, window=etiqueta9)

    # Campo de texto
    entrada9 = Entry(frame_nueva_cuenta, textvariable=confirmacion, show="*")
    entrada9.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+350, anchor=NW, window=entrada9)
    
    #Boton de mostrar y ocultar la contraseña
    boton_mostrar = Button(lienzo_nueva_cuenta, text="mostrar", command  = lambda: mostrar_password(entrada8, entrada9, boton_mostrar), width=6, height=3) #Entrega como parametro la lista de respuestas, el frame actual, la imagen de fondo y la raiz
    boton_mostrar.place(x=cortx+200, y = cory+400)
    boton_mostrar.lift()

    etiqueta_foto_de_perfil = Label(lienzo_nueva_cuenta, text="Cargar foto de perfil")
    etiqueta_foto_de_perfil.pack()
    etiqueta_foto_de_perfil.place(x=cortx+200, y=cory+470, anchor=NW)
    
    
    #Imagen de perfil:
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp")])
    imagen_perfil = PhotoImage(file=ruta_archivo)
    etiqueta_foto_de_perfil.config(image=imagen_perfil)  # Esto puede estar causando el problema.
    etiqueta_foto_de_perfil.image = imagen_perfil
    
    
    # Fondo del frame
    lista_recibida = [nombre, apellido, correo, dpi, telefono, fecha, password, confirmacion, imagen_perfil, ruta_archivo]
    lista_test=[]
    
    return lista_recibida

def recibir_datos_de_crear_cuenta(lista_de_recepcion, frame_nueva_cuenta, cortx, cory, imagen):
    """En esta función se revisa la sintaxis de las entradas de los datos antes de enviarlos, por ejemplo, que
    el nombre solo tenga texto. Los argumentos son: Lista de recepción, frame, posición X, posición Y y la imagen
    retornada por la función:
    1) Primera validación: Guarda el mensaje que se envía como error para las etiquetas.
    2) Sintaxis correcta: Envia True o False, donde True indica que no tiene error y False indica que hay error.
    """
    syntaxis_correcta = []      # Lista para enviar verificación True o False
    lista_recibida = []         # Lista donde se van a almacenar las entradas de texto
    primera_validacion = []     # En esta lista se almacenan los datos que se van a enviar, ya sea las alarmas o los datos escritos

    # Obtiene el valor en cadena de cada dato
    for elemento in lista_de_recepcion[:7]:
        valor = elemento.get()
        lista_recibida.append(valor)
    valor = lista_de_recepcion[7].get()
    lista_recibida.append(valor)
    
    valor = lista_de_recepcion[8]
    lista_recibida.append(valor)
    
    valor = lista_de_recepcion[9]
    lista_recibida.append(valor)
    
    print(lista_recibida[9])
    

    # Guarda cada iteración en una variable
    ver_nombre       = lista_recibida[0]
    ver_apellido     = lista_recibida[1]
    ver_correo       = lista_recibida[2]
    ver_DPI          = lista_recibida[3]
    ver_telefono     = lista_recibida[4]
    ver_fecha        = lista_recibida[5]
    ver_password     = lista_recibida[6]
    ver_confirmacion = lista_recibida[7]
    ver_imagenper    = lista_recibida[8]
    ver_rutaimagen   = lista_recibida[9]

    # Nombre 1
    if ver_nombre.isalpha():
        check = True
        primera_validacion.append(ver_nombre)
        syntaxis_correcta.append(check)
    else:
        check = False
        ver_nombre = "El nombre contiene otros tipos de datos."
        primera_validacion.append(ver_nombre)
        syntaxis_correcta.append(check)

    # Apellido 2
    if ver_apellido.isalpha():
        check = True
        primera_validacion.append(ver_apellido)
        syntaxis_correcta.append(check)
    else:
        check = False
        ver_apellido = "El apellido contiene otros tipos de símbolos."
        primera_validacion.append(ver_apellido)
        syntaxis_correcta.append(check)

    # DPI
    cantidad_digitos_dpi = len(ver_DPI)
    if cantidad_digitos_dpi == 13:
        if ver_DPI.isdigit():
            check = True
            primera_validacion.append(ver_DPI)
            syntaxis_correcta.append(check)
        else:
            check = False
            ver_DPI = "Faltan dígitos de un número de DPI."
            primera_validacion.append(ver_DPI)
            syntaxis_correcta.append(check)
    else:
        check = False
        ver_DPI = "No puede ser un número de DPI."
        primera_validacion.append(ver_DPI)
        syntaxis_correcta.append(check)

    # Fecha de nacimiento 4
    partes = ver_fecha.split('/')
    if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
        if len(partes[0]) in [1, 2] and len(partes[1]) in [1, 2] and len(partes[2]) == 4:
            now = datetime.datetime.now()
            year_actual = now.strftime("%Y")
            year_nacimiento = partes[2]
            year_actual_int = int(year_actual)
            year_nacimiento_int = int(year_nacimiento)
            edad = year_actual_int - year_nacimiento_int

            if 11 <= edad <= 18:
                check = True
                primera_validacion.append(ver_fecha)
                syntaxis_correcta.append(check)
            else:
                check = False
                ver_fecha = "No tiene la edad suficiente."
                primera_validacion.append(ver_fecha)
                syntaxis_correcta.append(check)
        else:
            check = False
            ver_fecha = "Formato de fecha inválido."
            primera_validacion.append(ver_fecha)
            syntaxis_correcta.append(check)
    else:
        check = False
        ver_fecha = "Formato de fecha inválido."
        primera_validacion.append(ver_fecha)
        syntaxis_correcta.append(check)

    # Teléfono
    cantidad_digitos_tel = len(ver_telefono)
    if cantidad_digitos_tel == 8:
        if ver_telefono.isdigit():
            check = True
            primera_validacion.append(ver_telefono)
            syntaxis_correcta.append(check)
        else:
            check = False
            ver_telefono = "No son números."
            primera_validacion.append(ver_telefono)
            syntaxis_correcta.append(check)
    else:
        check = False
        ver_telefono = "No tiene 8 dígitos."
        primera_validacion.append(ver_telefono)
        syntaxis_correcta.append(check)

    # Dirección de correo
    patron = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    if re.match(patron, ver_correo):
        check = True
        primera_validacion.append(ver_correo)
        syntaxis_correcta.append(check)
    else:
        check = False
        ver_correo = "Correo inválido."
        primera_validacion.append(ver_correo)
        syntaxis_correcta.append(check)

    # Contraseña
    carnumero = 0
    carletramayuscula = 0
    carletraminuscula = 0
    car_letras_especiales = 0
    caracteres_especiales = ['!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '[', '*', '{', '}', '/', '+', '-', '.', ',', '.', '-']
    cantidad_digitos = len(ver_password)
    if cantidad_digitos >= 8:
        for posicion in ver_password:
            if 48 <= ord(posicion) <= 57:
                carnumero += 1
            if 'A' <= posicion <= 'Z':
                carletramayuscula += 1
            if 'a' <= posicion <= 'z':
                carletraminuscula += 1
            if posicion in caracteres_especiales:
                car_letras_especiales += 1
        if carnumero >= 1 and carletramayuscula >= 1 and carletraminuscula >= 1 and car_letras_especiales >= 1:
            check = True
            primera_validacion.append(ver_password)
            syntaxis_correcta.append(check)

            # Confirmación
            if ver_password == ver_confirmacion:
                check = True
                primera_validacion.append(ver_confirmacion)
                syntaxis_correcta.append(check)
            else:
                check = False
                ver_confirmacion = "La confirmación no coincide con la contraseña."
                primera_validacion.append(ver_confirmacion)
                syntaxis_correcta.append(check)
        else:
            check = False
            ver_password = "La clave no es válida, debe usar números, letras mayúsculas, minúsculas y símbolos especiales como: !#%..."
            primera_validacion.append(ver_password)
            syntaxis_correcta.append(check)
    else:
        check = False
        ver_confirmacion = "Cantidad de dígitos insuficientes."
        primera_validacion.append(ver_confirmacion)
        syntaxis_correcta.append(check)
        
    #Comprobacion de imagen
    if ver_imagenper is not None:
    # Aquí puedes continuar con el proceso de guardar la imagen
        check = True
        
        # Carga la imagen usando la biblioteca Pillow
        imagen_p = Image.open(ver_rutaimagen)
            
        # Convierte la imagen a bytes
        with io.BytesIO() as output:
            imagen_p.save(output, format='PNG')
            imagen_bytes = output.getvalue()
            primera_validacion.append(imagen_bytes)
            
    
    else:
        check = False
        ver_confirmacion = "No se ha cargado la imagen de perfil."
        primera_validacion.append(ver_confirmacion)
        syntaxis_correcta.append(check)
        
    return primera_validacion, syntaxis_correcta
