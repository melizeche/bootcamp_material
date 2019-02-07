# Diccionarios
#¿Qué es un Diccionario de datos?

# Un Diccionario es una estructura de datos y un tipo de dato en Python 
# con características especiales que nos permite almacenar cualquier 
# tipo de valor como enteros, cadenas, listas e incluso otras funciones. 
# Estos diccionarios nos permiten además identificar cada elemento por una 
# clave (Key).

#Ejemplo:
nombre_del_diccionario = {"nombre_de_la_clave":"valor de cualquier tipo"}
diccionario_vacio = {}

persona = {"nombre":"Marce", "edad":32}

print(persona)

# Para acceder a un valor ponemos nombre_del_dict["nombre de la clave"]
print(persona["nombre"])
print(persona["edad"])
# Tambien podemos usar
print(persona.get("nombre"))

#agregar un elemento(clave/valor)
persona["profesion"] = "Programador"
print(persona)
lista_hobbies = ["rugby", "dormir", "ver peliculas"]
persona["hobbies"] = lista_hobbies
print(persona)

#cambiar un valor del diccionario
persona["edad"] = 22
print(persona)

agenda = {
    "lunes": {
        "AM":"Dormir",
        "PM":"Enseñar"
        },
    "martes": {
        "AM":"Enseñar", 
        "PM":["Enseñar", "Hacer asado"]
        },
    "miercoles" :{"AM":"Enseñar en el bootcap"},
}

print(agenda)

persona["horario"] = agenda

print(persona)

from pprint import pprint

# Crear un diccionario persona que contenga las claves 
# "nombre", "edad", "profesion" e imprimir el valor de cada clave
persona={} #diccionario vacio
persona["nombre"] = "Marce"                       #opcion1
personita = { "nombre" : "pepito" , "edad" : 12 } #opcion2

print(persona["nombre"])


# Recorrer un diccionario con for e imprimir los valores(no las claves)
personita["nombre"]

for clave in personita:
    print(personita[clave])




pprint(persona)

import requests


respuesta = requests.get("http://www.omdbapi.com/?apikey=595695c3&t=Harry+Potter")
print(respuesta.text)
harry = respuesta.json()



basic_call = "http://www.omdbapi.com/?apikey=" + API_KEY + "&s="

def buscar_peli(titulo):
    busqueda = basic_call + titulo
    resp = requests.get(busqueda)
    return resp

a = buscar_peli("Birdemic").json()

def info_peli(titulo):
    busqueda = "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + titulo
    print(busqueda)
    resp = requests.get(busqueda).json()
    print(resp)
    return resp

pelicula = info_peli("Birdemic")


import requests
API_KEY = "595695c3"

titulo="Blade"
busqueda = "http://www.omdbapi.com/?apikey=" + API_KEY + "&t=" + titulo
print(busqueda)
peli = requests.get(busqueda).json()

pprint(peli)
print(peli["Director"])

# Crear una funcion que reciba como argumento el titulo de una pelicula y 
# que consulte al API de OpenMovieDataBase y retorne el nombre de los actores
# de esa pelicula