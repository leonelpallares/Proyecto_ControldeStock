###########DECORADORES###########

def decorador_alta(funcion):
    def decorator(*args):
        funcion(*args)
        print("Se ha realizado un alta de producto")
    return decorator


def decorador_borrar(funcion):
    def decorator(*args):
        funcion(*args)
        print("Se ha realizado una baja de producto")
    return decorator


def decorador_modificar(funcion):
    def decorator(*args):
        funcion(*args)
        print("Se han modificado los registros")
    return decorator