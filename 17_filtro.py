'''
   Nicole Guerrero
   Noviembre 2024

   Uso de filtros
'''

# 1)  Hacer una lista de los numeros por arriba del promedio

# ---Modulo de Estadistica---
import statistics
bigdata = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
promedio = statistics.mean(bigdata)
print(promedio)

'''
   Hazme una lista de elementos que cumplan la condicon x>promedio
   filter(condicion, datos)
'''
print(list(filter(lambda x: x>promedio, bigdata)))

# 2)  Limpiar los datos
paises = ["", "Argentina", "", "Brasil", "", "Chile", "Mexico", "", "Colombia", "", "", "Cuba", "Venezuela"]

# Filtra lo que no contiene nada
print(list(filter(None, paises)))
