from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import glob
import os
import openpyxl


# -------------------funciones principales-------------------------------------


def leer_datos():
    with open('profesor1.txt', 'r') as f:
        datos = f.read().splitlines()
    return datos


def buscar_y_mostrar(variable, listadoA):
    # Obtener el curso seleccionado y eliminar la coma al final
    curso_seleccionado = variable.get().rstrip(',')

    # Limpiar el listbox antes de mostrar nuevos resultados
    listadoA.delete(0, END)

    # Buscar en todos los archivos .txt en la carpeta especificada
    for filename in glob.glob(r'C:\Users\mynor\Desktop\Ingeniería USAC\Semestre 2 Ingeniería 2023\Introducción a la Programación de Computadoras\Proyectos\*.txt'):
        # Ignorar los archivos especificados
        if filename not in ['cursos_disponibles.txt', 'profesor1.txt']:
            with open(filename, 'r') as f:
                # Leer todas las líneas del archivo
                lineas = f.readlines()

                # Comenzar la búsqueda después de la línea 7
                for i in range(7, len(lineas)):
                    # Verificar si el curso_seleccionado está en la línea actual
                    if curso_seleccionado in lineas[i]:
                        # Obtener el nombre del curso
                        nombre_curso = lineas[0].strip()

                        # Mostrar el nombre en el Listbox si no está ya presente
                        if nombre_curso not in listadoA.get(0, END):
                            listadoA.insert(END, nombre_curso)

                        # Agregar el nombre al archivo existente o crear un nuevo archivo si no existe
                        file_path = f'{curso_seleccionado}.txt'
                        if not os.path.isfile(file_path) or nombre_curso not in open(file_path).read():
                            with open(file_path, 'a') as f_curso:
                                f_curso.write(nombre_curso + '\n')


def editar_notas(variable, listadoA):
    curso_seleccionado = variable.get().rstrip(',')

    def guardar_notas():
        # Obtener los valores ingresados
        estudiante_seleccionado = comboEstudiantes.get()
        nota1 = entryNota1.get()
        nota2 = entryNota2.get()
        nota3 = entryNota3.get()

        # Calcular el promedio
        promedio = (float(nota1) + float(nota2) + float(nota3)) / 3

        # Actualizar el archivo del curso con las nuevas notas y el promedio
        with open(f'{curso_seleccionado}.txt', 'r') as curso_file:
            curso_data = curso_file.read().split('\n')

        # Buscar el estudiante y actualizar sus notas y promedio
        for i in range(len(curso_data)):
            estudiante_data = curso_data[i].split(',')
            if estudiante_seleccionado == estudiante_data[0]:
                if len(estudiante_data) >= 4:
                    estudiante_data[1] = nota1
                    estudiante_data[2] = nota2
                    estudiante_data[3] = nota3
                    estudiante_data[4] = str(promedio)
                    curso_data[i] = ', '.join(estudiante_data)
                else:
                    # Si no hay suficientes elementos en estudiante_data, crear uno nuevo con notas y promedio
                    estudiante_data.extend(
                        [nota1, nota2, nota3, str(promedio)])
                    curso_data[i] = ', '.join(estudiante_data)
                break

        with open(f'{curso_seleccionado}.txt', 'w') as curso_file:
            curso_file.write('\n'.join(curso_data))

        # Actualizar el Listbox con los cambios
        buscar_y_mostrar(variable, listadoA)

        # Cerrar la ventana de edición
        ventanaEditar.destroy()

    ventanaEditar = Toplevel(ventanaP)
    ventanaEditar.title(f"Editar Notas - {curso_seleccionado}")

    # Modificar esta sección para obtener los nombres de los estudiantes
    with open(f'{curso_seleccionado}.txt', 'r') as curso_file:
        curso_data = curso_file.read().split('\n')

    estudiantes = [line.split(',')[0] for line in curso_data]

    # Crear una ComboBox para seleccionar el estudiante
    comboEstudiantes = ttk.Combobox(ventanaEditar, values=estudiantes)
    comboEstudiantes.pack()

    # Crear etiquetas (labels) para las actividades
    labelActividad1 = Label(ventanaEditar, text="Actividad 1:")
    labelActividad1.pack()
    entryNota1 = Entry(ventanaEditar)
    entryNota1.pack()

    labelActividad2 = Label(ventanaEditar, text="Actividad 2:")
    labelActividad2.pack()
    entryNota2 = Entry(ventanaEditar)
    entryNota2.pack()

    labelActividad3 = Label(ventanaEditar, text="Actividad 3:")
    labelActividad3.pack()
    entryNota3 = Entry(ventanaEditar)
    entryNota3.pack()

    # Crear un botón para guardar las notas
    botonGuardar = Button(
        ventanaEditar, text="Guardar Notas", command=guardar_notas)
    botonGuardar.pack()

    # Crear un botón para cerrar la ventana de edición
    botonCerrar = Button(ventanaEditar, text="Cerrar",
                         command=ventanaEditar.destroy)
    botonCerrar.pack()


def mostrar_notas(curso_seleccionado):
    ventanaMostrar = tk.Toplevel(ventanaP)
    ventanaMostrar.title(f"Notas del Curso - {curso_seleccionado}")

    # Crear un Treeview para mostrar los datos
    tree = ttk.Treeview(ventanaMostrar, columns=(
        'Nombre', 'Actividad 1', 'Actividad 2', 'Actividad 3', 'Promedio'))
    tree.heading('#1', text='Nombre del Estudiante')
    tree.heading('#2', text='Actividad 1')
    tree.heading('#3', text='Actividad 2')
    tree.heading('#4', text='Actividad 3')
    tree.heading('#5', text='Promedio')

    # Obtener los datos del archivo del curso
    with open(f'{curso_seleccionado}.txt', 'r') as curso_file:
        curso_data = curso_file.read().split('\n')

    for line in curso_data:
        data = line.split(',')
        if len(data) >= 5:
            nombre = data[0]
            actividad1 = data[1]
            actividad2 = data[2]
            actividad3 = data[3]
            promedio = data[4]
            tree.insert('', 'end', values=(nombre, actividad1,
                        actividad2, actividad3, promedio))

    tree.pack()

    # Botón para cerrar la ventana
    botonCerrar = tk.Button(ventanaMostrar, text="Cerrar",
                            command=ventanaMostrar.destroy)
    botonCerrar.pack()


def guardar_notas_en_xlsx(curso_seleccionado):
    # Crear un archivo xlsx
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Notas"

    # Obtener los datos del archivo del curso
    with open(f'{curso_seleccionado}.txt', 'r') as curso_file:
        curso_data = curso_file.read().split('\n')

    # Agregar encabezados
    encabezados = ["Estudiante", "Actividad 1",
                   "Actividad 2", "Actividad 3", "Promedio"]
    sheet.append(encabezados)

    for line in curso_data:
        data = line.split(',')
        if len(data) >= 5:
            nombre = data[0]
            actividad1 = data[1]
            actividad2 = data[2]
            actividad3 = data[3]
            promedio = data[4]
            sheet.append(
                [nombre, actividad1, actividad2, actividad3, promedio])

    # Guardar el archivo xlsx
    wb.save(f'{curso_seleccionado}.xlsx')

    # Mostrar un mensaje de confirmación
    messagebox.showinfo(
        "Éxito", f"Las notas del curso {curso_seleccionado} se han guardado en {curso_seleccionado}.xlsx")

# -----------------------parte gráfica------------------------------------------


def parteG():
    titulo = Label(frameP, text="Bienvenido Profesor",
                   font=("Helvetica", 16), justify="center")
    titulo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    tituloSC = Label(frameP, text="Seleccione el curso")
    tituloSC.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    opciones = leer_datos()
    variable = StringVar(frameP)
    variable.set(opciones[0])  # valor por defecto
    selCurso = OptionMenu(frameP, variable, *opciones)
    selCurso.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    # Llamar a buscar_y_mostrar cuando el valor de variable cambia
    variable.trace('w', lambda *args: buscar_y_mostrar(variable, listadoA))

    listadoA = Listbox(frameP)
    listadoA.grid(row=4, column=1, padx=10, pady=10)

    notasEdit = Button(frameP, text="Editar Notas",
                       command=lambda: editar_notas(variable, listadoA))
    notasEdit.grid(row=2, column=2, padx=10, pady=10, sticky='ew')

    notasRegis = tk.Button(frameP, text="Ver Notas", command=lambda: mostrar_notas(
        variable.get().rstrip(',')))
    notasRegis.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

    notasGuard = tk.Button(frameP, text="Guardar en Excel",
                           command=lambda: guardar_notas_en_xlsx(variable.get().rstrip(',')))
    notasGuard.grid(row=4, column=2, padx=10, pady=10, sticky='ew')


ventanaP = Tk()
frameP = Frame(ventanaP)
frameP.pack()
parteG()

ventanaP.mainloop()
