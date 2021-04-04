from tkinter import *
from tkinter import filedialog
import xml.etree.ElementTree as ET


def ventanaCargar():
    archivo_entrada = filedialog.askopenfilename(initialdir = "C:/Users/jezeh/OneDrive/Escritorio/IPC2/Proyecto2_ipc2",title = "Selecciona un archivo",filetypes =(("xml files","*.xml"),("xml files","*.*")))
    print(archivo_entrada)

    archivo = ET.parse(archivo_entrada)
    root = archivo.getroot()

    for element in root:
        print(element)
        for subelement in element:
            print(subelement.text)
    

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