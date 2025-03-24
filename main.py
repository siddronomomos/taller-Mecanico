from mainWindow import mainWindow
from loginCanvas import LoginCanvas
from dbUser import dbUser
from tkinter import messagebox, Tk

if __name__ == "__main__":
    try:
        db = dbUser()
        if not db.test_connection():
            raise ConnectionError("Error al conectar con la base de datos.")
        del db


    except Exception as e:
        root = Tk()
        root.withdraw()
        messagebox.showerror("Error crítico", f"No se pudo conectar con la base de datos.\nDetalles: {e}")
        root.destroy()

    try:
        app = mainWindow()
        app.switch_canvas(LoginCanvas)
        app.window.mainloop()

    except Exception as e:
        root = Tk()
        root.withdraw()
        messagebox.showerror("Error crítico", f"Ocurrió un error inesperado.\nDetalles: {e}")
        root.destroy()