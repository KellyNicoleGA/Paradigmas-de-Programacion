'''
   Nicole Guerrero
   Noviembre 2024
'''
# Tres listas 
mi_lista = [1,2,3]
tu_lista = (10,20,30)
su_lista = (40,50,100) # tuplas (objetos constantes)

# Funcion multiplicar por 2
def multiplicar_por2(elemento):
    return elemento*2

'''
   Funcion filtra pares
   %modulo != no es igual
   lo regresa solo si es impar
'''
def solo_impar(elemento):
    return elemento % 2 != 0

'''
   Lista de pares de datos de las dos listas
   zip sirve para juntar listas
   list es para que la haga toda lista
'''
print(list(zip(mi_lista, tu_lista, su_lista)))

# ----------
una_lista = ["a", "b", "c", "d", "e", "f", "g"]
#Crear conjunto de elementos que se repiten 
duplicados = set([x for x in una_lista if una_lista.count(x) > 1])
print(duplicados)

# ---------
'''
   Expresion generadora 
   contiene un iterador 
   range(5) es un iterador de 0 a 4
   Utiliza ()
'''
cuadrados = (x*x for x in range(5))

# next llama a la siguiente evaluacion del iterador 
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))

# Pasar una funcion generadora
import math

# Suma los elementos del iterador
print(sum(x*x for x in range(5)))

# Lista de comprehension pasada como funcion
# Arma la lista por usar []
numeros_pares = [x for x in range(21) if x%2 == 0]
print([x for x in range(21) if x%2 == 0])
print(numeros_pares)

