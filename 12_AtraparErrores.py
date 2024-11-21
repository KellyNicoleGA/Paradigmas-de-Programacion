'''
   Atrapar errores
   Nicole Guerrero
'''


#   La clase ClienteBancario esta en el subdirectorio aplicacion/banco/
from aplicacion.banco.cliente_bancario import ClienteBancario

'''
   try: intenta (correr las instrucciones
   except: atrapar el error en una variable e
   e se puede convertir a string
'''
try:
    cliente = ClienteBancario("Jaime Andrade", "Hernandez Sanchez", 28, 0.0)
    cliente.guardarDinero(300)
    print("Esta es la informacion del cliente: " + cliente.imprimirInfo())
    cliente.retirarDinero(150) # El try saca un error por intentar sacar mas dinero del que se tiene

# La excepcion es el objeto mas general de error
except Exception as e:
    print("Este es un error por sacar mas dinero del que se tiene: " + str(e))

try: # Error por usar un atributo privado
    print(cliente.__nombres)
except Exception as ex:
    print("Este es un error por usar un atributo privado (nombre): " + str(ex))

# Forma correcta
print(cliente.nombres)

