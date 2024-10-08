#________26 sept 2024________

'''
 LISTAS
 Las listas pueden ser  de objetos diferentes
'''
miprimeralista = [] #lista vacio
print(miprimeralista)

'''
 Llenado de lista
'''
miprimeralista = [1, "Javier", 1.34, "Bosco", "Angel", "Abigail", True]
print(miprimeralista)

'''
 funcion list: crea una lista
 funcion range: secuencia de i hasta j-1
'''
nums = list(range(0,10)) 
nums2 = list(range(1,11))

for i in nums:
    print(i) 
for i in nums2:
    print(i)

'''
 Incluir nuevos elementos de la lista
'''
nums.append(11)
nums.append(12)
nums.append(13)
print(nums)

'''
 Quitar elementos de la lista
'''
nums.remove(13)
print(nums)

'''
 Quitar al elemento con indice i
'''
i=10
del nums[i]
print(nums)

'''
 Borrar la lista
'''
del nums

'''
 Sumar listas
'''
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

'''
 Llenado a mano
'''
potencial = []
for i in range(0,10):# range empieza por default en cero
    potencial.append(int(i))
print(potencial[9])

'''
 Generar una tupla con la lista
'''
potencial = tuple(potencial) #la tuplas son listas estaticas, tamaño definido
print(potencial[9])
print(potencial [10] #¿¿fuera de rango??!!!!!


