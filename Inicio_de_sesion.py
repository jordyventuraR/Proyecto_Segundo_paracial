#La pantalla principal la sseleccion de roles 
# Profesor 
# Administracion 
# Alumno 
from tkinter import*

#Creacion la ventana principal
raiz=Tk()
raiz.title("Hogwarts")                  #Titulo
raiz.resizable(True, True)              #Ajustable
raiz.geometry("2160x2160")              #Tamaño por defecto

# Crear un frame y agregarlo a la ventana principal
frame = Frame(raiz)
frame.pack()

#Cargar el icono de la imagen
raiz.iconbitmap("Hogwartsicono.ico")   

#Cargar imagenes
imagen = PhotoImage(file="hogwartsFP.png") 
imagenEsc1=PhotoImage(file="Gryffindor_logo.png")
imagenEsc2=PhotoImage(file="Hufflepuff.png")
imagenEsc3=PhotoImage(file="Slytherin.png")
imagenEsc4=PhotoImage(file="Ravenclaw.png")

#Botones
#Funciones de los botones
def seleccionar_escuela(escuela):
    print(escuela)


def registrarse():
    print("registrase")

def administracion():
    print("Administracion")

# Fondo
lienzo = Canvas(raiz, width=2160, height=2160)
lienzo.pack()

# Mostrar la imagen en el lienzo
lienzo.create_image(0, 0, anchor=NW, image=imagen)

# Crear botones para las escuelas
botonEsc1 = Button(raiz, image=imagenEsc1, command=lambda: seleccionar_escuela("Gryffindor"))
botonEsc2 = Button(raiz, image=imagenEsc2, command=lambda: seleccionar_escuela("Hufflepuff"))
botonEsc3 = Button(raiz, image=imagenEsc3, command=lambda: seleccionar_escuela("Slytherin"))
botonEsc4 = Button(raiz, image=imagenEsc4, command=lambda: seleccionar_escuela("Ravenclaw"))
boton5 = Button(raiz, text="registrarse", command=registrarse, width=10, height=5)
boton6 = Button(raiz, text="administracion", command=administracion, width=10, height=5)

#ubicar los botones
botonEsc1.place(x=493, y=100) 
botonEsc2.place(x=793, y=100)
botonEsc3.place(x=493, y=337) 
botonEsc4.place(x=793, y=337) 
boton5.place(x=650, y=500) 
boton6.place(x=650, y=600)

#Eleva los botones
botonEsc1.lift()
botonEsc2.lift()
botonEsc3.lift()
botonEsc4.lift()
boton5.lift()

raiz.mainloop()
