from random import randint

def definir_celda():
    num = randint(0,1)
    return num

def crear_grilla(size):
    grilla = []
    for fila in range(size):
        grilla.append([])
        for columna in range(size):
            grilla[fila].append(definir_celda())
    return grilla

def print_grilla(grilla):
    for fila in grilla:
        print(fila)
# Ej.1
# Crear una funcion que reciba como parametro 
# una grilla, una posicion X y una posicion Y
# y que cambie ese elemento a "-" y retorne la grilla cambiada
grilla = crear_grilla(6)

def cambiar_elemento(grilla,fila,columna):
    grilla[fila][columna]="-"
    return grilla

# cambiar_elemento(grilla,8,2)
# print_grilla(grilla)

def esta_vivo(celda):
    if celda==1:
        return True
    else:
        return False

# Crear una funcion que reciba la lista como argumento
#  y Recorra la grilla (con fors) y cuente cuantas celulas
#  vivas hay (usar funcion esta_vivo() para esto)
# def contador_vivos(una_grilla):
#     size = len(una_grilla) #Si le pasas una grilla de 5x5 size va a ser 5
#     for fila in range(size):
#         for columna in range...


def vivos(grilla):
    contador = 0
    for fila in grilla:
        for celda in fila:
            if esta_vivo(celda)==True:
                contador = contador + 1
    return contador


print_grilla(grilla)

def contador_vivos(grilla):
    size = len(grilla)
    cuenta=0
    for fila in range(size):
        for columna in range(size):
            if esta_vivo(grilla[fila][columna])==True:
                cuenta = cuenta + 1
    return cuenta

def make_emoji_grid(grilla):
    size = len(grilla)
    for fila in range(size):
        for columna in range(size):
            if esta_vivo(grilla[fila][columna])==True:
                grilla[fila][columna]="🐧"
            else:
                grilla[fila][columna]="💀"
    return grilla
print(contador_vivos(grilla))
print_grilla(make_emoji_grid(grilla))
