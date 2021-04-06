class Nodo_simple:
    
    def __init__(self, objeto):
        self.objeto = objeto
        self.siguiente = None

    def getObjeto(self):
        return self.objeto

    def setObjeto(self,objeto):
        self.objeto = objeto

    def getSiguiente(self):
        return self.siguiente

    def setObjeto(self,siguiente):
        self.siguiente = siguiente

class Nodo_matriz:
    
    def __init__(self, fecha, hora, nombre, espacios, asteriscos):
        self.fecha = fecha
        self.hora = hora
        self.nombre = nombre
        self.espacios = espacios
        self.asteriscos = asteriscos
        self.siguiente = None

class Nodo_Operaciones:
    
    def __init__(self, fecha,hora, operacion, nombre):
        self.fecha = fecha
        self.hora = hora
        self.nombre = nombre
        self.operacion = operacion
        self.siguiente = None

class Nodo_Errores:
    
    def __init__(self, fecha,hora, error, operacion, nombre):
        self.fecha = fecha
        self.hora = hora
        self.error = error
        self.nombre = nombre
        self.operacion = operacion
        self.siguiente = None