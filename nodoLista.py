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