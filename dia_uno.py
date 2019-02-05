# Toda linea que empiece con # es un comentario y la computadora va a ignorar

# Creamos una variable nombre con el valor "Marce"
# El operador `es igual` = es el operador de asignacion
nombre = "Marce"
# Imprimimos en pantlla el valor de la variable nombre
print(nombre)

# Creamos una lista que contiene la variable nombre y un numero
# para definir una lista se usan los corchetes -> [] y los elementos se separan
# con comas
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
# en el siguiente ejemplo la variable `concepto` (que podria tener cualquier otro
# nombre) por cada ciclo o repeticion va a ir tomando los valores de la
# lista `lista temas`, en este ejemplo el bucle for va a tener 3 repeticiones
# porque es la cantidad de elementos que tiene `lista_temas`
for concepto in lista_temas:
    print("Hoy aprendi", concepto)
    print("Que gusto!")
print("Esto es lo que aprendi")
# Todo lo que va identado(el espacio) bajo el for es el bloque de codigo
# que se va a ejecutar en cada repeticion del for, lo que no este identado
# (como el ultimo print)no pertenece a ese for en particular

# range(10) genera una secuencia de numeros del 0 al 9
# range(1,10) genera una secuencia de numeros del 1 al 9
# range(1,11) genera una secuencia de numeros del 1 al 10

# Por cada repeticion/iteracion del siguiente for la variable i toma el valor
# de la secuencia retornada por range, en este caso del 1 al 10, y lo imprime
for i in range(1, 11):
    print(i)

# El ejemplo de arriba seria equivalente a esto:
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# La variable del for puede tener cualquier nombre e inclusive podemos no usarla
# este for va a imprimir en pantalla "Hola Mundo!" 10 veces
for pepito in range(10):
    print("Hola Mundo!")

# Crear una lista de 6 numeros, recorrerla con un for e imprimir la suma de
# los numeros de la lista
lista_numeros = [1, 2, 3, 4, 5, 6]
suma = 0
for i in lista_numeros:
    suma = suma + i

print(suma)

# Lo de arriba es un ejemplo de un acumulador, se inicializa la variable con 0
# y luego dentro del bucle se suma a si misma mas el valor a acumular

# Crear un acumulador que de la multiplicacion de una lista de numeros

lista_numeros = [1, 2, 3, 4, 5, 6]
multi = 1

for factor in lista_numeros:
    print(multi, "*", factor)
    multi = multi * factor
    print(multi)
print(multi)


# FUNCIONES
# Una función es un bloque de código con un nombre asociado, que recibe cero o más argumentos
# como entrada, sigue una secuencia de sentencias, la cuales ejecuta una
# operación deseada y devuelve un valor y/o realiza una tarea,
# este bloque puede ser llamado cuando se necesite.

# Para definir una funcion se utiliza def ej:

# def NOMBRE_DE_LA_FUNCION(LISTA_DE_PARAMETROS):
#     CODIGO( ej. asignacion de variables, operaciones, bucles, )
#     RETURN VALOR_A_RETORNAR

# La siguiente funcion tiene como nombre `saludo` y reciba un argumento `nombre`
# e imprime en pantalla `Hola [valor de nombre]`
def saludo(nombre):
    print("Hola", nombre)
# Lo de arriba es la definicion de la funcion, esto nunca se ejecuta hasta que
# se llama a la funcion, para llamar a una funcion hay que poner el nombre de la
# funcion seguido de parentesis, si la funcion espera un argumento hay que poner
# el valor del argumento dentro de los parentesis


saludo("RAMONCITO")  # esto imprimiria en pantalla `Hola RAMONCITO`

# Una funcion puede tener n numero de argumentos o no tener ninguno,
# estos son posicionales, por eso es importante el orden


def saludo2(nombre, edad):
    print("Hola", nombre, "tenes", edad, "años")


saludo2("Marcelo", 32)  # Esto imprimiria `Hola Marcelo tenes 32 años`
saludo2(32, "Marcelo")  # Esto imprimiria `Hola Marcelo32 tenes Marcelo años`


# La siguiente funcion recibe 2 argumentos y retorna el valor de su suma
def suma_numeros(num1, num2):
    suma = num1 + num2
    return suma

# Utilizamos return para retornar el valor, de esta forma podemos utilizarlo
# como en el siguiente ejemplo guardamos el valor de retorno(la suma de los
# numeros en los argumentos al llamar a la funcion) en la variable pepito


pepito = suma_numeros(3, 4)
print(pepito)  # esto imprime el valor de pepito que es 7


def division(dividendo, divisor):
    return dividendo / divisor


division(20, 5)  # 20  divido 5
division(5, 20)  # 5 divido 20

# Crear una funcion retorne un numero al cuadrado


def al_cuadrado(numero):
    return numero * numero


al_cuadrado(6)

# Se puede asignar un valor por defecto a los argumentos


def saludo3(nombre, edad=0):
    print("Hola", nombre, "tenes", edad, "anhos")


saludo3("Marce")
saludo3("Marce", 32)


def saludo4(nombre, edad):
    pepito = nombre * 5
    print("Hola", pepito, "tenes", edad, "anhos")


saludo4("Marce", 32)
nombre = "Juan"
edad = 22
print(nombre, edad)


def saludo5(nombre="", edad=""):
    print("Hola", nombre, "tenes", edad, "anhos")


saludo5(edad=32, nombre="Marce")

2**3  # dos al cubo
3**5  # tres a la quinta potencia

# Crear una funcion con parametros nombrados que eleve un numero a una
# potencia

# Crear una funcion que reciba como parametro una lista de numeros que
# retorne la suma de los numeros

lista_numeros = [1, 2, 3, 4, 5, 6]


def suma_lista(lista_de_numeros):
    # Esto es lo que hay que completar
    # mas codigo
    # es lo que esta adentro del for, lo que se va a repetir

    return  # algo


# Asi se le llama a la funcion
lista_x = [1, 2, 30, 5, 1]
suma_lista(lista_x)
# Tambien se le puede pasar la lista directamente
suma_lista([1, 2, 30, 5, 1])
# estos ejemplos deberian retornar 39 porque 1+2+30+5+1=39


# TIPOS DE DATOS

"Hola!"                          # esto es un string/cadena de caraceres(str)
50                               # esto es un Integer/entero(int)
50.0                             # esto es un Float(float)
[]                               # esta es una lista vacia(list)
def nombre_de_la_funcion(): ...  # esto es una funcion(function)


# Para saber el tipo de dato de una variable podemos usar la funcion type()
# ejemplo


a = 345  # Creamos la variable a y le asignamos 345 como valor
type(a)  # deberia retornar int(integer)
a = "Hola"  # Cambiamos el valor a un texto
type(a)  # deberia retornar str(string)
