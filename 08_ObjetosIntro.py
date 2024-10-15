'''
   15-10-24
    
  *** PROGRAMACION ORIENTADA A OBJETOS ***
'''

'''
   Una CLASE para un OBJETO VACIO:
   (no esta tan vacio, necesita la palabra PASS = pasar)
'''
class ObjetoVacio:
    pass

nada = ObjetoVacio() # "nada" es la instancia de la clase ObjetoVacio
print(type(nada)) # --> "nada" es un objeto de tipo "ObjetoVacio"

'''
   La clase llanta
'''
class Llanta:
    cuenta = 0 # esta variable es de toda la clase, la pueden usar todas sus funciones
    '''
       FUNCION CONSTRUCTOR
       __init__ es una funcion reservada
       self == mi mismo == mi --> indica que lo que se llamo le pertenece
       parametros de entrada = default
    '''
    def __init__(mi, radio=50, ancho=30, presion=1.5):
        Llanta.cuenta += 1  # variable de toda la clase Llanta
        # variables exclusivas de cada objeto tipo Llanta
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

'''
   OBJETOS (instanciados)
'''
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2) # crea objetos con parametros de default excepto la presion
llanta3 = Llanta() # todos los parametros de default
llanta4 = Llanta(40,30,1.6)

'''
   Objetos que contienen otros objetos
'''
class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

    micoche = Coche(llanta1, llanta2, llanta3, llanta4)
