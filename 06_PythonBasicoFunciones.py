'''
   Kelly Nicole Guerrero Astudillo
   10 de octrubre del 2024
'''
# FUNCIONES
def saludo(): # documentacion rapida de la funcion
    print('Hola, como estas?')

saludo() # llamado de la funcion

salida = saludo() # se ejecuta pero no se asigna
print(salida) # esto no funciona

help(saludo) # mostrar documentacion

def salu2(nombre):
    print("Que onda", nombre,"!") # esta funcion te saluda por tu nombre
salu2("Kelly")
salu2("Nicole")

''' Ahorrar trabajo del interprete
    nombre:str --> la variable nombre es de tipo str
'''
def saludos(nombre:str):
    # Esta funcion te saluda por tu nombre estrictamente (cadena de texto)
    print("¡Que onda esa ", nombre, " <3")
saludos("Maria")
a = 123
print(type(a))
saludos(a)


# FUNCION CON MUCHOS ARGUMENTOS
def muchos_saludos(*nombres):
    # esta funcion saluda a todos los que quieras
    i = 0
    # END es para ponerlo de corrido
    print("Hola ", end = "")
    while len (nombres) > i:
        # ultimo nombre
        if(i == len(nombres) - 1):
            print(nombres[i])
        else:
            # cualquier otro nombre
            print(nombre[i], end = ", ")
         i+=1

muchos_saludos("nicole", "enrique", "alejandro", "ivan", "zaid", "joel", "servin", "alexis", "joel")

def saludo_completo(firstname, lastname):
    print("Hola, firstname, lastname")

# LLAMAR la funcion con argumentos en DESORDEN
saludo_completo(lastname = "Jobs", firstname = "Steve")

# funcion con ARGUMENTOS ESCONDIDOS
def saludo_completo(**persona):
  # persona tiene caracteristicas firstname y lastname
  print("Hola ", person['firstname'], person['lastname'])

saludo_completo(firstname = "Steve", lastname = "Jobs")
saludo_completo(lastname = "Maria", firstname = "Guadalupe")
saludo_completo(firstname = "Nicole", lastname = "Guerrero", edad = 19) # se pueden pasar parametros innecesarios

# Funcion con VALORES por DEFECTO
def saludo_completo(name = "Kelly"):
    print("Hola ", name)

saludo_completo() # Utiliza el valor dado de antemano
saludo_completo("Nicole")

# FUNCION CON RESULTADO
def suma(a,b):
    return a+b

# PROGRAMACION FUNCIONAL 
# Se pueden usar funciones dentro de funciones
total = suma(5, suma(10,20))
print(total)

# CALCULO LAMBDA
# Nombre de la funcion = lambda variable: funcion
x_al_cuadrado = lambda x: x*x # CUADRADO DE UN NUMERO
a1 = x_al_cuadrado(5)
print(a1)

# Lambda de varias variables
suma = lambda x1, x2, x3: x1+x2+x3 # SUMA DE TRES NUMEROS 
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]
print(sumas(100,200,300,400))

'''
   Uso de una funcion anonima
   El argumento va afuera entre parentesis
'''
print((lambda x: x*x)(6)) #Funcion anonima (no tiene nombre)

'''
   Funcion con variable global
   (evitar el exceso!)
'''
nombre = 'Nicole'
def Saluditos():
    globlal nombre # Para utilizar una variable global (que viene de fuera del bloque)
    nombre = "Kelly"
    print('Hola', nombre)
saluditos()



