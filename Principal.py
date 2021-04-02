from tkinter import *

def mensaje():
    print("mensaje de boton")

ventana = Tk()
ventana.geometry("600x400") 
ventana.title("PRINCIPAL")

lbl = Label(ventana, text = "este es un label de tkinter")
lbl.pack()

btn = Button(ventana, text = "BUSCAR", command = mensaje)
btn.pack()
btn1 = Button(ventana, text = "HOLA", command = mensaje)
btn1.pack()
btn2 = Button(ventana, text = "JAJA", command = mensaje)
btn2.pack()
ventana.mainloop()