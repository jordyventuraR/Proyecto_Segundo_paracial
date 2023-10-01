from tkinter import*
def mensajes(lista_recibida, syntaxis_correcta, frame_nueva_cuenta, lienzo_nueva_cuenta):
    
    #Etiqueta
        etiquetA1 = Label(frame_nueva_cuenta, text = "El nombre contiene otro tipo de datos. ")
        etiquetA1.pack()
        etiquetA1 = lienzo_nueva_cuenta.create_window(0, 0, anchor = NW, window = etiquetA1)
        