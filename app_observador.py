class Sujeto:

    observadores = []

    def alta(self, obj):
        self.observadores.append(obj)

    def borrar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(*args)


class Observador:
    def actualizar(self, *args): pass



class Observador_alta(Observador):
    def __init__(self, obj):
        self.observado_altas = obj
        self.observado_altas.agregar(self)

    def actualizar(self, *args):
        if args[0]=="alta":
           print("Se ha realizado un alta de producto")

class Observador_borrar(Observador):
    def __init__(self, obj):
        self.observador_borrar = obj
        self.observador_borrar.agregar(self)
    
    def actualizar(self,*args):
        if args[0]=="borrar":
            print("Se ha realizado una baja de producto")
