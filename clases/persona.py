#Crear una carpeta que se llame clases y adentro poner los$
# archivos dino.py persona.py

# Crear una clase Persona() que tenga como atributos nombre, edad 
# y profesion. Al instanciar la clase tiene que saludar igual que el
# dino diciendo sus atributos

# Agregar un metodo a la clase persona, que se llame cumpleanhos y que aumente la edad de la
# persona en un anho y retorne la edad nueva

# Agregarle un atributo de clase a la clase persona que almacene una lista de hobbies
# Crear un metodo getter que retorne los hobbies de la persona
# Crear un metodo que agregue hobbies a la lista





class Persona:

    lista_hobbies=[]

    def __init__(self, un_nombre,una_edad,una_profesion, hobbies=None):
        self.nombre=un_nombre
        self.edad = una_edad
        self.profesion = una_profesion
        self.lista_hobbies = hobbies
    
    def __repr__(self):
        valor = "<Objeto Persona: " + self.nombre  + ">"
        return valor
    
    def agregar_hobbies(self, something):

        self.lista_hobbies.append(something)
        return self.lista_hobbies
        # if type(something)==str or type(something)==list:
        #     self.lista_hobbies.append(something)
        #     return self.lista_hobbies
        # else:
        #     return ("Debes ingresar una lista [] o una cadena de texto '' ")
        #self.agregados = something
    
    def obtener_hobbies(self):
        return self.lista_hobbies

    def cumpleanhos(self):
        self.edad = self.edad + 1
        return self.edad

patata = Persona("Guillermo", 27, "Programador", ['comer'])

print(patata.lista_hobbies)
print(patata.obtener_hobbies())
print(patata.agregar_hobbies("dormir"))


# Crear una clase que se llame Agenda que tenga metodos
# para agregar objetos de tipo Persona a una lista(atributo de clase) 
# y tambien poder eliminar personas de esa lista
# crear 3 personas y agregarlas a un objeto Agenda

class Agenda:
    #contactos = []
    def __init__(self):
        self.contactos = []
    
    def agregar_persona(self, milanesa):
        if type(milanesa)==Persona:
            self.contactos.append(milanesa)
        else:
            print("Necesito una persona")
    
    def eliminar_persona(self, personita):
        self.contactos.remove(personita)

agendita = Agenda()

pepito = Persona("Pepe", 27, "EEEEEE", ['comer'])
pepita = Persona("Pepa", 27, "DDDD", ['comer'])
pepite = Persona("Pepx", 27, "Programador", ['comer'])

agendita.agregar_persona(pepito)
agendita.agregar_persona(pepita)
agendita.agregar_persona(pepite)

