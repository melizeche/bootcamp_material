# Creamos una variable nombre con el valor "Marce"
nombre = "Marce"

# Creamos una lista que contiene la variable nombre y un numero
persona = [nombre, 32]
print(persona)  # Imprime el contenido de la lista persona -> ['Marce', 32]

# len() se utiliza para saber cuantos elementos tiene algo(de lenght en ingles)
cantidad = len(persona)  # resultado: 2 elementos
# Mezclamos texto/strings con la variable cantidad
print("La lista persona tiene", cantidad, "elementos")

# Agregamos un elemento mas a la lista persona con .append()
persona.append("programador")
print(persona)
# obtenemos la nueva cantidad de elementos de la lista persona
cantidad2 = len(persona)
print("La lista persona tiene", cantidad2, "elementos")

# Imprimir el ultimo elemento de una lista sin saber cuantos elementos tiene
cantidad = len(persona)
indice = 0
print(persona[indice])
# Entonces el ultimo elemento es la cantidad de elementos - 1
# porque el indice de la lista empieza en 0
indice_ultimo = cantidad - 1
print(persona[indice_ultimo])

# En Python los indices negativos recorren la lista de atras para adelante
print(persona[-1])
print(persona[-2])

print(persona)

# Insert deja elegir en que posicion insertar el elemento nuevo
persona.insert(0, "Mr")
print(persona)


# LOOPS / Bucles

lista_temas = ["variables", "tipos", "listas"]

# En Python el bucle for recorre una lista o un rango,
# en  el siguiente ejemplo la variable `concepto` (que podria tener cualquier otro
# nombre) por cada ciclo o repeticion va a ir tomando los valores de la
# lista `lista temas`
for concepto in lista_temas:
    print("Hoy aprendi", concepto)
    print("Que gusto!")
print("Esto es lo que aprendi")
# Todo lo que va identado(el espacio) bajo el for es el bloque de codigo
# que se va a ejecutar en cada repeticion del for

# range(10) genera una secuencia de numeros del 0 al 9
# range(1,10)
for i in range(1, 11):
   print(i)

for pepito in range(10):
    print("Hola Mundo!")

# Crear una lista de 6 numeros, recorrerla con un for e imprimir el numero
lista_numeros = [1, 2, 3, 4, 5, 6]
suma = 0
for i in lista_numeros:
    suma = suma + i

print(suma)


# Crear un acumulador que de la multiplicacion de una lista de numeros

lista_numeros = [1, 2, 3, 4, 5, 6]
multi = 1

for factor in lista_numeros:
    print(multi, "*", factor)
    multi = multi * factor
    print(multi)
print(multi)


def saludo(nombre):
    print("Hola", nombre)


def saludo2(nombre, edad):
    print("Hola", nombre, "tenes", edad, "anhos")

saludo2("Marcelo", 32)
saludo2(32, "Marcelo")

saludo("Marcelo")


def suma_numeros(num1, num2):
    suma = num1 + num2
    return suma

pepito = suma_numeros(3, 4)
print(pepito)


def division(dividendo, divisor):
    return dividendo / divisor

division(20, 5)
division(5, 20)

# Crear una funcion retorne un numero al cuadrado


def al_cuadrado(numero):
    return numero * numero

al_cuadrado(6)


def saludo3(nombre, edad=0):
    print("Hola", nombre, "tenes", edad, "anhos")

saludo3("Marce")
saludo3("Marce", 32)


def saludo(nombre, edad):
    pepito = nombre * 5
    print("Hola", pepito, "tenes", edad, "anhos")


saludo("Marce", 32)
nombre = "Juan"
edad = 22
print(nombre, edad)


def saludo4(nombre="", edad=""):
    print("Hola", nombre, "tenes", edad, "anhos")

saludo4(edad=32, nombre="Marce")

2**3  # dos al cubo
3**5  # tres a la quinta potencia

# Crear una funcion con parametros nombrados que eleve un numero a una
# potencia

# Crear una funcion que reciba como parametro una lista de numeros que
# retorne la suma de los numeros

lista_numeros = [1, 2, 3, 4, 5, 6]


def suma_lista(.........
    # Esto es lo que hay que completar
    # mas codigo
    for ...:
        # esto es lo que esta adentro del for, lo que se va a repetir

    return  # algo


# Asi se le llama a la funcion
lista_x = [1, 2, 30, 5, 1]
suma_lista()
# este ejemplo deberia retornar 39 porque 1+2+30+5+1=39
