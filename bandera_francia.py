from tkinter import *

# Crear ventana
francia = Tk()
francia.title("Bandera de Francia")


francia.geometry("320x220")  
francia.resizable(False, False)


margen = 10


azul = Frame(francia, bg="blue", width=100, height=200)
azul.place(x=margen, y=margen)

blanco = Frame(francia, bg="white", width=100, height=200)
blanco.place(x=100 + margen, y=margen)

rojo = Frame(francia, bg="red", width=100, height=200)
rojo.place(x=200 + margen, y=margen)


francia.mainloop()
