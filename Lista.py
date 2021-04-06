from nodoLista import Nodo_simple, Nodo_matriz,Nodo_Operaciones,Nodo_Errores
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

class Lista_matriz:

    def __init__(self):
        self.inicio = None

    def insertar(self,fecha,hora,nombre,espacios,asteriscos):
        nuevo = Nodo_matriz(fecha,hora,nombre,espacios,asteriscos)
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
    
    def cadena_html(self):
        cadena = "<h1>Matrices</h1>\n"
        if self.inicio != None:
            aux =  self.inicio
            while aux != None:
                cadena = cadena + "<p> Fecha: "+str(aux.fecha)+" - Hora: "+str(aux.hora)+" - Nombre: "+str(aux.nombre)+" - Espacios vacios: "+str(aux.espacios)+" - Espacios llenos: "+str(aux.asteriscos)+"</p>\n"
                aux = aux.siguiente
        return cadena

class Lista_ope:

    def __init__(self):
        self.inicio = None

    def insertar(self,fecha,hora,operacion,nombre):
        nuevo = Nodo_Operaciones(fecha,hora,operacion,nombre)
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

    def cadena_html(self):
        cadena = "<h1>Operaciones</h1>\n"
        if self.inicio != None:
            aux =  self.inicio
            while aux != None:
                cadena = cadena + "<p> Fecha: "+str(aux.fecha)+" - Hora: "+str(aux.hora)+" - Operacion: "+str(aux.operacion)+" - Nombre: "+str(aux.nombre)+"</p>\n"
                aux = aux.siguiente
        return cadena

class Lista_error:

    def __init__(self):
        self.inicio = None

    def insertar(self,fecha,hora,error,operacion,nombre):
        nuevo = Nodo_Errores(fecha,hora,error,operacion,nombre)
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

    def cadena_html(self):
        cadena = "<h1>Errores</h1>\n"
        if self.inicio != None:
            aux =  self.inicio
            while aux != None:
                cadena = cadena + "<p> Fecha: "+str(aux.fecha)+" - Hora: "+str(aux.hora)+" - Error: "+str(aux.error)+" - Operacion: "+str(aux.operacion)+" - Nombre: "+str(aux.nombre)+"</p>\n"
                aux = aux.siguiente
        return cadena

   
# m = Lista_matriz()
# m.insertar("12/12","12:12","matriz_1","20","2")
# m.insertar("12/14","12:1","matriz_2","30","20")
# s = m.cadena_html()
# print(s)
