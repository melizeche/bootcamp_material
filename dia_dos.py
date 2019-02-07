# ejercicio del dia anterior


def suma_lista(numeros):
    suma = 0
    for num in numeros:
        suma = num + suma
    return suma


# definimos una lista de numeros y lo asignamos a la variable pepito
pepito = [1, 2, 3, 4, 5]

# llamamos a la funcion suma_lista pasando como parametro la variable pepito
juancito = suma_lista(pepito)
# que contiene la lista de numeros y el resultado retornado por la funcion y
# lo guardamos en la variable juancito

# Imprimimos el valor de la variable juancito que tiene el resutado de lo
# que retorno suma_lista(pepito)
print(juancito)

# Ej.1  Lista Al cuadrado
# Crear una funcion que reciba una lista de numeros como
# parametro y que retorne una lista con los numeros al cuadrado
# lista_cuadrado(pepito) -> [1,4,9,16,25]

# Ej.2  Suma Lista al cuadrado
# Crear una funcion que reciba una lista de numeros como parametro
# y que retorne la suma de cada numero al cuadrado
# suma_lista_cuadrado(pepito) -> 55


def list_square(lista):
    lista_return = []
    for i in lista:
        lista_return.append(i**2)
    return lista_return


lista_pepito = [1, 2, 3, 4, 5]
list_square(lista_pepito)


def list_square2(lista):
    lista_return = []
    for i in lista:
        cuadrado = i * i
        lista_return.append(cuadrado)
    return lista_return


def list_square3(lista):
    c = 0
    for x in lista:
        lista[c] = x**2
        c = c + 1
    return lista


list_square3(lista_pepito)


def lista_suma(lista_n):
    sumita = 0
    for i in lista_n:
        cuadrado = i * i
        sumita = sumita + cuadrado
    return sumita


lista_n = [2, 4, 6, 8]
lista_suma(lista_pepito)


def cuadrado_lista(lista2):
    lista_n = []
    for i in lista2:
        cuadrado = i**2
        lista_n.append(cuadrado)
    return lista_n


def suma_cuadrado(sc):
    suma = 0
    for z in sc:
        suma = suma + z
    return suma


lista_nueva = [1, 2, 3, 4, 5]
pepito = cuadrado_lista(lista_nueva)
suma_cuadrado(pepito)


def suma_lista2(lista):
    suma = 0
    for z in lista:
        suma = suma + z
    return suma


def cuadrado_lista(lista2):
    lista_n = []
    for i in lista2:
        cuadrado = i**2
        lista_n.append(cuadrado)
    return lista_n


def ej2(listita):
    return suma_lista2(cuadrado_lista(listita))


pepito2 = [1, 2, 3, 4, 5]
ej2(pepito2)

# CONDICIONALES

a = 2
if a > 3:
    print("A es mayor que 3")
else:
    print("A no es mayor que 3")

edad = 18
if edad >= 18:
    print("Podes tomar")
else:
    print("No podes tomar")


def puede_tomar(edad):
    if edad >= 18:
        return True
    else:
        return False


if not puede_tomar(22):
    print("No Puede tomar")
else:
    print("Puede tomar")

# Crear una funcion que reciba un nota del 1 al 100 como argumento y que retorne
# True si el alumno paso el examen, sino que retorne False si se aplazó

# Crear un if que utilize la funcion anterior e imprima un mensaje si el alumno pasó
# o se aplazó


def paso_examen(nota):
    if nota >= 70:
        resultado = True
    else:
        resultado = False
    return resultado


paso_examen(72)

if paso_examen(80) == True:
    print("Paso!")
else:
    print("Se aplazo")


def puede_tomar2(edad):
    if edad > 90:
        print("Podes tomar pero no deberias")
    elif edad >= 18:
        print("Puede Tomar")
    elif edad > 15:
        print("Callado nomas")
    else:
        print("Tu papa se preso")


puede_tomar2(14)

# Crear una funcion que reciba una edad y diga si el alumno deberia estar en prescolar
# primaria, secundaria o universidad


def debe_estar(edad):
    esta = ""
    if edad >= 18:
        esta = "Universidad"
    elif edad > 14:
        esta = "Secundaria"
    elif edad > 6:
        esta = "Primaria"
    else:
        esta = "Preescolar"
    return esta


for edad in range(1, 100):
    print(edad, "años deberia estar en ", debe_estar(edad))


lista_animales = ["perro", "gato", "caballo", "tortuga", "vaca", "pinguino"]

# Dada esta lista, recorrerla y decir si el animal vive en casa de los
# nomadas o no


def casa_de_nomadas(animales):
    if animales == "perro":
        return True
    if animales == "gato":
        return True
    if animales == "caballo":
        return True
    if animales == "tortuga":
        return True
    if animales == "vaca":
        return False
    if animales == "pinguino":
        return True
    else:
        return False


lista_animales = ["perro", "gato", "caballo", "tortuga", "vaca", "pinguino"]
for i in lista_animales:
    if casa_de_nomadas(i):
        print(i, "esta en la CdN")
    else:
        print(i, "No esta en la CdN")


def lista_ani(lista):
    for i in lista:
        if i == "perro" or i == "tortuga" or i == "pinguino":
            print(i, "vive en la CdN")
        else:
            print(i, "no vive en la casa")


lista_ani(lista_animales)

# animales_existentes = ["perro", "gato", "pinguino", "tortuga"]
# animales_por_preguntar = []
# x = 5

# for i in range(x):
#     lista_animales
viven_en_cdn = ["pinguino", "perro", "gato", "tortuga"]
lista_animales = ["perro", "gato", "caballo", "tortuga", "vaca", "pinguino"]
for animal in lista_animales:
    if animal in viven_en_cdn:
        print(animal, "vive en CdN")
    else:
        print(animal, "No vive en CdN")


cuadricula = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
print(cuadricula)

# Pista, usar listas y for
dimension = 3
tablero = []
for a in range(dimension):
    pass
