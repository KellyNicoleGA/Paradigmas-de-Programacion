'''
   08 de octubre
   Condicionales y Bucles
'''
'''
   CONDICIONALES
'''
precio = 50

if precio < 50: #SI esto (proposicion1) es verdadero, entonces haz:
    print("El precio es menor que 50") #ESTO
elif precio > 50: #SI NO (proposicion1 falsa), pero (proposicion2) es verdadero, entonces haz:
    print("El precio es mayor que 50")
else: #SI NINGUNA de las proposiciones anteriores fue verdadera, entonces haz:
    print("El precio es 50")

'''
   CONDICIONALES ANIDADOS
'''
cantidad = 5
total = precio*cantidad
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero menor que 400")
        elif total < 500 and total > 300:
            print("Total entre 100 y 300")
'''
   CONDICIONALES DE IGUALDAD (==)
'''
elif (total==100):
    print("Total es 100")
else: 
    print("Total menor que 100")

'''
   CONTADOR mientras la CONDICION sea verdadera
'''
num = 0
while num < 5:
    num = num +1
    print('num = ', num)
num = 0
while num < 5:
    num += 1 # num=num+1 --> num+=1
    print('num = ', num) 
    if num == 3: #condicion antes de salir del bloque
        break
num = 0
while num < 5:
    num +=1
    if num > 3:
        continue #EVITA lo que sigue, continua con las iteraciones
    print('num = ', num)

'''
   BUCLE sobre LISTA
'''
nums = [10,20,30,40,50]
for i in nums:
    print(i)

'''
   BUCLE sobre un STRING
'''
for char in 'Hola':
    print(char)

'''
   BUCLE sobre un DICCIONARIO
   items = elementos
'''
numeros = {1:'uno', 2:'dos', 3:'tres'}
for par in numeros.items(): # par (pareja)
    print(par)

'''
   Bucle sobre diccionario
   key = llave
   value = valor
'''
for k,v in numeros.items():
    print("key = ", k, " value = ", v)




