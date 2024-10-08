'''
   Nicole Guerrero, 03-10-24
'''

'''
   CONJUNTO en python (SET)
'''
even_nums = {2,4,6,8,10} #conjunto de numeros pares
print(even_nums)

#el bool no es parte del conjunto
emp = {1,'Steve',10.5,True} #conjunto de diferentes objetos
print(emp)

nums = {1,2,3,4,5,6,6,5}
print(nums)

'''
   Convertir secuencia a conjunto
   NO LO GENERA EN ORDEN
'''
s = set('Hola')
print(s)
s = set((1,2,3,4,5)) #tupla a conjunto
print(s)

'''
   De diccionario a conjunto: conjunto de llaves
'''
d = {1:'uno', 2:'dos'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)
s.remove(100)
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

su = s1|s2   #UNION
print(su)

s1 = s1&s2   #INTERSECCION
print(s1)

sr = s1-s2   #DIFERENCIA DE CONJUNTOS
print(sr)

sp = s2-s1
print(sp)

ss = s1^s2   #DIFERENCIA SIMETRICA
print(ss)


'''
   Uso de diccionarios
'''

capitales = {"USA": "Washington D.C.", "France":"Paris", "India":"New Delhi"}
print(capitales)

'''
   Llave:valor
'''
d = {}   #diccionario vacio
numeros = {1:"uno", 2:"dos", 3:"tres"}   #llave int, valor string
decimales = {1.5:"uno y medio", 2.5:"dos y medio", 3.5:"tres y medio"}   #llave real(floaat), valor string
cosas = {("Parker","Reynolds", "Camlin"):"pluma", ("LG", "Whirlpool", "Samsung"): "refrigerador"}   #Llave tuple, valor string
romanos = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5} #llave string, valor int
print(romanos)
print(romanos["I"])

print(capitales.get("India"))

'''
   Imprimir llave y valor
'''
for k in capitales:
    print("Key= "+k+ " ,value= " +capitales[k])

# AGREGAR un dato en el diccionario con llave y valor manuales
capitales["Mexico"] = "CDMX"
print(capitales)

# BORRAR dato del diccionario
del capitales["Mexico"]
print(capitales)

# BORRAR TODO el diccionario
del capitales

#Imprimir llaves
print(romanos.keys())

#Imprimir valores
print(romanos.value())

# JUICIO de llave (esta o no esta la llave en el diccionario)
print("I" in romanos)
print("X" in romanos)
print("XX" in romanos)
