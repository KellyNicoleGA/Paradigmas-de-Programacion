'''
   Nicole Guerrero 
   Enero 2025
'''
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# un dato
data = (rank+1)**2

# manden sus datos al proceso root=0 (en orden)
datas = comm.gather(data, root=0)

# asegurarse que todo funcione bien
if rank==0:
    for i in range(size):
        assert datas[i] == (i+1)**2
else:
    assert datas is None
print(datas)

# Ahora mas rapido con numpy
n = 10

'''
   arreglo de ceros de tamaño n
   sumado con un escalar (en cada entrada)
'''
sendarray = numpy.zeros(n, dtype='i')+rank
recvarray = None
if rank == 0:
    # matriz vacia de tamaño (procesos*n)
    recvarray = numpy.empty([size,n], dtype='i')
    #dtype es el tipo de dato (i) es entero

# Gather es rapido para numpy, enviar datos al proceso root
comm.Gather(sendarray, recvarray, root=0)
if rank == 0:
    for i in range(size):
        '''
           revisar por fila la matriz
           : significa todos los elementos de esa dimension
           allclose es un metodo de numpy que compara los elementos
        '''
        assert numpy.allclose(recvarray[i,:], i)
print(recvarray)

