# Importar librería
from tkinter import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Ventana principal
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

ventana_principal = Tk()
ventana_principal.title("Bandera de Noruega - Alfonzo")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="purple")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Área de la bandera (Frame rojo de fondo)
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

bandera = Frame(ventana_principal)
bandera.config(bg="red", width=600, height=400)
bandera.place(x=100, y=50)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Cruz blanca
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

# Vertical blanca
cruz_blanca_v = Frame(ventana_principal)
cruz_blanca_v.config(bg="white", width=60, height=400)
cruz_blanca_v.place(x=240, y=50)

# Horizontal blanca
cruz_blanca_h = Frame(ventana_principal)
cruz_blanca_h.config(bg="white", width=600, height=60)
cruz_blanca_h.place(x=100, y=190)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Cruz azul
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

# Vertical azul
cruz_azul_v = Frame(ventana_principal)
cruz_azul_v.config(bg="blue", width=30, height=400)
cruz_azul_v.place(x=255, y=50)

# Horizontal azul
cruz_azul_h = Frame(ventana_principal)
cruz_azul_h.config(bg="blue", width=600, height=30)
cruz_azul_h.place(x=100, y=205)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Ejecutar ventana
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

ventana_principal.mainloop()
