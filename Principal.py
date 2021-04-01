from tkinter import *

def mensaje():
    print("mensaje de boton")

ventana = Tk()
ventana.geometry("600x400") 
ventana.title("Ventana Hola mundo")

lbl = Label(ventana, text = "este es un label de tkinter")
lbl.pack()

btn = Button(ventana, text = "presiona este boton para mensaje", command = mensaje)
btn.pack()

ventana.mainloop()