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
        self.main_window.geometry("750x550")
        self.main_window.config(bg = "#A6FA3E")

        self.frameB = Frame(self.main_window, pady = 5, bg = "#014A42")
        self.frameB.grid(row  = 0, column = 0, sticky = "ew", padx = 10, pady = 10)

        self.frame2 =  Frame(self.main_window, pady = 5, bg = "#014A42" )    
        self.frame2.grid(row  = 1, column = 0, pady =  20, padx = 10, sticky = "nsew", rowspan = 5)

        self.labO =Label(self.frame2, text = "Imagen Original")
        self.labO.grid(row = 0,column = 0, padx = 10,pady = 10, sticky = "nsew")

        self.labE =Label(self.frame2, text = "editada")
        self.labE.grid(row = 0,column = 1, padx = 10,pady = 10, sticky = "nsew")

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
        
        frameC = Frame(self.ventana_C)
        frameC.config(bg = "#014A42")
        frameC.pack(pady = 20)

        boton1  =  Button(frameC, text = "Cargar 1 imagen", command  = self.cargar1)
        boton1.grid(row = 0, column = 0,pady = 20)
        
        boton2  =  Button(frameC, text = "Cargar 2 imagenes")
        boton2.grid(row = 1, column = 0,pady = 20) 
    
    def ventanaOperaciones(self):
        self.ventana_ope = Toplevel()
        self.ventana_ope.config(bg = "#A6FA3E")
        self.ventana_ope.title("Operaciones")
        self.ventana_ope.geometry("200x300")

        frameO =  Frame(self.ventana_ope)
        frameO.config(bg = "#014A42")
        frameO.pack(pady = 20)

        boton1 = Button(frameO, text = "limpiar zona", width = 20, command = self.ventana_limpiar)
        boton1.grid(row = 0, column = 0,pady = 10)
        
        Button(frameO, text = "Agregar linea horizontal", width = 20, command = self.ventana_lineH).grid(row = 1, column = 0, pady = 10)
        Button(frameO, text = "Agregar linea vertical", width = 20, command = self.ventana_lineV).grid(row = 2, column = 0,pady = 10)
        Button(frameO, text = "Agregar rectangulo", width = 20, command = self.ventana_Rectangulo).grid(row = 3, column = 0, pady = 10)
        Button(frameO, text = "Agregar triangulo", width = 20, command = self.ventana_Triangulo).grid(row = 4, column = 0, pady = 10)

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
                    y = 0
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
    
    def ventana_lineH(self):

        def linea_horizontal():
            f = fini.get()
            c1 = cini.get()
            c2 = ffi.get()
            self.m.linea_horizontal(int(f),int(c1),int(c2))
            a = self.m.cadena_grap()
            s = Source(a,filename="edit.gv",format="png")
            s.view()
            self.img2 = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/edit.gv.png"))
            self.lab2 =Label(self.frame2, image = self.img2)
            self.lab2.grid(row = 1,column = 1, padx = 10,pady = 10, sticky = "nsew")
            
            self.labE.config(text = "Linea Horizontal")
            self.ventana_data2.destroy()

        self.ventana_data2 = Toplevel()
        self.ventana_data2.title("Datos")
        self.ventana_data2.geometry("200x200")
        self.ventana_data2.config(bg = "#A6FA3E")

        frama3 = Frame(self.ventana_data2)
        frama3.pack(pady = 5)
        
        lb1 = Label(frama3, text = "Fila : ")
        lb1.grid(row = 0, column  = 0 , pady = 5, padx = 5)
        
        fini = Entry(frama3, width = 5)
        fini.grid(row = 0, column  = 1 , pady = 5, padx = 5)

        lb2 = Label(frama3, text = "columna Inicial: ")
        lb2.grid(row = 1, column  = 0 , pady = 5, padx = 5)

        cini = Entry(frama3, width = 5)
        cini.grid(row = 1, column  = 1 , pady = 5, padx = 5)

        lb3 = Label(frama3, text = "columna Final: ")
        lb3.grid(row = 2, column  = 0 , pady = 5, padx = 5)

        ffi = Entry(frama3, width = 5)
        ffi.grid(row = 2, column  = 1 , pady = 5, padx = 5)

        bt1 = Button(frama3, text = "Aceptar", command = linea_horizontal)
        bt1.grid(row = 3, column = 0, columnspan = 2, sticky = "we")

        self.ventana_ope.destroy()

    def ventana_limpiar(self):

        def limpiar():
            f1 = fini.get()
            c1 = cini.get()
            f2 = ffi.get()
            c2 = cfi.get()
            self.m.limpiar_espacio(int(f1),int(c1),int(f2),int(c2))
            a = self.m.cadena_grap()
            s = Source(a,filename="edit.gv",format="png")
            s.view()
            self.img2 = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/edit.gv.png"))
            self.lab2 =Label(self.frame2, image = self.img2)
            self.lab2.grid(row = 1,column = 1, padx = 10,pady = 10, sticky = "nsew")
            
            self.labE.config(text = "Limpiar zona")
            self.ventana_data1.destroy()

        self.ventana_data1 = Toplevel()
        self.ventana_data1.title("Datos")
        self.ventana_data1.geometry("200x200")
        self.ventana_data1.config(bg = "#A6FA3E")

        frama3 = Frame(self.ventana_data1)
        frama3.pack(pady = 5)
        
        lb1 = Label(frama3, text = "Fila Inicial: ")
        lb1.grid(row = 0, column  = 0 , pady = 5, padx = 5)
        
        fini = Entry(frama3, width = 5)
        fini.grid(row = 0, column  = 1 , pady = 5, padx = 5)

        lb2 = Label(frama3, text = "columna Inicial: ")
        lb2.grid(row = 1, column  = 0 , pady = 5, padx = 5)

        cini = Entry(frama3, width = 5)
        cini.grid(row = 1, column  = 1 , pady = 5, padx = 5)

        lb3 = Label(frama3, text = "Fila Final: ")
        lb3.grid(row = 2, column  = 0 , pady = 5, padx = 5)

        ffi = Entry(frama3, width = 5)
        ffi.grid(row = 2, column  = 1 , pady = 5, padx = 5)

        lb4 = Label(frama3, text = "columna Final: ")
        lb4.grid(row = 3, column  = 0 , pady = 5, padx = 5)

        cfi = Entry(frama3, width = 5)
        cfi.grid(row = 3, column  = 1 , pady = 5, padx = 5)

        bt1 = Button(frama3, text = "Aceptar", command = limpiar)
        bt1.grid(row = 4, column = 0, columnspan = 2, sticky = "we")

        self.ventana_ope.destroy()  

    def ventana_lineV(self):

        def linea_Vertical():
            c = fini.get()
            f1 = cini.get()
            f2 = ffi.get()
            self.m.linea_vertical(int(c),int(f1),int(f2))
            a = self.m.cadena_grap()
            s = Source(a,filename="edit.gv",format="png")
            s.view()
            self.img2 = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/edit.gv.png"))
            self.lab2 =Label(self.frame2, image = self.img2)
            self.lab2.grid(row = 1,column = 1, padx = 10,pady = 10, sticky = "nsew")
            
            self.labE.config(text = "Linea Vertical")
            self.ventana_data3.destroy()

        self.ventana_data3 = Toplevel()
        self.ventana_data3.title("Datos")
        self.ventana_data3.geometry("200x200")
        self.ventana_data3.config(bg = "#A6FA3E")

        frama3 = Frame(self.ventana_data3)
        frama3.pack(pady = 5)
        
        lb1 = Label(frama3, text = "columna : ")
        lb1.grid(row = 0, column  = 0 , pady = 5, padx = 5)
        
        fini = Entry(frama3, width = 5)
        fini.grid(row = 0, column  = 1 , pady = 5, padx = 5)

        lb2 = Label(frama3, text = "fila Inicial: ")
        lb2.grid(row = 1, column  = 0 , pady = 5, padx = 5)

        cini = Entry(frama3, width = 5)
        cini.grid(row = 1, column  = 1 , pady = 5, padx = 5)

        lb3 = Label(frama3, text = "fila Final: ")
        lb3.grid(row = 2, column  = 0 , pady = 5, padx = 5)

        ffi = Entry(frama3, width = 5)
        ffi.grid(row = 2, column  = 1 , pady = 5, padx = 5)

        bt1 = Button(frama3, text = "Aceptar", command = linea_Vertical)
        bt1.grid(row = 3, column = 0, columnspan = 2, sticky = "we")

        self.ventana_ope.destroy()

    def ventana_Rectangulo(self):

        def rectangulo():
            f1 = fini.get()
            c1 = cini.get()
            f2 = ffi.get()
            c2 = cfi.get()
            self.m.agregar_rectangulo(int(f1),int(c1),int(f2),int(c2))
            a = self.m.cadena_grap()
            s = Source(a,filename="edit.gv",format="png")
            s.view()
            self.img2 = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/edit.gv.png"))
            self.lab2 =Label(self.frame2, image = self.img2)
            self.lab2.grid(row = 1,column = 1, padx = 10,pady = 10, sticky = "nsew")
            
            self.labE.config(text = "Agregando rectangulo")
            self.ventana_data4.destroy()

        self.ventana_data4 = Toplevel()
        self.ventana_data4.title("Datos")
        self.ventana_data4.geometry("200x200")
        self.ventana_data4.config(bg = "#A6FA3E")

        frama3 = Frame(self.ventana_data4)
        frama3.pack(pady = 5)
        
        lb1 = Label(frama3, text = "Coordenada X Inicial: ")
        lb1.grid(row = 0, column  = 0 , pady = 5, padx = 5)
        
        fini = Entry(frama3, width = 5)
        fini.grid(row = 0, column  = 1 , pady = 5, padx = 5)

        lb2 = Label(frama3, text = "Coordenan Y Inicial: ")
        lb2.grid(row = 1, column  = 0 , pady = 5, padx = 5)

        cini = Entry(frama3, width = 5)
        cini.grid(row = 1, column  = 1 , pady = 5, padx = 5)

        lb3 = Label(frama3, text = "Cantidad de Final: ")
        lb3.grid(row = 2, column  = 0 , pady = 5, padx = 5)

        ffi = Entry(frama3, width = 5)
        ffi.grid(row = 2, column  = 1 , pady = 5, padx = 5)

        lb4 = Label(frama3, text = "Cantidad de Columnas: ")
        lb4.grid(row = 3, column  = 0 , pady = 5, padx = 5)

        cfi = Entry(frama3, width = 5)
        cfi.grid(row = 3, column  = 1 , pady = 5, padx = 5)

        bt1 = Button(frama3, text = "Aceptar", command = rectangulo)
        bt1.grid(row = 4, column = 0, columnspan = 2, sticky = "we")

        self.ventana_ope.destroy()  

    def ventana_Triangulo(self):

        def triangulo():
            x = fini.get()
            y = cini.get()
            t = ffi.get()
            self.m.agregar_triangulo(int(x),int(y),int(t))
            a = self.m.cadena_grap()
            s = Source(a,filename="edit.gv",format="png")
            s.view()
            self.img2 = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/edit.gv.png"))
            self.lab2 =Label(self.frame2, image = self.img2)
            self.lab2.grid(row = 1,column = 1, padx = 10,pady = 10, sticky = "nsew")
            
            self.labE.config(text = "Agregando Triangulo")
            self.ventana_data5.destroy()

        self.ventana_data5 = Toplevel()
        self.ventana_data5.title("Datos")
        self.ventana_data5.geometry("200x200")
        self.ventana_data5.config(bg = "#A6FA3E")

        frama3 = Frame(self.ventana_data5)
        frama3.pack(pady = 5)
        
        lb1 = Label(frama3, text = "Coordenada x : ")
        lb1.grid(row = 0, column  = 0 , pady = 5, padx = 5)
        
        fini = Entry(frama3, width = 5)
        fini.grid(row = 0, column  = 1 , pady = 5, padx = 5)

        lb2 = Label(frama3, text = "Coordenada Y: ")
        lb2.grid(row = 1, column  = 0 , pady = 5, padx = 5)

        cini = Entry(frama3, width = 5)
        cini.grid(row = 1, column  = 1 , pady = 5, padx = 5)

        lb3 = Label(frama3, text = "Tamaño de lados: ")
        lb3.grid(row = 2, column  = 0 , pady = 5, padx = 5)

        ffi = Entry(frama3, width = 5)
        ffi.grid(row = 2, column  = 1 , pady = 5, padx = 5)

        bt1 = Button(frama3, text = "Aceptar", command = triangulo)
        bt1.grid(row = 3, column = 0, columnspan = 2, sticky = "we")

        self.ventana_ope.destroy()
ventanaP = Tk()
app = window(ventanaP)
ventanaP.mainloop()