from nodoLista import*
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
            while aux.siguiente != None:
                print("aqui hay algo")
                aux = aux.siguiente

