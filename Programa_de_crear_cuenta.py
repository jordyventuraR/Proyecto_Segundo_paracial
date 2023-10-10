from tkinter import*
import re
import datetime

def nueva_cuenta(numero_de_casa_ganadora, frame_nueva_cuenta, lienzo_nueva_cuenta, imagen, nombre, apellido, correo, username, dpi, telefono, fecha, password, confirmacion):
    """La funcion de la nueva cuenta crea las etiquetas y los campos de texto para el registro con la entrada de: 
    1) Nombre completo 
    2) Apellido completo 
    3) DPI
    4)Fecha de nacimiento
    5)Telefono
    6)Direccion de correo
    7)Contraseña
    8)confirmacion
    Y retorna -> el valor de los campos de texto """
    #Posicion de los widgets en la pantalla(X, Y y la posicion va dependiendo de la etiqueta y el campo de texto)
    cortx = 400
    cory = 100
    
    
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
    
    
    #Direccion de correo:
    #Etiqueta
    etiqueta7 = Label(frame_nueva_cuenta, text="Ingrese su direccion de correo: ")
    etiqueta7.pack()
    etiqueta7 = lienzo_nueva_cuenta.create_window(cortx, cory+250, anchor = NW, window = etiqueta7)
        
    #Campo de texto
    entrada7 = Entry(frame_nueva_cuenta, textvariable = correo)
    entrada7.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+250, anchor = NW, window = entrada7)
    
    
    #Contraseña:
    #Etiqueta
    etiqueta8 = Label(frame_nueva_cuenta, text="Ingrese su contraseña: ")
    etiqueta8.pack()
    etiqueta8 = lienzo_nueva_cuenta.create_window(cortx, cory+300, anchor = NW, window = etiqueta8)
        
    #Campo de texto
    entrada8 = Entry(frame_nueva_cuenta, textvariable = password, show = "*")
    entrada8.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+300, anchor = NW, window = entrada8)
    
    
    #Confirmacion:
    #Etiqueta
    etiqueta9 = Label(frame_nueva_cuenta, text="Reafirme su password: ")
    etiqueta9.pack()
    etiqueta9 = lienzo_nueva_cuenta.create_window(cortx, cory+350, anchor = NW, window = etiqueta9)
        
    #Campo de texto
    entrada9 = Entry(frame_nueva_cuenta, textvariable = confirmacion, show = "*")
    entrada9.pack()
    lienzo_nueva_cuenta.create_window(cortx+200, cory+350, anchor = NW, window = entrada9)
    
    
    #fondo del frame
    lista_recibida = [nombre, apellido, correo, dpi, telefono, fecha, password, confirmacion]
    return lista_recibida
    

#Funcion que imprime los datos que se escribieron en el campo de texto   
def recibir_datos_de_crear_cuenta (lista_de_recepcion, frame_nueva_cuenta, cortx, cory, imagen):
    """En esta funcion se revisa la syntaxis de las entradas de los datos antes de enviarlos por ejemplo que
    el nombre solo tenga texto, los argumentos son: Lista de recepcion, frame, posicion X, Posicion Y y la imagen
    lo retornada por la funcion->: 
    1) Primera validacion: Guarda el mensaje que se envia como error para las etiquetas  
    2) syntaxis correcta: Envia True o False y esto donde True indica que no tiene error y False: indica que hay error
    """
    syntaxis_correcta = []      #Lista para enviar verificacion True o False      
    lista_recibida = []         #Lista donde se van almacenar las entradas de texto
    primera_validacion = []     #En esta lista se almacena los datos que se van a enviar ya sea las alarmas o los datos escritos
    #Obtiene el valor en string de cada datos
    for elemento in lista_de_recepcion: 
        valor = elemento.get()
        lista_recibida.append(valor)
    
    #Guarda cada iteracion en una variable
    ver_nombre = lista_recibida[0]
    ver_apellido = lista_recibida[1]
    ver_correo = lista_recibida[2]
    ver_DPI = lista_recibida[3]
    ver_telefono = lista_recibida[4]
    ver_fecha = lista_recibida[5]
    ver_password = lista_recibida[6]
    ver_confirmacion = lista_recibida[7]
    
    #Nombre
    if ver_nombre.isalpha():                    #Si el nombre es totalmente texto
        check = True
        primera_validacion.append(ver_nombre)
        syntaxis_correcta.append(check)
    else:
        #Etiqueta
        check = False
        ver_nombre =  "El nombre contiene otro tipo de datos. "
        primera_validacion.append(ver_nombre)     #Guarda la variable con la correccion
        syntaxis_correcta.append(check)           #Guarda el estado de false
        
    #Apellido
    if ver_apellido.isalpha():
        check = True
        primera_validacion.append(ver_apellido)
        syntaxis_correcta.append(check)
        
    else:
        #Etiqueta
        check = False
        ver_apellido =  "El apellido contiene otro tipo de simbolos"
        primera_validacion.append(ver_apellido)
        syntaxis_correcta.append(check)
        
        
    #DPI
    cantidad_diguitos_dpi = len(ver_DPI)        #obtiene la longitud de caracteres
    if cantidad_diguitos_dpi == 13:             #Si tiene 13 diguitos
        if ver_DPI.isdigit():                   #Si solo son numeros
            check = True                        #Correcto
            primera_validacion.append(ver_DPI)  
            syntaxis_correcta.append(check)
        else:                                               #Error por no tener el numero correcto de diguitos
            check = False                                   
            ver_DPI = "Faltan diguitos de un numero de DPI"
            primera_validacion.append(ver_DPI)
            syntaxis_correcta.append(check)
            
    else:
        check = False
        ver_DPI = "No puede ser un numero de DPI"              #Posee datos no numericos
        primera_validacion.append(ver_DPI)
        syntaxis_correcta.append(check)
    
    
    #Fecha de nacimiento
    # Dividir la cadena en partes usando '/' como separador
    partes = ver_fecha.split('/')  
    #Verificar si hay exactamente 3 partes y si las partes 0, 1 y 2 son dígitos
    if len(partes) == 3 and partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
        #Verificar que las partes 0, 1 y 2 tengan longitudes válidas (2, 2, y 4 caracteres respectivamente)
        if len(partes[0]) in [1, 2] and len(partes[1]) in [1, 2] and len(partes[2]) == 4:
            
            #!Verificacion
            now = datetime.datetime.now()                 #Obtiene la fecha actual
            year_actual = now.strftime("%Y")              #Obtiene el año actual
            year_nacimiento = partes[2]                   #Guarda el año de la fecha de nacimiento
            year_actual_int = int(year_actual)            #Pasa el año a enteros
            year_nacimiento_int = int(year_nacimiento)    #Pasa el año de nacimiento a enteros
            edad = year_actual_int - year_nacimiento_int  #Obtiene la edad
        

            #La edad valida para registrarse es de 11 a 18 años
            if 11 <= edad <= 18:
                check = True
                primera_validacion.append(ver_fecha)
                syntaxis_correcta.append(check)
            
            #No tiene edad suficiente    
            else:
                check = False
                ver_fecha = "No tiene la edad suficiente"
                primera_validacion.append(ver_fecha)
                syntaxis_correcta.append(check)
                
        #No tiene adecuadamente el formato de fecha    
        else:
            check = False
            ver_fecha = "formato de  fecha invalida"
            primera_validacion.append(ver_fecha)
            syntaxis_correcta.append(check)
            
    #El formato de fecha no es valido      
    else:
        check = False
        ver_fecha = "formato de  fecha invalida"
        primera_validacion.append(ver_fecha)
        syntaxis_correcta.append(check)    
    
    
    # Telefono
    cantidad_digitos_tel = len(ver_telefono)        #Obtiene la cantidad de diguitos
    if cantidad_digitos_tel == 8:                   #Debe de ser igual a 8
        if ver_telefono.isdigit():
            #Etiqueta
            check = True                             #El numero es correcto
            primera_validacion.append(ver_telefono)
            syntaxis_correcta.append(check)
            
        else:
            #Etiqueta
            check = False                             #Tiene caracteres no validos
            ver_telefono = "No son numeros"
            primera_validacion.append(ver_telefono)
            syntaxis_correcta.append(check)
    else:
        #Etiqueta
        check = False                                 #No posee que 8 diguitos
        ver_telefono = "No tiene 8 digitos"
        primera_validacion.append(ver_telefono)
        syntaxis_correcta.append(check)
    
        
    #Direccion de correo
    # Patrón de expresión regular para validar un correo de Gmail
    patron = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'          #Verifica que lo ingresado sea .@gmail.com
    
    if re.match(patron, ver_correo):
        check = True                                    #El correo posee ese formato
        primera_validacion.append(ver_correo)
        syntaxis_correcta.append(check)
        
    else:
        check = False                                   #No posee ese formato
        ver_correo = "Correo invalido"
        primera_validacion.append(ver_correo)
        syntaxis_correcta.append(check)
        

    # #Contraseña
    carnumero = 0
    carletramayuscula = 0
    carletraminuscula = 0
    car_letras_especiales = 0
    caracteres_especiales = ['!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '[', '*', '{', '}', '/', '+', '-', '.', ',', '.', '-'] #Simbolos considerados especiales
    cantidad_diguitos = len(ver_password)       #Obtiene la cantidad de diguitos          
    
    if cantidad_diguitos >= 8:                  #Debe de tener mas de 8 diguitos
        for posicion in ver_password:                       
            if 48 <= ord(posicion) <= 57:
                carnumero += 1
            if 'A' <= posicion <= 'Z':
                carletramayuscula += 1
            if 'a' <= posicion <= 'z':
                carletraminuscula += 1
            if posicion in caracteres_especiales:
                car_letras_especiales += 1
        if carnumero >= 1 and carletramayuscula >= 1 and carletraminuscula >= 1 and car_letras_especiales >= 1:     #La contraseña debe de poseer como minimo un caracter especial, un caracter en Mayuscula y uno en minuscula
            check = True                                
            primera_validacion.append(ver_password)
            syntaxis_correcta.append(check)
            
            #Confirmacion
            if ver_password == ver_confirmacion:                #Si la confirmacion  es igual a la contraseña
                check = True
                primera_validacion.append(ver_confirmacion)
                syntaxis_correcta.append(check)
                
            else:
                check = False
                ver_confirmacion = "La confirmacion no es igual que el password"
                primera_validacion.append(ver_confirmacion)
                syntaxis_correcta.append(check)
            
        else:
            check = False
            ver_password = "La clave no es valida debe de usar numeros, letras mayusculas, minusculas, y simbolos especiales como: !#%..."
            primera_validacion.append(ver_password)
            syntaxis_correcta.append(check)         
    else:
        check = False
        ver_confirmacion = "Cantidad de diguitos insuficientes"
        primera_validacion.append(ver_confirmacion)
        syntaxis_correcta.append(check)
    
    return primera_validacion, syntaxis_correcta
    
    