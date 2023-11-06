from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

import modulo_compartido


def iniciar_interfaz(lienzo_alumnos, color):

    nombre = modulo_compartido.nombre_ingreso

    # ---------------------funciones-----------------------------------------------

    def crear_botones():  # funcion para ingresar a los cursos
        # Leer el archivo del estudiante
        with open(f'{nombre}.txt', 'r') as f:
            lines = f.readlines()

        cursos = lines[7:]  # Los cursos están después de la 7ª línea

        if cursos:  # Verificar si hay cursos
            for i, curso in enumerate(cursos):
                # Calcular la fila y la columna para cada botón
                fila = i // 4 + 2  # Dividir por 5 y sumar 1 para empezar en la fila 2
                columna = i % 4  # Usar el módulo para obtener la columna

                # Crear un botón para cada curso
                boton_curso = Button(
                    aFrame, text=f"Curso {i+1}", cursor="hand2", command=lambda c=curso: mostrar_curso(c), width=20, height=10)
                boton_curso.grid(row=fila, column=columna, padx=90, pady=40)
            return fila
        else:
            return 1

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
                    f.write(
                        f"Certificado\n\nCurso: {curso.strip()}\nNota: {nota}")

        # Botón para generar un certificado
        boton_certificado = Button(
            CursoFrame, text="Generar certificado", command=generar_certificado)
        boton_certificado.pack(padx=10, pady=10)

    def asignacion():
        # Crea una nueva ventana secundaria
        ventana_Asign = Toplevel(bg=color)
        AsignFrame = Frame(ventana_Asign, bg=color)
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

            with open(f"{nombre}.txt", "r") as archivo:
                cursos_existentes = set(archivo.read().splitlines())

            cursos_nuevos = [
                curso for curso in cursos_seleccionados if curso not in cursos_existentes]

            with open(f"{nombre}.txt", "a") as archivo:
                for curso in cursos_nuevos:
                    archivo.write(curso + "\n")

        # Leer los cursos disponibles desde el archivo "cursos_disponibles.txt"
        with open("cursos_disponibles.txt", "r") as archivo:
            cursos_disponibles = [line.strip() for line in archivo.readlines()]

        # Leer los cursos asignados al estudiante desde el archivo del alumno
        with open(f"{nombre}.txt", "r") as archivo:
            cursos_asignados = set(archivo.read().splitlines())

        # Filtrar los cursos disponibles para mostrar solo los no asignados
        cursos_disponibles = [
            curso for curso in cursos_disponibles if curso not in cursos_asignados]

        # Lista para almacenar los cursos seleccionados
        cursos_seleccionados = []

        # ---------parte grafica de la funcion----------------------------------

        # Combobox para seleccionar los cursos
        cursos_combobox = ttk.Combobox(
            ventana_Asign, values=cursos_disponibles)
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
        # Crea una nueva ventana secundaria
        ventana_Desasign = Toplevel()
        DesasignFrame = Frame(ventana_Desasign, bg=color)
        DesasignFrame.pack()

        # Leer el archivo del estudiante
        with open(f'{nombre}.txt', 'r') as f:
            lines = f.readlines()

        # Crear una Listbox para mostrar los cursos
        listbox = Listbox(DesasignFrame)
        # Los cursos están después de la 7ª línea
        for i, line in enumerate(lines[7:]):
            # Insertar cada curso en la Listbox
            listbox.insert(i, line.strip())
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
                with open(f'{nombre}.txt', 'w') as f:
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
        # Eliminar todos los botones dentro del frame
        for widget in aFrame.winfo_children():
            widget.destroy()
        # Actualizar los botones de los cursos
        crear_botones()
        # Destruir la ventana secundaria
        Cerrar_Ventana.destroy()

    # --------------------parte gráfica--------------------------------------------------------------

    def inicializar_botones():
        saludo = Label(
            lienzo_alumnos, text=f"Bienvenido {nombre}", bg=color, font=("Helvetica", 14))
        saludo.place(x=1200, y=20)

        crear_botones()

        botonAsign = Button(lienzo_alumnos, text="Asignación de Cursos",
                            cursor="hand2", command=asignacion, height=4)
        botonAsign.place(x=120, y=600)

        botonDesasign = Button(lienzo_alumnos, text="Desasignación de Cursos",
                               cursor="hand2",  command=desasignacion, height=4)
        botonDesasign.place(x=1150, y=600)

    aFrame = Frame(lienzo_alumnos, bg=color, width=400, height=800)
    aFrame.place(x=50, y=100)
    inicializar_botones()


modulo_compartido.funcion_alumnos = iniciar_interfaz
