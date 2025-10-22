import tkinter as tk
from tkinter import messagebox


class Dashboardapp:
    def __init__(self, username):
       self.username = username
       self.root = tk.TK()
       self.root.title(f"Bienvenido{username}")
       self.root.geometry("600x400")
       self.root.resizable(False, False)
       
       self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text="Hola {self.username}", font=("Arial", 22, "bold")).pack(pady=10)

        tk.Button(self.root, text="ver usuario", command=self.self.ver_usuarios).pack(pady=20)

        tk.Button(self.root, text="agregar usuario", command=self.self.agregar_usuarios).pack(pady=20)

        tk.Button(self.root, text="actualizar usuario", command=self.self.actualizar_usuarios).pack(pady=20)

        tk.Button(self.root, text="eliminar usuario", command=self.self.eliminar_usuarios).pack(pady=20)

        tk.Button(self.root, text="cerrar sesion", command=self.self.cerrar_sesion).pack(pady=20)
    
    def ver_usuario(self):
        messagebox.showinfo("acción", "ver usuario")

    def agregar_usuario(self):
        messagebox.showinfo("acción", "agregar usuario")

    def actualizar_usuario(self):
        messagebox.showinfo("acción", "actualizar usuario")

    def eliminar_usuario(self):
        messagebox.showinfo("acción", "eliminar usuario")

    def cerrar_sesión(self):
        messagebox.showinfo("acción", "has cerrado sesión.")

if __name__ == "__main__":
    App = Dashboardapp("admin")