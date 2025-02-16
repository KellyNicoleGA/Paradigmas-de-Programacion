'''
   Curvas Z-splines en n dimensiones
   Nicole Guerrero
'''
import numpy as np
from Curva import Curva, zpline
import matplotlib.pyplot as plt
import math

# CONJUNTO DE PUNTOS

#  numero de puntos
nump:no.int32 = 8
# Dimension
dim:np.int32 = 2
# memoria para puntos
puntos = np.zeros(dim*nump, dtype=np, float64)
# Parametrizacion
X = np.linspace(0.0, 2*np.pi, nump+1)
# Coordenada x
puntos[0:nump] = np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
# Coordenadas y
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

'''
   Curva z-spline de n puntos zspline(p,d,n,m)
   p: puntos, d: dimension, n: segmentos de curva, m: continuidad
'''
n:np.int32 = 1000
x1,y1 = zspline(puntos, dim, n, 2)
x1,y2 = zspline(puntos, dim, n, 1)
x3, y3 = zspline(puntos, dim, n, 0)
plt.plot(x3,y3,lw=3, color="orange")
plt.plot(x2,y2,lw=3, color="red")
plt.plot(x1,y1,lw=3, color="blue")
plt.scatter(puntos[0:nump], puntos[nump:2*nump], marker='o', color='black')
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")
plt.title("Curva cerrada Z-spline en 2D")
plt.show()
