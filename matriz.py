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

    def grafica_original(self):
        cadena = """digraph matriz{
        node[shape = record];
        structura [label = \""""

        eColum = self.eColumnas.primero
        while eColum != None:
            actual = eColum.acceso
            cadena = cadena + "{" + str(actual.columna) 
            while actual != None:  
                if actual.dato == "*":
                    cadena = cadena + "|" + str(actual.dato)
                else:
                    cadena = cadena + "|"
                actual = actual.abajo
            eColum = eColum.siguiente
            
            if eColum == None:
                cadena =  cadena + "}"     
            else:     
                cadena =  cadena + "}|"

        cadena = cadena +"""\"];
        }"""
        return cadena

# m = matriz()

# m.insertar(1,1,"-")
# m.insertar(1,2,"-")
# m.insertar(1,3,"*")
# m.insertar(2,1,"*")
# m.insertar(2,2,"-")
# m.insertar(2,3,"*")
# m.insertar(3,1,"-")
# m.insertar(3,2,"*")
# m.insertar(3,3,"-")

# m.imprimirColumna()
# a = m.grafica_original()
# print(a)