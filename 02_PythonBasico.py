#*****************************************
#   Kelly Nicole Guerrero Astudillo
#   Clase 19-09-24
#*****************************************
#_________________________________________________________
#   INPUT permite obtener datos del usuario en prompter
#_________________________________________________________
nombre = input("Dame tu nombre: ")
print("Hola como estas ", nombre)

#____________________________________________
#   Los enteros son de precision ilimitada   
#____________________________________________
y = 500000000000000000000000000000000000000
print(y)
#_________________________________________________________________
#   Se pueden delimitar numeros con guion bajo pero no con coma
#_________________________________________________________________
y = 5_000_000
print(y)

#________________________________________________________
#   La funcion int() cambia strings y floats a enteros
#________________________________________________________
numero = int(input("Dame tu edad: "))
type(numero)

#_______________________________________________________
#   La notacion cientifica de flotantes utiliza e o E 
#   1.2x10^9
#_______________________________________________________
y = 1.2E-09
print(y)

#_____________________________________________________________
#   La funcion float() convierte strings y enteros a floats
#_____________________________________________________________
y = float("14.3")
print(y)

#_________________________________________________________
#   Los numeros complejos se escriben con la raiz de -1
#   j siempre va con un numero como prefijo
#   j no acepta la j suelta
#_________________________________________________________
z = 1+1j

#   SUMA(+), RESTA(-), MULTIPLICACION(*) 
#   DIVISION(/), MODULO(%), EXPONENTE(**) 
#   
#   ******   Funciones Piso   ******
#   Funciones para transformar numeros
#      float(), complex(), int()

#   ****** OPERACIONES ******
#    abs(), round(), pow()

print(round(3.14159,4))

#_______________________________ 
#   STRINGS DE VARIAS LINEAS
#_______________________________
parrafo = "En el bosque de la china,
           la chinita se perdio"""
print(parrafo)

#___________________________________________________
#   La funcion LEN() obtiene el tamaño del string
#___________________________________________________
n = len(parrafo)
print(n)

#________________________________________________________________
#   Las letras en un string ocupan lugares como en un arreglo
#   (tambien de atras para adelante comenzando en -1 el ultimo)
#_________________________________________________________________
palabra = "hola"
print(palabra[0])
print(palabra[1])


