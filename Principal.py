from tkinter import *
from tkinter import filedialog

def ventanaCargar():
    archivo_entrada = filedialog.askopenfilename(initialdir = "/",title = "Selecciona un archivo",filetypes =(("lfp files","*.xml"),("lfp files","*.*")))
    archivo1 = open(archivo_entrada, "r")
    texto1 = archivo1.read()
    print(texto1)

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