from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

# Para llenar la interface hay que heredar la clase
class BaseDeDatos(RepositorioDeUsuarios):
    __host:str
    __user:str
    __password:str

    # constructor
    def __init__(mi, host:str, user:str, password:str):
        mi.__host=host
        mi.user=user
        mi.password=password

    def abrir(mi) -> None:
        print(f"Abriendo la conexion a la base de datos: {mi.__host}: {mi.__user}@{mi.__password}")

    def guardar(mi, usuario:Usuario) -> None:
        userElements = {"nombre":usuario.getNombre(),
                "apellidos":usuario.getApellido(),
                "edad":usuario.getEdad() }
        print(f"Guardando el usuario en la base de datos {usuario.getNombre()}\n")
    def cerrar(mi) -> None:
        print("Cerrando la conexion")
