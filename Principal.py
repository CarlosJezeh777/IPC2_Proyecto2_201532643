from tkinter import *
from tkinter import filedialog
import xml.etree.ElementTree as ET
from Lista import Lista_Simple, Lista_xml
from matriz import matriz
from graphviz import Source
from PIL import ImageTk, Image


class window:

    def __init__(self, main_window):
        self.m = matriz()
        self.lista_datos = Lista_xml()

        self.main_window = main_window
        self.main_window.title("Principal")
        self.main_window.geometry("700x500")
        self.main_window.config(bg = "#A6FA3E")

        self.frameB = Frame(self.main_window, pady = 5, bg = "#014A42")
        self.frameB.grid(row  = 0, column = 0, sticky = "ew", padx = 10, pady = 10)

        self.frame2 =  Frame(self.main_window, pady = 5, bg = "#014A42" )    
        self.frame2.grid(row  = 1, column = 0, pady =  20, padx = 10, sticky = "nsew", rowspan = 5)

        self.labO =Label(self.frame2, text = "Imagen Original")
        self.labO.grid(row = 0,column = 0, padx = 10,pady = 10, sticky = "nsew")

        self.b1 = Button(self.frameB, text = "CARGAR ARCHIVO", width = 20, command = self.ventanaCargar)
        self.b1.grid(row = 0, column = 0, padx = 5 )
        
        self.b2 = Button(self.frameB, text = "OPERACIONES", width = 20, command = self.ventanaOperaciones)
        self.b2.grid(row = 0, column = 2,padx = 5)
        
        self.b3 = Button(self.frameB, text = "REPORTES", width = 20)
        self.b3.grid(row = 0, column = 3,padx = 5)
        
        self.b4 = Button(self.frameB, text = "AYUDA", width = 20)
        self.b4.grid(row = 0, column = 4, padx = 5)

    def ventanaCargar(self):
        self.ventana_C = Toplevel()
        self.ventana_C.title("Cargar archivos")
        self.ventana_C.geometry("200x200")
        self.ventana_C.config(bg = "#A6FA3E")
        
        self.frameC = Frame(self.ventana_C)
        self.frameC.config(bg = "#014A42")
        self.frameC.pack(pady = 20)

        self.boton1  =  Button(self.frameC, text = "Cargar 1 imagen", command  = self.cargar1)
        self.boton1.grid(row = 0, column = 0,pady = 20)
        
        self.boton2  =  Button(self.frameC, text = "Cargar 2 imagenes")
        self.boton2.grid(row = 1, column = 0,pady = 20) 
    
    def ventanaOperaciones(self):
        self.ventana_ope = Toplevel()
        self.ventana_ope.config(bg = "#A6FA3E")
        self.ventana_ope.title("Operaciones")
        self.ventana_ope.geometry("200x300")

        self.frameO =  Frame(self.ventana_ope)
        self.frameO.config(bg = "#014A42")
        self.frameO.pack(pady = 20)

        Button(self.frameO, text = "limpiar zona", width = 20).grid(row = 0, column = 0,pady = 10)
        Button(self.frameO, text = "Agregar linea horizontal", width = 20).grid(row = 1, column = 0, pady = 10)
        Button(self.frameO, text = "Agregar linea vertical", width = 20).grid(row = 2, column = 0,pady = 10)
        Button(self.frameO, text = "Agregar rectangulo", width = 20).grid(row = 3, column = 0, pady = 10)
        Button(self.frameO, text = "Agregar triangulo", width = 20).grid(row = 4, column = 0, pady = 10)

    def cargar1(self):
        archivo_entrada = filedialog.askopenfilename(initialdir = "C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2",title = "Selecciona un archivo",filetypes =(("xml files","*.xml"),("xml files","*.*")))
        
        print(archivo_entrada)
        
        archivo = ET.parse(archivo_entrada)
        root = archivo.getroot()

        for element in root:
            contador = 0
            for subelement in element:
                if contador == 0:
                    name1 = subelement.text
                    contador = contador + 1
                elif contador == 1:
                    row1 = subelement.text
                    contador = contador + 1
                elif contador == 2:
                    colum1 = subelement.text
                    contador = contador + 1
                elif contador == 3:
                    self.ima1 = subelement.text
                    x = 1
                    y = -1
                    contadorES = 0
                    contadorAS = 0
                    for i in self.ima1:
                        if i == " ":
                           continue
                        elif i == "\n":
                            y = y + 1
                            x = 1
                        else:
                            if i == "-":
                                contadorES = contadorES + 1
                            elif i == "*":
                                contadorAS = contadorAS + 1    
                            self.m.insertar(y,x,i)
                            x = x + 1
                    contador = 0
        a = self.m.cadena_grap()
        s = Source(a,filename="original.gv",format="png")
        s.view()
        self.img = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/original.gv.png"))
        self.lab1 =Label(self.frame2, image = self.img).grid(row = 1,column = 0, padx = 10,pady = 10, sticky = "nsew")
        self.ventana_C.destroy()
    
    def limpiar(self):
        self.m.limpiar_espacio()
        a = self.m.cadena_grap()
        s = Source(a,filename="edit.gv",format="png")
        s.view()
        self.img2 = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/edit.gv.png"))
        self.lab2 =Label(self.frame2, image = self.img2).grid(row = 1,column = 1, padx = 10,pady = 10, sticky = "nsew")

    

ventanaP = Tk()
app = window(ventanaP)
ventanaP.mainloop()