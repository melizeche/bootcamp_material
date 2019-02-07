#Crear una carpeta que se llame clases y adentro poner los$
# archivos dino.py persona.py

# Crear una clase Persona() que tenga como atributos nombre, edad 
# y profesion. Al instanciar la clase tiene que saludar igual que el
# dino diciendo sus atributos

# Agregar un metodo a la clase persona, que se llame cumpleanhos y que aumente la edad de la
# persona en un anho y retorne la edad nueva

class Persona:
    def __init__(self, un_nombre,una_edad,una_profesion):
        self.nombre=un_nombre
        self.edad = una_edad
        self.profesion = una_profesion
    
    def cumpleanhos(self):
        self.edad = self.edad + 1
        return self.edad

guillermo = Persona("Guillermo", 27, "Programador")
print(guillermo.edad)
guillermo.cumpleanhos()
print(guillermo.nombre)
print(guillermo.edad)
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()
guillermo.cumpleanhos()

marce = Persona("Marcelo",32,"Chofer")
print(marce.edad)
marce.cumpleanhos()
print(marce.edad)
print(guillermo.edad)

edad_de_guille = guillermo.cumpleanhos()
print(edad_de_guille)
print(edad_de_guille)
print(edad_de_guille)
print(edad_de_guille)
print(edad_de_guille)
print(edad_de_guille)
