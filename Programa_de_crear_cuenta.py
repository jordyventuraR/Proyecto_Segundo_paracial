from tkinter import*

def nueva_cuenta(numero_de_casa_ganadora, raiz, imagen):
    print("Ya envio a la tercera pantalla")
    #Creacion del frame para el cuestionario
    frame_nueva_cuenta = Frame(raiz) 
    frame_nueva_cuenta.pack()
    
    
    #fondo del frame
    lienzo_nueva_cuenta = Canvas(frame_nueva_cuenta, width=2160, height=2160)
    lienzo_nueva_cuenta.pack()
    lienzo_nueva_cuenta.create_image(0, 0, anchor=NW, image=imagen)
    
