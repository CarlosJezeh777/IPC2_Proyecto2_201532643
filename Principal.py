from tkinter import *
from tkinter import filedialog
import xml.etree.ElementTree as ET
from Lista import Lista_Simple, Lista_xml
from matriz import matriz
from graphviz import Source
from PIL import ImageTk, Image

lista_datos = Lista_xml()
m = matriz()

def cargar1():
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
                ima1 = subelement.text
                print(ima1)
                x = 1
                y = 0
                contadorES = 0
                contadorAS = 0
                for i in ima1:
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
                        m.insertar(y,x,i)
                        x = x + 1
                contador = 0
    a = m.grafica_original()
    s = Source(a,filename="original.gv",format="png")
    s.view()
    img = ImageTk.PhotoImage(Image.open("C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2/original.gv.png"))
    lab1 =Label(frame2, image = img).grid(row = 1,column = 0, padx = 5)
    lab1.pack()
    print("asteriscos " +str(contadorAS))
    print("espacios " +str(contadorES))
    

def ventanaCargar():
    ventana_C = Toplevel()
    ventana_C.title("Cargar archivos")
    ventana_C.geometry("200x200")
    frameC = Frame(ventana_C,pady = 5)
    frameC.pack()

    boton1  =  Button(frameC, text = "Cargar 1 imagen", command  = cargar1).grid(row = 0, column = 0,pady = 20)
    boton2  =  Button(frameC, text = "Cargar 2 imagenes").grid(row = 1, column = 0,pady = 20)
   
    

def ventanaOperaciones():
    ventana_ope = Toplevel()
    ventana_ope.title("Operaciones")
    ventana_ope.geometry("200x300")

    frameO =  Frame(ventana_ope, pady = 5)
    frameO.pack()

    Button(frameO, text = "Operacion 1", width = 20).grid(row = 0, column = 0,pady = 20)
    Button(frameO, text = "Operacion 2", width = 20).grid(row = 1, column = 0, pady = 20)
    Button(frameO, text = "Operacion 3", width = 20).grid(row = 2, column = 0,pady = 20)
    Button(frameO, text = "Operacion 4", width = 20).grid(row = 3, column = 0, pady = 20)


ventanaP = Tk()
ventanaP.geometry("700x500")
ventanaP.title("Principal")
ventanaP.config(bg = "#A6FA3E")

frameB = Frame(ventanaP, pady = 5, bg = "#014A42")
frameB.grid(row  = 0, column = 0, pady =  20)
frameB.pack()

frame2 =  Frame(ventanaP, pady = 5, bg = "#014A42" )
frame2.place()
frame2.pack()

Button(frameB, text = "CARGAR ARCHIVO", width = 20, command = ventanaCargar).grid(row = 0, column = 0, padx = 5 )
Button(frameB, text = "OPERACIONES", width = 20, command = ventanaOperaciones).grid(row = 0, column = 2,padx = 5)
Button(frameB, text = "REPORTES", width = 20).grid(row = 0, column = 3,padx = 5)
Button(frameB, text = "AYUDA", width = 20).grid(row = 0, column = 4, padx = 5)

ventanaP.mainloop()