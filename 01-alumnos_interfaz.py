from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

nombre = "Estudiante"  # cambiar esto cuando se solucione: 4)Mostrar el username

# ---------------------funciones-----------------------------------------------


def crear_botones():  # funcion para ingresar a los cursos
    # Leer el archivo del estudiante
    with open('Pamela.txt', 'r') as f:
        lines = f.readlines()

    cursos = lines[7:]  # Los cursos están después de la 7ª línea

    if cursos:  # Verificar si hay cursos
        for i, curso in enumerate(cursos):
            # Calcular la fila y la columna para cada botón
            fila = i // 5 + 2  # Dividir por 5 y sumar 1 para empezar en la fila 2
            columna = i % 5  # Usar el módulo para obtener la columna

            # Crear un botón para cada curso
            boton_curso = Button(
                aFrame, text=f"Curso {i+1}", command=lambda c=curso: mostrar_curso(c))
            boton_curso.grid(row=fila, column=columna, padx=10, pady=10)
        return fila
    else:
        return None


def mostrar_curso(curso):
    # Crea una nueva ventana secundaria
    ventana_curso = Toplevel()
    CursoFrame = Frame(ventana_curso)
    CursoFrame.pack()

    # Mostrar la información del curso
    label_curso = Label(CursoFrame, text=curso.strip())
    label_curso.pack(padx=10, pady=10)

    # Supongamos que la nota es una variable con un valor asignado
    nota = 70

    # Función para generar un certificado si la nota es 61 o más
    def generar_certificado():
        if nota >= 61:
            with open('certificado.txt', 'w') as f:
                f.write(f"Certificado\n\nCurso: {curso.strip()}\nNota: {nota}")

    # Botón para generar un certificado
    boton_certificado = Button(
        CursoFrame, text="Generar certificado", command=generar_certificado)
    boton_certificado.pack(padx=10, pady=10)


def asignacion():
    # Cerrar la ventana principal
    VentanaAlumno.withdraw()
    # Crea una nueva ventana secundaria
    ventana_Asign = Toplevel()
    AsignFrame = Frame(ventana_Asign)
    AsignFrame.pack()

    def agregar_curso():
        curso_seleccionado = cursos_combobox.get()
        if curso_seleccionado and curso_seleccionado not in cursos_seleccionados:
            cursos_seleccionados.append(curso_seleccionado)
            cursos_seleccionados_listbox.insert(tk.END, curso_seleccionado)
            cursos_combobox.set("")  # Limpiar la Combobox

    def quitar_curso():
        seleccion = cursos_seleccionados_listbox.curselection()
        if seleccion:
            cursos_seleccionados_listbox.delete(seleccion)

    def asignar_cursos():
        cursos_seleccionados = cursos_seleccionados_listbox.get(0, tk.END)
        cursos_existentes = set()

        with open("Pamela.txt", "r") as archivo:
            cursos_existentes = set(archivo.read().splitlines())

        cursos_nuevos = [
            curso for curso in cursos_seleccionados if curso not in cursos_existentes]

        with open("Pamela.txt", "a") as archivo:
            for curso in cursos_nuevos:
                archivo.write(curso + "\n")

    # Leer los cursos disponibles desde el archivo "cursos_disponibles.txt"
    with open("cursos_disponibles.txt", "r") as archivo:
        cursos_disponibles = [line.strip() for line in archivo.readlines()]

    # Leer los cursos asignados al estudiante desde el archivo "Pamela.txt"
    with open("Pamela.txt", "r") as archivo:
        cursos_asignados = set(archivo.read().splitlines())

    # Filtrar los cursos disponibles para mostrar solo los no asignados
    cursos_disponibles = [
        curso for curso in cursos_disponibles if curso not in cursos_asignados]

    # Lista para almacenar los cursos seleccionados
    cursos_seleccionados = []

    # ---------parte grafica de la funcion----------------------------------

    # Combobox para seleccionar los cursos
    cursos_combobox = ttk.Combobox(ventana_Asign, values=cursos_disponibles)
    cursos_combobox.pack(padx=10, pady=10)

    # Botón para agregar curso a la lista de cursos seleccionados
    boton_agregar = Button(
        ventana_Asign, text="Agregar Curso", command=agregar_curso)
    boton_agregar.pack(padx=10, pady=10)

    # Listbox para mostrar los cursos seleccionados
    cursos_seleccionados_listbox = Listbox(
        ventana_Asign, selectmode=MULTIPLE)
    cursos_seleccionados_listbox.pack(padx=10, pady=10)

    # Botón para quitar cursos seleccionados
    boton_quitar = Button(
        ventana_Asign, text="Quitar Curso", command=quitar_curso)
    boton_quitar.pack(padx=10, pady=10)

    # Botón para asignar los cursos seleccionados a un archivo .txt
    boton_asignar = Button(
        ventana_Asign, text="Asignar", command=asignar_cursos)
    boton_asignar.pack(padx=10, pady=10)

    # Botón para volver a la ventana principal
    boton_volver = Button(AsignFrame, text="Volver",
                          command=lambda: volver_a_principal(ventana_Asign))
    boton_volver.pack(padx=10, pady=10)


def desasignacion():
    # Cerrar la ventana principal
    VentanaAlumno.withdraw()
    # Crea una nueva ventana secundaria
    ventana_Desasign = Toplevel()
    DesasignFrame = Frame(ventana_Desasign)
    DesasignFrame.pack()

    # Leer el archivo del estudiante
    with open('Pamela.txt', 'r') as f:
        lines = f.readlines()

    # Crear una Listbox para mostrar los cursos
    listbox = Listbox(DesasignFrame)
    # Los cursos están después de la 7ª línea
    for i, line in enumerate(lines[7:]):
        listbox.insert(i, line.strip())  # Insertar cada curso en la Listbox
    listbox.pack(padx=10, pady=10)

    # Función para eliminar cursos seleccionados
    def eliminar_cursos():
        # Mostrar una advertencia con opciones "Sí" y "No"
        respuesta = messagebox.askquestion(
            "Advertencia", "¿Estás seguro de querer desasignarte de este curso?")
        if respuesta == 'yes':
            selected_indices = listbox.curselection()  # Obtener los índices seleccionados
            # Recorrer en orden inverso para evitar problemas de índices
            for i in selected_indices[::-1]:
                # Eliminar la línea correspondiente del archivo
                del lines[i + 7]
                listbox.delete(i)  # Eliminar el curso de la Listbox

            # Escribir las líneas restantes de nuevo en el archivo
            with open('Pamela.txt', 'w') as f:
                f.writelines(lines)

    # Botón para desasignar los cursos seleccionados
    boton_eliminar = Button(
        DesasignFrame, text="Desasignar cursos seleccionados", command=eliminar_cursos)
    boton_eliminar.pack(padx=10, pady=10)

    # Botón para volver a la ventana principal
    boton_volver = Button(DesasignFrame, text="Volver",
                          command=lambda: volver_a_principal(ventana_Desasign))
    boton_volver.pack(padx=10, pady=10)


def volver_a_principal(Cerrar_Ventana):
    # Destruir la ventana secundaria
    Cerrar_Ventana.destroy()
    # Mostrar la ventana principal nuevamente
    VentanaAlumno.deiconify()
    # Actualizar los botones de los cursos
    crear_botones()


def inicializar_botones():
    saludo = Label(
        aFrame, text=f"Bienvenido {nombre}", bg="gray", font=("Helvetica", 14))
    saludo.grid(row=1, column=4, padx=10, pady=10)

    imagen_path = r"C:\Users\mynor\Desktop\Ingeniería USAC\Semestre 2 Ingeniería 2023\Introducción a la Programación de Computadoras\Proyectos\alumnos\pngwing.com.png"
    miImagen = PhotoImage(file=imagen_path)

    perfilImgn = Label(aFrame, image=miImagen)
    perfilImgn.grid(row=1, column=5, padx=10, pady=10)

    # Llamar a la función para crear los botones
    ultima_fila = crear_botones()

    botonAsign = Button(aFrame, text="Asignación de Cursos",
                        cursor="hand2", command=asignacion)
    botonAsign.grid(row=ultima_fila + 3, column=0, padx=10, pady=10)

    botonDesasign = Button(aFrame, text="Desasignación de Cursos",
                           cursor="hand2",  command=desasignacion)
    botonDesasign.grid(row=ultima_fila + 3, column=5,  padx=10, pady=10)

    botonRegresar = Button(aFrame, text="Regresar",
                           cursor="hand2", command=VentanaAlumno.destroy)
    botonRegresar.grid(row=1, column=0,  padx=10, pady=10, sticky="nw")

# --------------------parte gráfica--------------------------------------------------------------


VentanaAlumno = Tk()
VentanaAlumno.title("Hogwarts")
aFrame = Frame(VentanaAlumno, bg="gray")
aFrame.pack()
inicializar_botones()

VentanaAlumno.mainloop()
