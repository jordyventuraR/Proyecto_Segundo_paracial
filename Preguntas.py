from tkinter import*  

#La funcion para hacer una pregunta a travez de una etiqueta
def preguntas(frame, text, lienzo, varx, vary):
    pregunta = Label(frame, text=text)
    pregunta.pack()
    pregunta.cuestionario=lienzo.create_window(varx, vary, anchor=NW, window=pregunta)
    
    
#La opciones la coloca por Radiobutton
def opciones(frame, text, variable, lienzo, varx, vary, value):
    dec=Radiobutton(frame, text=text, value=value, variable=variable)
    dec.pack()
    dec.cuestionario=lienzo.create_window(varx, vary, anchor=NW, window=dec)
    

#La funcion enviar
def enviar(datos, frame):
    """Devuelve el valor de la casa ganadora por ende recibe como parametro:
    1) datos: le sirve para obtener los valores de las respuestas de cada pregunta
    2) El frame: el cual lo destruye
    
    como retorno entrega: ->El nombre de la casa ganadora o el estado False el cual indica 
    que algunas de las preguntas no fue respondida"""
    #Declaracion de las variables para el conteo
    Gryffindor=0
    Hufflepuff=0
    Ravenclaw=0
    Slytherin=0
    
    #obtiener el  valor de cada opcion seleccionada donde todas las respuestas  a pertenecen a una escuela
    decisiones = [decision.get() for decision in datos]
    
    #Hace la revision de si todas las preguntas tiene respuestas
    for value in decisiones:
        if value==0:
            print("Hay preguntas que no fueron resueltas")
            return False
    #En caso de que si todas tienen solucion   
    for value in decisiones:
        if value == 1:                  #Si el participante ingreso respuestas con referencia a opcion 1
            Gryffindor+=1
        elif value == 2:                #Si el participante ingreso respuestas con referencia a opcion 2
            Hufflepuff=1+Hufflepuff
        elif value == 3:                #Si el participante ingreso respuestas con referencia a opcion 3
            Ravenclaw=1+Ravenclaw
        else:                           ##Si el participante ingreso respuestas con referencia a opcion 4
            Slytherin=1+Slytherin       
            
    casas = [Gryffindor, Hufflepuff, Ravenclaw, Slytherin] #Guarda en una lista el valor que obtuvo en cada opcion
    casa_ganadora = max(casas)                             #Obtiene la que tuvo mayor resultado
    
    #Destruye el frame 
    frame.destroy()
    #Compara si el valor que obtuvo cada casa es igual al valor de la casa mas grande y retorna esa respuesta(La casa ganadora)
    if Gryffindor==casa_ganadora:
        return "Gryffindor es la casa ganadora"
    elif Hufflepuff==casa_ganadora:
        return "Hufflepuff es la casa ganadora"
    elif Ravenclaw==casa_ganadora:
        return "Ravenclaw"
    elif Slytherin==casa_ganadora:
        return "Slytherin"
    
#la funcion cuestionario
def cuestionario(raiz, imagen, frame, lienzo):
    
    #Titulo
    label = Label(frame, text="Cuestionario para la eleccion de escuela")
    label.pack()
    label.cuestionario=lienzo.create_window(400, 0, anchor=NW, window=label)
    
    
    #pregunta 1   
    decision1=IntVar()
    preguntas(frame, "Qué tipo de libro prefieres leer?", lienzo, 100, 50)
    opciones(frame, "a) Aventuras emocionantes y llenas de peligros.", decision1, lienzo, 100, 80, 1)
    opciones(frame, "b) Historias sobre amistad y lealtad.", decision1, lienzo, 100, 110, 2)
    opciones(frame, "c) Libros que desafían tu mente e intelecto.", decision1, lienzo, 100, 140, 3)
    opciones(frame, "d) Narrativas intrigantes y astutas.", decision1, lienzo, 100, 170, 4)
    
    
    #pregunta 2
    decision2=IntVar()
    preguntas(frame, "¿Qué cualidad te parece más admirable?", lienzo, 100, 305)
    opciones(frame, "a) Valentía.", decision2, lienzo, 100, 335, 1)
    opciones(frame, "b) Lealtad.", decision2, lienzo, 100, 365, 2)
    opciones(frame, "c) Inteligencia.", decision2, lienzo, 100, 395, 3)
    opciones(frame, "d) Astucia.", decision2, lienzo, 100, 425, 4)
    
    
    #Pregunta 3
    decision3=IntVar()
    preguntas(frame, "¿Cuál es tu idea de una actividad perfecta en tu tiempo libre?", lienzo, 100, 530)
    opciones(frame, "a) Practicar deportes o actividades físicas.", decision3, lienzo, 100, 560, 1)
    opciones(frame, "b) Pasar tiempo con amigos y seres queridos. ", decision3, lienzo, 100, 590, 2)
    opciones(frame, "c) Leer un buen libro o aprender algo nuevo.", decision3, lienzo, 100, 620, 3)
    opciones(frame, "d) Resolver enigmas o estrategias.", decision3, lienzo, 100, 650, 4)
    
    
    #pregunta 4
    decision4=IntVar()
    preguntas(frame, "¿Cómo enfrentas los desafíos en la vida?", lienzo, 540, 50)
    opciones(frame, "a) Con valentía y decisión.", decision4, lienzo, 540, 80, 1)
    opciones(frame, "b) Con determinación y persistencia..", decision4, lienzo, 540, 110, 2)
    opciones(frame, "c) Analizando cuidadosamente y usando tu conocimiento.", decision4, lienzo, 540, 140, 3)
    opciones(frame, "d) Usando tu astucia y determinación.", decision4, lienzo, 540, 170, 4)

    
    #pregunta 5
    decision5=IntVar()
    preguntas(frame, "¿Qué tipo de mascota preferirías tener?", lienzo, 540, 305)
    opciones(frame, "a) León.", decision5, lienzo, 540, 335, 1)
    opciones(frame, "b) Perro.", decision5, lienzo, 540, 365, 2)
    opciones(frame, "c) Búho.", decision5, lienzo, 540, 395, 3)
    opciones(frame, "d) Serpiente.", decision5, lienzo, 540, 425, 4)
    
    
    #pregunta 6
    decision6=IntVar()
    preguntas(frame, "¿Qué asignatura escolar disfrutas más?", lienzo, 540, 530)
    opciones(frame, "a) Defensa Contra las Artes Oscuras.", decision6, lienzo, 540, 560, 1)
    opciones(frame, "b) Cuidado de las Criaturas Mágicas.", decision6, lienzo, 540, 590, 2)
    opciones(frame, "c) Historia de la Magia.", decision6, lienzo, 540, 620, 3)
    opciones(frame, "d) Pociones.", decision6, lienzo, 540, 650, 4)
    
    
    #pregunta 7
    decision7=IntVar()
    preguntas(frame, "¿Cómo te sientes en una gran fiesta o reunión social?", lienzo, 980, 50)
    opciones(frame, "a) Disfruto y me sumerjo en la diversión.", decision7, lienzo, 980, 80, 1)
    opciones(frame, "b) Me siento cómodo rodeado de amigos.", decision7, lienzo, 980, 110, 2)
    opciones(frame, "c) Me gusta tener conversaciones interesantes.", decision7, lienzo, 980, 140, 3)
    opciones(frame, "d) Observo y evalúo la situación cuidadosamente.", decision7, lienzo, 980, 170, 4)
    
    
    #pregunta 8
    decision8=IntVar()
    preguntas(frame, "¿Qué cualidad crees que te define mejor?", lienzo, 980, 305)
    opciones(frame, "a) Coraje.", decision8, lienzo, 980, 335, 1)
    opciones(frame, "b) Lealtad.", decision8, lienzo, 980, 365, 2)
    opciones(frame, "c) Inteligencia.", decision8, lienzo, 980, 395, 3)
    opciones(frame, "d) Astucia.", decision8, lienzo, 980, 425, 4)
    
    
    #pregunta 9
    decision9=IntVar()
    preguntas(frame, "¿Qué tipo de entorno prefieres para estudiar o trabajar?", lienzo, 980, 530)
    opciones(frame, "a) Un lugar lleno de actividad y emoción.", decision9, lienzo, 980, 560, 1)
    opciones(frame, "b) Un ambiente cálido y acogedor.", decision9, lienzo, 980, 590, 2)
    opciones(frame, "c) Un espacio tranquilo y ordenado.", decision9, lienzo, 980, 620, 3)
    opciones(frame, "d) Un lugar estratégico y desafiante.", decision9, lienzo, 980, 650, 4)
    
    #lista de variables que se van a enviar como parametro
    datos=[decision1, decision2, decision3, decision4, decision5, decision6, decision7, decision8, decision9]
    #Envia los datos
    return datos


    
    
    
    