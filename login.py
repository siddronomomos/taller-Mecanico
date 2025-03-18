from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, PhotoImage, messagebox
from typing import Callable, Any
from dbUser import dbUser
from user import user


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "login"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title("Login Taller Mecanico")
window.iconbitmap(relative_to_assets("icon.ico"))
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f'{width}x{height}+{x}+{y}')

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "flat",
)

canvas.place(x = 0, y = 0)

class CanvasButton:
    """ Create leftmost mouse button clickable canvas image object.

    The x, y coordinates are relative to the top-left corner of the canvas.
    """

    def __init__(self, canvas: Canvas, x: int, y: int, image_path: Path, command: str | Callable[[], Any], state=tk.NORMAL):
        self.canvas = canvas
        self.btn_image = PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state,
                                                      image=self.btn_image)
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


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    638.0,
    360.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    960.0,
    319.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#444444",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=841.5,
    y=295.0,
    width=237.0,
    height=51.0
)

entry_2 = Entry(
    bd=0,
    bg="#444444",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=841.5,
    y=385.0,
    width=184.0,
    height=51.0
)
entry_2.config(show='*')

image_eye_closed = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1079.0,
    412.0,
    image=image_eye_closed
)

image_eye_open = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1079.0,
    412.0,
    image=image_eye_open
)
canvas.itemconfig(image_3, state=tk.HIDDEN)

def show_hide_password():
    if entry_2.cget('show') == '':
        entry_2.config(show='*')
        canvas.itemconfig(image_3, state=tk.HIDDEN)
        canvas.itemconfig(image_2, state=tk.NORMAL)
    else:
        entry_2.config(show='')
        canvas.itemconfig(image_2, state=tk.HIDDEN)
        canvas.itemconfig(image_3, state=tk.NORMAL)


CanvasButton(canvas, 1062, 395, relative_to_assets("button_1.png"), lambda: show_hide_password())

def login():
    u = user()
    db = dbUser()
    u.setUserName(entry_1.get())
    u.setPassword(entry_2.get())
    result = db.login(u).getPerfil() if db.login(u) else None
    if result:
        messagebox.showinfo("Éxito", "Usuario encontrado, perfil: " + result)
    else:
        messagebox.showerror("Error", "Usuario no encontrado")

CanvasButton(canvas, 880, 501, relative_to_assets("button_2.png"), lambda: login())

window.resizable(False, False)
window.mainloop()
