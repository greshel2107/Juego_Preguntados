import random
#========[Variebles]========
temas = ["",["Historia",
            ["¿De que color era el caballo blanco de Simon Bolivar?","1). marron","2). negro","3). blanco"],
            ["¿Quien fue la primera pareja de Cleopatra?","1). julio cesar","2). marco antonio","3). tutankamon"],
            ["¿Quien es el hijo de Zeus? ","1). Hercules","2). Triton","3). Hades"],
            ["¿Como murio Pablo Escobar?","1). sobredosis","2). choque de auto","3). en un tiroteo"],
            ["¿Que tropas aliadas escaparon de Alemania en Dunquerque?","1). Italia","2). EE.UU","3). Reino Unido"]],
            ["Biologia",
            ["¿Cuantos huesos tiene el cuerpo humano adulto?","1). 206","2). 120","3). 312"],
            ["¿Cuales de estos animales son marsupiales?","1). Kanguro","2). Leon","3). Carpincho"],
            ["¿Cual de estos es un globulo blanco?","1). leucocitos","2). heritrocitos","3). electrolitos"],
            ["¿Cuantas etapas tiene el ciclo del agua?","1). 5","2). 10","3). 155"],
            ["¿Cual de estás sustancias dan una sensación picante en la lengua?","1). Capsaicina","2). Glucosa","3). Leche"]],
            ["Qumica",
            ["¿Cuantos elementos hay en la tabla periodica?","1). 118","2). 122","3). 1302"],
            ["¿Como se llama el elemento Mc?","1). Moscovio","2). Mudanio","3). Macdonium"],
            ["¿cual de estos es equipo de trabajo en el laboratorio quimico?","1). tubos de ensayo","2). sorbete","3). Clavos"],
            ["¿Cual de estos elementos reacciona volatilmente cuando entra en contacto con agua?","1). Potasio","2). Hierro","3). Silicio"],
            ["¿Cual es el elemento más resistente del mundo?","1). Aluminio","2). Diamante","3). Carbono"]],
            ["Ingles",
            ["¿Cuál de estas palabras es 'papa'","1). pineapple","2). Dad","3). Potato"],
            ["¿Cuál va de estás palabras va en la siguiente frase?: 'I want __ eat donuts'","1). To","2). The","3). Could"],
            ["¿Como se pronuncia 'weirdest'?","1). wahr.east4","2). weeuh·duhst","3). wir·dast"],
            ["¿Como se traduce 'Tidy your bed!'?","1). Limpia tu cama!","2). Ordena unas camas!","3). Ordena tu cama!"],
            ["¿Como invitarás a alguien al teatro?","1). Do you want with me to go the teater?","2). Do you want to go to the theater with me?","3). Do you want waches the teater with me?"]]]

correctas = ("3). blanco","1). julio cesar","1). Hercules","3). en un tiroteo","3). Reino Unido",
             "1). 206","1). Kanguro","1). leucocitos","1). 5","1). Capsaicina",
             "1). 118","1). Moscovio","1). tubos de ensayo","1). Potasio","3). Carbono",
             "2). Dad","1). To","2). weeuh·duhst","3). Ordena tu cama!","2). Do you want to go to the theater with me?")

#========[Funciones]========
#mostrar temas
def main ():
    
    print("|||Escoja un tema para jugar|||")
    print("1", "Historia","2","Biologia","3","Quimica","4","Ingles")
    op = input("==> ")
    
    #validar ingreso de dato
    while op == "" or op == "0" or op.isnumeric() == False :
        print("Valor no permitido")
        op = input("==> ")
    
    mostrarPreguntas(op)

def mostrarPreguntas (tema):
    tema = int(tema)
    pe = random.randint(1,5)
    #imrime la pregunta y las opciones
    for i in temas[tema][pe]:
        print(i)
    ingresarRespuestas(tema,pe)
    
def ingresarRespuestas(tema,pe):
    #validar ingreso de datos
    resp = int(input("==> "))
    opciones =(1,2,3)
    
    while resp not in opciones:
        print("Opcion no valida")
        resp = int(input("==> "))
    
    if temas[tema][pe][resp] in correctas:
        print("Correcto")
    else:
        print("Incorrecto")
#========[Principal]==========
while True:
    main()