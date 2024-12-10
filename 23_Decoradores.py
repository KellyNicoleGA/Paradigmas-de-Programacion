'''
   Nicole Guerrero
   Diciembre 2024
   DECORADORES
'''

# Funcion que regresa otra funcion 
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Funcion saludo
def say_hi():
    return "hello there"

# Generar y correro funcion
decorate = uppercase_decorator(say_hi)
print(decorate())

# Utilizar como decorador
@uppercase_decorator
def say_hi():
    return "hello there"

# Correr funcion pasado por decorador
print(say_hi())
