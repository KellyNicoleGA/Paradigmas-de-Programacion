from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

# S3 es hijo de RepositorioDeUsuarios
class S3(RepositorioDeUsuarios):
    __clienteId:str
    __secretkey:str
    __bucket:str

    # constructor
    def __init__(mi, clienteId:str, secretKey:str, bucket:str):
        mi.__clienteId=clienteId
        mi.password=secretKey
        mi.__bucket=buckey

    def abrir(mi)-> None:
        print(f"Estableciendo conexion a AWS S3 {mi.__clienteId}:{mi.__secretKey}")

    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(),
                "apellido":usuario.getApellido(),
                "edad":usuario.getEdad() }
        print(f"Guardando usuario de la bandeja: {mi.__bucket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando el archivo")


