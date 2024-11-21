'''
   Nicole Guerrero
   Noviembre 2024
'''

# Funcion para x**3
def alcuadrado(x):
    return x*x

# Funcion para x**2
def alcubo(x):
    return x*x*x

# Mapeo de una funcion pura
def mapeo(func, lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado, [2.5, 2, 3.8, 1.2, 6.6, 11, 7, 8])
cubos = mapeo(alcubo, [1,2,3,4,5,6,7,8])
print(cuadrados)
print(cubos)

# Funciobes dentro de funciones
def en_mayusculas(texto):
    return texto.upper()
def en_minusculas(texto):
    return texto.lower()
def saludar(func):
    saludo = func("Hola, como estas?")
    print(saludo)

# Con strings
saludar(en_mayusculas)
saludar(en_minusculas)

'''
   Funciones abstractas dentro de funciones 
   su resultado es otra funcion
'''
def divisor(x):
    def dividendo(y): # se tiene que llamar dos veces la funcion 
        return y/x
    return dividendo

# Primero generamos la funcion y/2
division = divisor(2)

# La usamos para calcular 3/2
print(division(3))

# --- Uso de la funcion map con una lista ---

# Lista de ciudades y su temperatura

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),("Los Angeles", 26), ("Tokyo", 27), ("Nueva York", 28), ("Londres", 27), ("Pekin", 32), ("Mexico Tenochtitlan", 23)]

# de centigrados a farenheit
C_a_F = lambda datos: (datos[0], (9/5)*datos[1] + 32) # el primer parametro lo guarda tal cual esta (el nombre de la ciudad), y el segundo lo converte a F mediante la formula
print(list(mapeo(C_a_F, temps))) # cuando entra a la funcion temps es el vector datos
# se puede sustituir la palabra mapeo por map e igual funciona
