'''
   Octubre 2024
***CONSTRUCTOR***
'''

#__CLASE Computadora__
class Computadora:
   marca: str = None
   capacidad: int = 0
   ram: int = 0

#CONSTRUCTOR
   def __init__(self, marca:Str, capacidad:int, ram:int):
      print(f"Accediendo al constructor de la pc: {marca}")
      self.marca = marca
      self.capacidad = capacidad
      self.ram = ram
   def imprimirInfoPC(self):
      print(f"Esta es la computadora marca: {self.marca} con almacenamiento de {self.capacidad}GB y memoria de {self.ram}GB")  

#DESTRUCTOR
   def __del__(self):
      print(f"Se elimino la computadora marca {self.marca}")


#__CLASE Persona__
class Persona:
   nombres: str = None
   apellidos: str = None
   edad: int = 0
   direccion: str = None
   computadora: Computadora = None

#CONSTRUCTOR
   def __init__(self, nombres:str, apellidos:str, edad:str, direccion:str, marca:str, capacidad:int, ram:int):
      self.nombres = nombres
      self.apellidos = apellidos
      self.edad = edad
      self.direccion = direccion
      self.Computadora = Computadora(marca, capacidad, ram)
      print(f"---Accedimos al constructor de la persona: {nombres}{apellidos}")
  
   def imprimirInfo(self) -> None
      print(f"---Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.direccion}")
      self.Computadora.imprimirInfoPC()
#DESTRUCTOR
   def __del__(self):
      print(f"---Eliminamos a la persona {self.nombres} {self.apellidos}")

'''
   Funcion1 es el PROGRAMA
'''
def funcion1():
   persona = Persona("Carlos", "Perez", 40, "Xochimilco", "Lenovo", 700,8)
   print("\n")
   persona.imprimirInfo()
   print("\n")
   persona2 = Persona("Magdalena", "Carrillo", 35, "Jalapa", "IBM", 200, 4)
   print("\n")
   persona2.imprimirInfo()
   print("\n")

'''
   LLAMAR funcion
'''
funcion1() 



  
A
         print(f"---Eliminamos a la persona {self.nombres} {self.apellidos}")
