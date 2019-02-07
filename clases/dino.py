
# Agregarle una propiedad color a la clase Dino, y que salude 
# diciendo su nombre y de que color es el dinosaurio

#Crear una carpeta que se llame clases y adentro poner los$
# archivos dino.py persona.py

# Crear una clase Persona() en el archivo persona.py que tenga como atributos 
# nombre, edad y profesion.
# Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

# Agregar un metodo a la clase persona, que se llame cumpleanhos y que aumente la edad de la
# persona en un anho y retorne la edad nueva
class Dino:
    def __init__(self,un_nombre="", un_color="verde"):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy un dinosaurio, me llamo ", self.nombre, "y soy ", self.color)
    
    def rugir(self, rugido):
        #print(self)
        #print(rugido)
        print("RARWRR!!!", rugido)
    
    def cambiar_color(self, un_color):
        self.color = un_color
        #print("Se cambio el color de", self.nombre, " a ", self.color)
    
    def que_color(self):
        print("El color del dinosaurio es ", self.color)

# Aca instanciamos o creamos el objeto pepito de tipo Dino
pepito = Dino("Pepe", "Verde")
# Aca accedemos a la propiedad o atributo nombre del objeto e imprimimos 
print(pepito.nombre)
# Aca accedemos a la propiedad o atributo nombre del objeto e imprimimos 
print(pepito.color)
# Aca llamamos al metodo rugir pasandole un string como atributo
pepito.rugir("AAAAH!!!!!!!!!!!!!!!!")
#
pepito.cambiar_color("Lila")

#Aca instanciamos varios objetos del tipo Dino

pepita = Dino("Pepa", "plata")
pepite = Dino("Pepx")
pepiti = Dino("Pxpx", "Azulgrana")
pepo = Dino(un_color="Pink", un_nombre="GGGG")


