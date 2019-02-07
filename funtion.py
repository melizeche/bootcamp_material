def transformador(boligrafo): # boligrafo = "lentes"
    papel = boligrafo + " de sol"
    return papel
papelito = transformador("lentes")
print(papelito)
#Crear una funcion que reciba dos parametros(A , B), 
#la funcion deberia sumar los parametros y retornar la suma
#Y llamar esta funcion muchas veces con diferentes tipos de datos(integer, string...)
def suma(A, B):
    suma = A+B
    return suma


suma(1,2)
suma("Hola", "Que tal")
suma(2, "Hola")
suma(True, "Chau")
suma([1,2,3],[4,5,6])
#TIPOS DE DATOS
"Hola" # Esto es un string
34 # Esto es un integer
34.53 # Esto es un float
True #Esto es un boolean
[1,2,3] #Esto es una lista