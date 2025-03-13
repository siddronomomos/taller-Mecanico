import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from dbUser import dbUser
from user import user

class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Usuarios")
        self.db = dbUser()
        
        # Labels y Entradas
        tk.Label(root, text="ID:").grid(row=0, column=0)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Nombre:").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Usuario:").grid(row=2, column=0)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=2, column=1)
        
        tk.Label(root, text="Contraseña:").grid(row=3, column=0)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=3, column=1)
        
        tk.Label(root, text="Perfil:").grid(row=4, column=0)
        self.perfil_combobox = ttk.Combobox(root, values=["Admin", "Auxiliar", "Mecánico", "Usuario"])
        self.perfil_combobox.grid(row=4, column=1)
        
        # Botones CRUD
        tk.Button(root, text="Guardar", command=self.save_user).grid(row=5, column=0)
        tk.Button(root, text="Actualizar", command=self.update_user).grid(row=5, column=1)
        tk.Button(root, text="Eliminar", command=self.delete_user).grid(row=6, column=0)
        tk.Button(root, text="Buscar", command=self.get_user).grid(row=6, column=1)
        tk.Button(root, text="Limpiar", command=self.clear_fields).grid(row=7, column=0, columnspan=2)
        
    def save_user(self):
        u = user()
        u.setNombre(self.nombre_entry.get())
        u.setUserName(self.username_entry.get())
        u.setPassword(self.password_entry.get())
        u.setPerfil(self.perfil_combobox.get())
        
        if self.db.save(u):
            messagebox.showinfo("Éxito", "Usuario guardado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo guardar el usuario")
        
    def update_user(self):
        u = user()
        u.setID(int(self.id_entry.get()))
        u.setNombre(self.nombre_entry.get())
        u.setUserName(self.username_entry.get())
        u.setPassword(self.password_entry.get())
        u.setPerfil(self.perfil_combobox.get())
        
        if self.db.update(u):
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el usuario")
        
    def delete_user(self):
        u = user()
        u.setID(int(self.id_entry.get()))
        
        if self.db.delete(u):
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el usuario")
        
    def get_user(self):
        u = user()
        u.setID(int(self.id_entry.get()))
        result = self.db.get(u)
        
        if result:
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, result.getNombre())
            
            self.username_entry.delete(0, tk.END)
            self.username_entry.insert(0, result.getUserName())
            
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, result.getPassword())
            
            self.perfil_combobox.set(result.getPerfil())
        else:
            messagebox.showerror("Error", "Usuario no encontrado")
    
    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.perfil_combobox.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()
