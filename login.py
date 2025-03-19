from pathlib import Path
from time import sleep
import tkinter as tk
from tkinter import Tk, Canvas, Entry, PhotoImage, messagebox
from typing import Callable, Any
from dbUser import dbUser
from user import user


class CanvasButton:
    def __init__(self, canvas: Canvas, x: int, y: int, image_path: Path, command: Callable[[], Any], state=tk.NORMAL):
        self.canvas = canvas
        self.btn_image = PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state, image=self.btn_image)
        self.command = command
        self.x = x
        self.y = y
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonPress-1>", self.on_press)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.canvas.move(self.canvas_btn_img_obj, 1, 1)

    def on_release(self, event):
        self.canvas.move(self.canvas_btn_img_obj, -1, -1)
        self.command()


class LoginWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Login Taller Mecanico")
        self.ASSETS_PATH = Path(__file__).parent / "assets" / "login"
        self.window.iconbitmap(self.relative_to_assets("icon.ico"))
        self.center_window()

        self.canvas = Canvas(
            self.window, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="flat"
        )
        self.canvas.place(x=0, y=0)
        self.create_widgets()

        self.window.resizable(False, False)
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        self.image_background = PhotoImage(file=self.relative_to_assets("background.png"))
        self.canvas.create_image(638.0, 360.0, image=self.image_background)

        self.entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(960.0, 319.5, image=self.entry_image)
        
        self.entry_username = Entry(bd=0, bg="#444444", fg="#FFFFFF", highlightthickness=0)
        self.entry_username.place(x=841.5, y=295.0, width=237.0, height=51.0)

        self.entry_password = Entry(bd=0, bg="#444444", fg="#FFFFFF", highlightthickness=0, show='*')
        self.entry_password.place(x=841.5, y=385.0, width=184.0, height=51.0)
        
        self.image_eye_closed = PhotoImage(file=self.relative_to_assets("eye_closed.png"))
        self.image_eye_open = PhotoImage(file=self.relative_to_assets("eye_open.png"))

        self.eye_button = self.canvas.create_image(1079.0, 412.0, image=self.image_eye_closed)
        self.canvas.tag_bind(self.eye_button, "<ButtonPress-1>", lambda e: self.show_hide_password())

        CanvasButton(self.canvas, 880, 501, self.relative_to_assets("login_button.png"), self.login)

    def show_hide_password(self):
        if self.entry_password.cget('show') == '':
            self.entry_password.config(show='*')
            self.canvas.itemconfig(self.eye_button, image=self.image_eye_closed)
        else:
            self.entry_password.config(show='')
            self.canvas.itemconfig(self.eye_button, image=self.image_eye_open)

    def login(self):
        u = user()
        db = dbUser()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Usuario y contraseña son requeridos")
            return

        u.setUserName(username)
        u.setPassword(password)

        if not db.login(u):
            messagebox.showerror("Error", "Usuario y/o contraseña incorrectos")
            return

        messagebox.showinfo("Login", "Login exitoso")


if __name__ == "__main__":
    LoginWindow()
