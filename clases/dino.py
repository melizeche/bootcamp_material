
# Agregarle una propiedad color a la clase Dino, y que salude 
# diciendo su nombre y de que color es el dinosaurio

#Crear una carpeta que se llame clases y adentro poner los$
# archivos dino.py persona.py

# Crear una clase Persona() en el archivo persona.py que tenga como atributos 
# nombre, edad y profesion.
# Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

# Agregar un metodo a la clase persona, que se llame cumpleanhos y que aumente la edad de la
# persona en un anho y retorne la edad nueva

# Agregarle un atributo de clase a la clase persona que almacene una lista de hobbies
# Crear un metodo getter que retorne los hobbies de la persona
# Crear un metodo que reciba un hobbie como argumento y que lo agregue a la lista de hobbies
class Dino:
    patas = 4   # esto es un atributo de clase
    def __init__(self,un_nombre=None, un_color=None):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy un dinosaurio, me llamo ", self.nombre, "y soy ", self.color)
    
    def __repr__(self):
        return "<Objeto tipo Dino, nombre: " + self.nombre + ">"
    
    def cantidad_patas(self): # es un metodo getter o metodo para obtener un atributo del objeto
        return self.patas
    
    def set_patas(self, canti): # es un metodo setter o para asignar un valor a un atributo
        #print("Entre al metodo, canti es ", canti)
        if type(canti)==int or type(canti)==float:
            #print("Entre al if")
            self.patas = canti
        else:
            #print("Entre al else")
            print(canti, "no es un entero, ingresa un numero de patas a asignar")
    
    def rugir(self, rugido):
        #print(self)
        #print(rugido)
        print("RARWRR!!!", rugido)
    
    def cambiar_color(self, un_color):
        self.color = un_color
        #print("Se cambio el color de", self.nombre, " a ", self.color)
    
    def que_color(self):
        print("El color del dinosaurio es ", self.color)

    def cortar_pata(self): 
        if self.patas>0:
            self.patas = self.patas-1
        else:
            print("Ya no tengo mas patas :(   ")

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


#

class TRex(Dino):
    gente_comida=0

    def __init__(self, un_nombre):
        self.nombre = un_nombre
        print("Soy un TRex, me llamo", self.nombre)
    
    def comer_gente(self):
        self.gente_comida = self.gente_comida + 1
        print("Me comi a una persona")


pepex = TRex("Pepex el TRex")

# Crear una clase Estudiante que herede de Persona y tenga como 
# atributos de clase una lista de cursos
# crear metodos para agregar cursos y eliminar cursos/materias
