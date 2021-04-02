class Nodo:

    def __init__(self,fila,columna,dato):
        self.dato = dato
        self.fila = fila
        self.columna = columna
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None

class nodoEncabezado:

    def __init__(self,id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None
