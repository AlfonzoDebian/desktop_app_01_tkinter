from tkinter import *

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Función para manejar clics
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

def mostrar_coordenadas(event):
    x = event.x
    y = event.y

    # Dibujar punto en la coordenada
    canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")

    # Mostrar coordenadas en la etiqueta
    etiqueta.config(text=f"Coordenadas: ({x}, {y})")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Ventana principal
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

ventana = Tk()
ventana.title("Plano Cartesiano Interactivo")
ventana.geometry("600x600")
ventana.resizable(0, 0)
ventana.config(bg="lightgray")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Canvas para el plano
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

canvas = Canvas(ventana, width=500, height=500, bg="white")
canvas.place(x=50, y=50)

# Dibujar ejes cartesianos
canvas.create_line(250, 0, 250, 500, fill="gray")  # eje Y
canvas.create_line(0, 250, 500, 250, fill="gray")  # eje X

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Etiqueta para mostrar coordenadas
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

etiqueta = Label(ventana, text="Haz clic en el plano", bg="lightgray", font=("Arial", 14))
etiqueta.place(x=200, y=10)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Evento de clic en el canvas
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

canvas.bind("<Button-1>", mostrar_coordenadas)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# Ejecutar ventana
# :::::::::::::::::::::::::::::::::::::::::::::::::::::

ventana.mainloop()
