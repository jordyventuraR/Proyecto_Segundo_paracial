import tkinter as tk
from tkinter import PhotoImage, Label, OptionMenu, Button, StringVar, Toplevel, messagebox
import openpyxl

# Estructura de datos para almacenar información de cursos y calificaciones
cursos = {
    "Introduccion a la programacion N": {
        "Mynor David Morales Obando": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
        "Jordy Rene Ventura Saquiq": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
    },
    "Introduccion a la programacion D": {
        "Pamela Alessandra Martinez Villegas": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
        "Cristian Alexander Lopez": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
    },
    "Introduccion a la programacion G": {
        "Taco Bebe Hermoso Martínez": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
        "Jose Agusto Martínez Villegas": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
    },
    "Introduccion a la programacion Q": {
        "Roberto Fabio Rodas Esquivel": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
        "Kukulkan Coc": {"Hojas de trabajo": 0, "Tareas": 0, "Examenes": 0, "Calificaciones": 0},
    },
}

# Función para exportar el registro de notas a un archivo Excel
def exportar_registro_notas_a_excel(clase_seleccionada):
    # Crear un nuevo libro de trabajo de Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Obtener la información de calificaciones para la clase seleccionada
    calificaciones_curso = cursos[clase_seleccionada]

    # Escribir encabezados en la hoja de Excel
    actividades = list(calificaciones_curso[list(calificaciones_curso.keys())[0]].keys())
    sheet.append(["Estudiante"] + actividades)

    # Escribir las calificaciones de cada estudiante
    for estudiante, calificaciones in calificaciones_curso.items():
        fila = [estudiante] + [calificaciones[act] for act in actividades]
        sheet.append(fila)

    # Guardar el archivo Excel con un nombre específico
    nombre_archivo = f"Registro_notas_{clase_seleccionada}.xlsx"
    workbook.save(nombre_archivo)

    messagebox.showinfo("Éxito", f"Registro de notas exportado como {nombre_archivo}.")

# Resto de tu código aquí...

# Función para abrir el mosaico de cursos
def abrir_mosaico_cursos():
    # Abre una ventana de mosaico de cursos para la clase seleccionada
    clase_seleccionada = clase_var.get()
    if clase_seleccionada in cursos:
        ventana_mosaicos = tk.Toplevel(ventana)
        ventana_mosaicos.title(f"Mosaicos de {clase_seleccionada}")

        # Banner de bienvenida para la clase
        banner_bienvenida = tk.Label(ventana_mosaicos, text=f"Bienvenido a {clase_seleccionada}!", font=("Helvetica", 20), fg="blue")
        banner_bienvenida.grid(row=0, column=0, columnspan=2)

        # Lista de actividades
        actividades = list(cursos[clase_seleccionada][list(cursos[clase_seleccionada].keys())[0]].keys())

        for i, actividad in enumerate(actividades):
            mosaico_label = tk.Label(ventana_mosaicos, text=actividad, cursor="hand2", font=("Helvetica", 16))
            mosaico_label.grid(row=i+1, column=0)
            mosaico_label.bind("<Button-1>", lambda event, act=actividad: abrir_ventana_actividades(act, clase_seleccionada))
    else:
        messagebox.showerror("Error", "Selecciona una clase válida antes de abrir el mosaico de cursos.")

# Función para abrir la ventana de actividades
def abrir_ventana_actividades(actividad_seleccionada, clase_seleccionada):
    # Abre una ventana de actividades para la actividad seleccionada
    ventana_actividades = tk.Toplevel(ventana)
    ventana_actividades.title(f"{actividad_seleccionada} de {clase_seleccionada}")

    # Puedes personalizar y agregar actividades para la selección actual
    estudiantes = list(cursos[clase_seleccionada].keys())

    for i, estudiante in enumerate(estudiantes):
        tk.Label(ventana_actividades, text=estudiante, font=("Helvetica", 16)).grid(row=0, column=i)

        actividades_estudiante = cursos[clase_seleccionada][estudiante]
        for j, (act, nota) in enumerate(actividades_estudiante.items()):
            tk.Label(ventana_actividades, text=f"{act}: {nota}", font=("Helvetica", 16)).grid(row=j+1, column=i)

# Función para abrir la ventana de edición de cursos
def abrir_edicion_cursos(clase_seleccionada):
    # Abre una ventana para editar cursos de la clase seleccionada
    if clase_seleccionada in cursos:
        ventana_edicion_cursos = tk.Toplevel(ventana)
        ventana_edicion_cursos.title(f"Edición de Cursos de {clase_seleccionada}")

        # Obtener la información del curso seleccionado
        curso_actual = cursos[clase_seleccionada]

        # Crear y configurar widgets para editar la información del curso
        tk.Label(ventana_edicion_cursos, text="Nombre del Curso:", font=("Helvetica", 16)).grid(row=0, column=0)
        nombre_curso_var = tk.StringVar()
        nombre_curso_var.set(clase_seleccionada)
        nombre_curso_entry = tk.Entry(ventana_edicion_cursos, textvariable=nombre_curso_var, font=("Helvetica", 16))
        nombre_curso_entry.grid(row=0, column=1)

        tk.Label(ventana_edicion_cursos, text="Nuevas Actividades:", font=("Helvetica", 16)).grid(row=1, column=0)
        nuevas_actividades_var = tk.StringVar()
        nuevas_actividades_entry = tk.Entry(ventana_edicion_cursos, textvariable=nuevas_actividades_var, font=("Helvetica", 16))
        nuevas_actividades_entry.grid(row=1, column=1)

        def guardar_cambios():
            # Actualizar el nombre del curso si se cambió
            nuevo_nombre_curso = nombre_curso_var.get()
            if nuevo_nombre_curso != clase_seleccionada:
                cursos[nuevo_nombre_curso] = cursos.pop(clase_seleccionada)

            # Agregar nuevas actividades al curso
            nuevas_actividades = nuevas_actividades_var.get().split(",")
            for actividad in nuevas_actividades:
                actividad = actividad.strip()
                if actividad:
                    for curso in cursos[nuevo_nombre_curso].values():
                        curso[actividad] = 0

            messagebox.showinfo("Éxito", "Cambios guardados.")
            ventana_edicion_cursos.destroy()

        guardar_button = tk.Button(ventana_edicion_cursos, text="Guardar Cambios", command=guardar_cambios, font=("Helvetica", 16))
        guardar_button.grid(row=2, column=0, columnspan=2)

# Función para abrir la ventana de registro de notas
def abrir_registro_notas(clase_seleccionada):
    # Abre una ventana de registro de notas de estudiantes para la clase seleccionada
    ventana_registro_notas = tk.Toplevel(ventana)
    ventana_registro_notas.title(f"Registro de Notas de {clase_seleccionada}")

    # Obtener información de calificaciones para la clase seleccionada
    calificaciones_curso = cursos[clase_seleccionada]

    # Crear una variable para seleccionar al estudiante
    estudiante_var = tk.StringVar()
    estudiante_var.set(list(calificaciones_curso.keys())[0])

    # Función para editar la nota del estudiante en la actividad seleccionada
    def editar_nota():
        estudiante_seleccionado = estudiante_var.get()
        actividad_seleccionada = actividad_var.get()
        nueva_nota = nueva_nota_var.get()

        cursos[clase_seleccionada][estudiante_seleccionado][actividad_seleccionada] = nueva_nota

        messagebox.showinfo("Éxito", f"Nota actualizada para {estudiante_seleccionado} en {actividad_seleccionada}.")

    tk.Label(ventana_registro_notas, text="Selecciona un estudiante:", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2)
    estudiante_dropdown = tk.OptionMenu(ventana_registro_notas, estudiante_var, *calificaciones_curso.keys())
    estudiante_dropdown.config(font=("Helvetica", 16))
    estudiante_dropdown.grid(row=1, column=0, columnspan=2)

    # Crear una variable para seleccionar la actividad
    actividad_var = tk.StringVar()
    actividades = list(calificaciones_curso[estudiante_var.get()].keys())
    actividad_var.set(actividades[0])

    tk.Label(ventana_registro_notas, text="Selecciona una actividad:", font=("Helvetica", 16)).grid(row=2, column=0, columnspan=2)
    actividad_dropdown = tk.OptionMenu(ventana_registro_notas, actividad_var, *actividades)
    actividad_dropdown.config(font=("Helvetica", 16))
    actividad_dropdown.grid(row=3, column=0, columnspan=2)

    # Widget para ingresar la nueva nota
    tk.Label(ventana_registro_notas, text="Nueva Nota:", font=("Helvetica", 16)).grid(row=4, column=0)
    nueva_nota_var = tk.StringVar()
    nueva_nota_entry = tk.Entry(ventana_registro_notas, textvariable=nueva_nota_var, font=("Helvetica", 16))
    nueva_nota_entry.grid(row=4, column=1)

    # Botón para editar la nota
    editar_button = tk.Button(ventana_registro_notas, text="Editar Nota", command=editar_nota, font=("Helvetica", 16))
    editar_button.grid(row=5, column=0, columnspan=2)

    # Botón para añadir un nuevo estudiante
    def agregar_estudiante():
        # Lógica para agregar un nuevo estudiante
        nuevo_estudiante_nombre = nuevo_estudiante_var.get()
        if nuevo_estudiante_nombre and nuevo_estudiante_nombre not in calificaciones_curso:
            # Agregar el nuevo estudiante con calificaciones predeterminadas
            calificaciones_curso[nuevo_estudiante_nombre] = {act: 0 for act in actividades}
            estudiante_var.set(nuevo_estudiante_nombre)
            messagebox.showinfo("Éxito", f"Nuevo estudiante '{nuevo_estudiante_nombre}' añadido.")
        else:
            messagebox.showerror("Error", "Ingresa un nombre de estudiante válido y único.")

    nuevo_estudiante_var = tk.StringVar()
    nuevo_estudiante_entry = tk.Entry(ventana_registro_notas, textvariable=nuevo_estudiante_var, font=("Helvetica", 16))
    nuevo_estudiante_entry.grid(row=6, column=0, columnspan=2)
    nuevo_estudiante_button = tk.Button(ventana_registro_notas, text="Añadir Nuevo Estudiante", command=agregar_estudiante, font=("Helvetica", 16))
    nuevo_estudiante_button.grid(row=7, column=0, columnspan=2)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Profesor")

# Etiqueta de título
titulo_label = tk.Label(ventana, text="Interfaz de Profesor", font=("Helvetica", 24), justify="center")
titulo_label.pack(fill="both", expand=True, anchor="center")

# Etiqueta y menú desplegable para seleccionar una clase
clase_label = tk.Label(ventana, text="Selecciona una clase:", font=("Helvetica", 16), justify="center")
clase_label.pack(fill="both", expand=True, anchor="center")
clases = list(cursos.keys())  # Obtener las clases del diccionario de cursos
clase_var = StringVar()
clase_var.set(clases[0])
clase_dropdown = OptionMenu(ventana, clase_var, *clases)
clase_dropdown.config(font=("Helvetica", 16))
clase_dropdown.pack()

# Botones para abrir diferentes funcionalidades
abrir_button_cursos = Button(ventana, text="Abrir Mosaico de Cursos", command=abrir_mosaico_cursos, font=("Helvetica", 16))
abrir_button_cursos.pack(fill="both", expand=True, anchor="center")

abrir_button_edicion_cursos = Button(ventana, text="Editar Cursos", command=lambda: abrir_edicion_cursos(clase_var.get()), font=("Helvetica", 16))
abrir_button_edicion_cursos.pack(fill="both", expand=True, anchor="center")

abrir_button_registro_notas = Button(ventana, text="Registro de Notas", command=lambda: abrir_registro_notas(clase_var.get()), font=("Helvetica", 16))
abrir_button_registro_notas.pack(fill="both", expand=True, anchor="center")

# Botón para exportar el registro de notas a Excel
exportar_button = Button(ventana, text="Exportar Registro de Notas a Excel", command=lambda: exportar_registro_notas_a_excel(clase_var.get()), font=("Helvetica", 16))
exportar_button.pack(fill="both", expand=True, anchor="center")

# Iniciar la ventana principal
ventana.mainloop()