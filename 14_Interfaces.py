'''
   Del directorio 'aplicacion', el subdirectorio 'repositorio', 
   el archivo 'base de datos.py' traemos el objeto 'Basededatos'
'''
from aplicacion.repositorio.basededatos import BaseDeDatos

'''
   Del directorio 'aplicacion', el subdirectorio 'repositorio',
   el archivo 's3.py' traemos el objeto S3
'''
from.aplicacion.repositorio.s3 import S3

''' 
   Del directorio 'aplicacion', el subdirectorio 'repositorio'
   el archivo 'sistemadearchivo.py' traemos el objeto SistemaDeArchivos
'''
from aplicacion.modelos.usuario import Usuario

'''
   Del directorio 'aplicacion', el subdirectorio 'negocios',
   el archivo manejodeinscripciones import ManejoDeInscripciones
'''
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

'''
   Crear el objeto 'Usuario'
'''
usuario = Usuario("Roberto", "Jimenez", 18)

'''
   Crear el objeto 's3'
'''
repositorios3 = S3("321321321", "sdf324223", "MiCubeta")

'''
   Interface inscribirUsuario del objeto ManejoDeInscripciones
'''
ManejoDeInscripciones.inscribirUsuario(usuario, repositorioS3)
print("\n")

'''
   Crear el objeto sistemadearchivos
'''
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

'''
   Interface inscribirUsuario del objeto ManejoDeInscripciones
'''
ManejoDeInscripciones.inscrirUsuario(usuario, repositorioSistemaDeArchivos)
print("\n")

'''
   Crear el objeto basededatos
'''
repositorioBaseDeDatos = BaseDeDatos("localhost", "admin", "admin123")

'''
Interface inscribirUsuario del objeto ManejoDeInscripciones
'''
ManejoDeInscripciiones.inscribirUsuario(usuario, repositorioBaseDeDatos)
print("\n")




 
