from tkinter import *
ventana_principal = Tk()
ventana_principal.title("Colombia")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="Black")

Frame_1 = Frame(ventana_principal)
Frame_1.config(bg="Yellow", width= 800, height= 380)
Frame_1.place(x=0, y=-10)
Frame_3 = Frame(ventana_principal)
Frame_3.config(bg="Red", width= 800, height= 120)
Frame_3.place(x=0, y=380)

Frame_2 = Frame(ventana_principal)
Frame_2.config(bg="Blue", width= 800, height= 140)
Frame_2.place(x=0, y=260)
ventana_principal.mainloop()