from tkinter import *


noruega = Tk()
noruega.title("Bandera de Noruega")
noruega.geometry("320x220")
noruega.resizable(False, False)


margen = 10


fondo = Frame(noruega, bg="red", width=300, height=200)
fondo.place(x=margen, y=margen)



blanco_v = Frame(noruega, bg="white", width=30, height=200)
blanco_v.place(x=90 + margen, y=margen)


blanco_h = Frame(noruega, bg="white", width=300, height=30)
blanco_h.place(x=margen, y=85 + margen)


azul_v = Frame(noruega, bg="blue", width=15, height=200)
azul_v.place(x=97 + margen, y=margen)


azul_h = Frame(noruega, bg="blue", width=300, height=15)
azul_h.place(x=margen, y=92 + margen)


noruega.mainloop()
