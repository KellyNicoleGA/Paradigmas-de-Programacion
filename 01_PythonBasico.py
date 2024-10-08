#****************************
#___Nicole Guerrero Astudillo
#___10 de septiembre del 2024, ESFM-IPN
#___(Apunte)   
#___OPERACIONES BASICAS___
#****************************
print(2+3)
print(2*3)
print(2/3)
print(2**10)
print(2**0.5) #RAIZ CUADRADA
print(10%2)
print(10%0.1) #Exclusivo en Python 

#___Type: Tipo de dato___
t=0
print(type(t)) #(entero)
t=3.6
print(type(t)) #(real) (flotante)
t=True
print(type(t)) #(booleano) (bool)

#___MENSAJES A PANTALLA___
#*****************************
print("Este es un comando de python." , "Este es otro enunciado." , t)
print('id: ', 1)
print('Nombres: ', 'Steve')
print('Apellidos: ', 'Steve')
print("vamos a sumar esto" + " con esto otro")

#___CONTINUAR una instruccion en Varios RENGLONES___

if 100>99 and \
    200<=300 and \
     True != False: 
       print('Hola a todos')

#___Comandos DIFERENTES en la misma LINEA

print("Hola ");print ("tu") #(se considera mala practica)

#___Usando parentesis redondos, cuadrados o llaves___
#___se puede escribir en varios renglones___
       
lista = [1,2,3,4,
         5,6,7,8,
         9,10,11,12]
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(lista)
print(matriz)
 
#****************************************************************
#Identacion estricta para procesos dependientes de : (dos puntos)
#****************************************************************

if 10>5: 
   print ("diez es mayor que cinco")
   print("otra identacion")
for i in lista:
   print(i)
   print("ok")
if 10>5:
   print("verdadero")

   if 10<20:
      print("verdadero")
elif 5>3: #comienza segundo condicional
   print("esto no se imprimira")
else:
   print ("aqui nunca llega")

#************
# Funciones
#************
def saludar(nombre):
    print("Hola ", nombre)
    print("Bienvenido al tutorial de python")

saludar("Julian")




























































































