from tkinter import*
def mensajes(frame_nueva_cuenta, lienzo_nueva_cuenta, lista_recibida, syntaxis_correcta, corx, cory):
    enviar_error = False
    Error = False
    for index, validez in enumerate(syntaxis_correcta):
        if validez == False:
            #Etiqueta
            etiquetA1 = Label(frame_nueva_cuenta, text = lista_recibida[index])
            etiquetA1.pack()
            etiquetA1 = lienzo_nueva_cuenta.create_window(corx, cory, anchor = NW, window = etiquetA1)
            error = True
        cory += 50 
            
    if Error == True: 
        enviar_error = True
        return enviar_error
    else:
        enviar_error = False
        return enviar_error
    