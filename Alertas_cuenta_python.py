from tkinter import*
#La funcion recibe como parametro el frame, el lienzo, la lista de datos con posibles errores la cordenada inicial
def mensajes(frame_nueva_cuenta, lienzo_nueva_cuenta, lista_recibida, syntaxis_correcta, corx, cory):
    enviar_error = False
    Error = False
    for index, validez in enumerate(syntaxis_correcta):     #Si la lista con los valores True False tiene un False de error
        if validez == False:
            #Coloca la etiqueta
            etiquetA1 = Label(frame_nueva_cuenta, text = lista_recibida[index])
            etiquetA1.pack()
            etiquetA1 = lienzo_nueva_cuenta.create_window(corx, cory, anchor = NW, window = etiquetA1)
            error = True        #Devuelve que si hubo error
        cory += 50              #Aumenta 50 la posicion en Y para bajar de posicion
    #Retorna si hubo o no error     
    if Error == True: 
        enviar_error = True
        return enviar_error
    else:
        enviar_error = False
        return enviar_error
#Coloca una etiqueta en la posicion que se requiera
def mensajes_validacion_2(frame_nueva_cuenta, lienzo_nueva_cuenta, mensaje_de_error, corx, cory):
    etiquetA1 = Label(frame_nueva_cuenta, text = mensaje_de_error)
    etiquetA1.pack()
    etiquetA1 = lienzo_nueva_cuenta.create_window(corx, cory, anchor = NW, window = etiquetA1)
    
    