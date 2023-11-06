from tkinter import*
#La funcion recibe como parametro el frame, el lienzo, la lista de datos con posibles errores la cordenada inicial
def mensajes(frame_nueva_cuenta, lienzo_nueva_cuenta, lista_recibida, syntaxis_correcta, corx, cory):
    """La funcion crea las etiquetas que dan el error, recibe como parametros: 
    1)El frame_nueva_cuenta donde van a estar las preguntas
    2)El lienzo sobre la cual estan las preguntas
    3)La lista con los mensajes
    5)La lista con las indicaciones de true o false
    6)Las cordenadas X y Y del lienzo
    y retorna -> si hubo o no algun error 
    La diferencia con la funcion mensaje_validacion_2 es que esta funcion solo se le pasa el valor de cordenadas
    iniciales y no en cada etiqueta
    """
    enviar_error = False
    error = False
    for index, validez in enumerate(syntaxis_correcta):     #Si la lista con los valores True False tiene un False de error
        if validez == False:
            #Coloca la etiqueta
            etiquetA1 = Label(frame_nueva_cuenta, text = lista_recibida[index])
            etiquetA1.pack()
            etiquetA1 = lienzo_nueva_cuenta.create_window(corx, cory, anchor = NW, window = etiquetA1)
            error = True        #Devuelve que si hubo error
        cory += 50              #Aumenta 50 la posicion en Y para bajar de posicion
    #Retorna si hubo o no error     
    if error == True: 
        enviar_error = True
        print(enviar_error)
        return enviar_error
    else:
        enviar_error = False
        print(enviar_error)
        return enviar_error

#Coloca una etiqueta en la posicion que se requiera
def mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, mensaje_de_error, corx, cory):
    """La funcion creea una etiqueta que recibe como argumento:
    1) Frame
    2) El lienzo
    3) El mensaje de error
    4) Cordenada en X
    5) Cordenada en Y"""
    etiquetA1 = Label(frame_nueva_cuenta, text = mensaje_de_error)
    etiquetA1.pack()
    etiquetA1 = lienzo_nueva_cuenta.create_window(corx, cory, anchor = NW, window = etiquetA1)
    
    