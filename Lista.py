from nodoLista import Nodo_simple, Nodo_xml
from matriz import matriz
class Lista_Simple:

    def __init__(self):
        self.inicio = None

    def insertar(self, objeto):
        nuevo = Nodo_simple(objeto)
        if self.inicio == None:
            self.inicio = nuevo
        else:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.siguiente = None

    def recorrer(self):

        if self.inicio != None:
            aux =  self.inicio
            while aux != None:
                print(aux.nombre)
                aux = aux.siguiente

class Lista_xml:

    def __init__(self):
        self.inicio = None

    def insertar(self,nombre, filas, columnas, imagen):
        nuevo = Nodo_xml(nombre,filas,columnas,imagen)
        if self.inicio == None:
            self.inicio = nuevo
        else:
            aux = self.inicio
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            nuevo.siguiente = None
    
    def recorrer(self):
        if self.inicio != None:
            aux =  self.inicio
            while aux != None:
                print(aux.nombre +" "+ aux.filas+" "+ aux.columnas+" "+ aux.imagen)
                aux = aux.siguiente

   
# m = Lista_xml()
# m.insertar("Carlos","filas","colum","imagen")
# m.insertar("Jezeh","filas","colum","imagen")
# m.insertar("Gedeoni","filas","colum","imagen")
# m.recorrer()
