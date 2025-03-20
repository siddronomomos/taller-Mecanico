from mainWindow import mainWindow
from loginWindow import LoginWindow
from dbUser import dbUser
import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":
    try:
        db = dbUser()
        if not db.test_connection():
            raise ConnectionError("Error al conectar con la base de datos.")
        del db

        app = mainWindow()
        app.switch_canvas(LoginWindow)
        app.window.mainloop()

    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error crítico", f"No se pudo conectar con la base de datos.\nDetalles: {e}")
        root.destroy()