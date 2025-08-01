import tkinter as tk
from tkinter import filedialog

class RutaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Selector de Ruta")
        self.root.geometry("400x200")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Ruta seleccionada:", bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=10)

        self.ruta_var = tk.StringVar()
        self.ruta_entry = tk.Entry(root, textvariable=self.ruta_var, width=50)
        self.ruta_entry.pack(pady=5)

        self.btn_archivo = tk.Button(root, text="Seleccionar archivo", command=self.seleccionar_archivo)
        self.btn_archivo.pack(pady=5)

        self.btn_carpeta = tk.Button(root, text="Seleccionar carpeta", command=self.seleccionar_carpeta)
        self.btn_carpeta.pack(pady=5)

    def seleccionar_archivo(self):
        ruta = filedialog.askopenfilename(title="Selecciona un archivo")
        if ruta:
            self.ruta_var.set(ruta)

    def seleccionar_carpeta(self):
        ruta = filedialog.askdirectory(title="Selecciona una carpeta")
        if ruta:
            self.ruta_var.set(ruta)

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = RutaApp(root)
    root.mainloop()
