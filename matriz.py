from Nodos import Nodo, nodoEncabezado
from encabezado import listaEncabezado

class matriz:
    def __init__(self):
         self.eFilas = listaEncabezado()
         self.eColumnas = listaEncabezado()

    def insertar(self, fila, columna, dato):
        nuevo = Nodo(fila, columna, dato)

        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = nodoEncabezado(fila)
            eFila.acceso = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.acceso.columna:
                nuevo.derecha = eFila.acceso
                eFila.acceso.izquierda = nuevo
                eFila.acceso = nuevo    
            else:
                actual =  eFila.acceso
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual =  actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual


        eColum = self.eColumnas.getEncabezado(columna)
        if eColum == None:
            eColum = nodoEncabezado(columna)
            eColum.acceso = nuevo
            self.eColumnas.setEncabezado(eColum)
        else:
            if nuevo.fila < eColum.acceso.fila:
                nuevo.abajo = eColum.acceso
                eColum.acceso.arriba = nuevo
                eColum.acceso = nuevo    
            else:
                actual =  eColum.acceso
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual =  actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def imprimirColumna(self):
        eColum = self.eColumnas.primero

        while eColum != None:

            actual = eColum.acceso
            print("\ncolumna " + str(actual.columna))
            print("fila valor")
            while actual != None:
                print(str(actual.fila)+"   "+actual.dato)  
                actual = actual.abajo

            eColum = eColum.siguiente      


m = matriz()

m.insertar(1,1,"hola")
m.insertar(1,2,"h")
m.insertar(4,3,"hol")
m.insertar(4,4,"ola")
m.insertar(5,1,"la")
m.insertar(6,1,"a")
m.insertar(6,2,"o")
m.insertar(2,1,"l")

m.imprimirColumna()