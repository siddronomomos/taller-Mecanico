from tkinter import Tk, Canvas
from pathlib import Path
from typing import Type

class mainWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Taller Mecanico")
        self.ASSETS_PATH = Path(__file__).parent / "assets" / "main"
        self.window.iconbitmap(self.relative_to_assets("icon.ico"))
        self.window.resizable(False, False)
        self.center_window()

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="flat")
        self.canvas.pack(fill="both", expand=True)

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def switch_canvas(self, new_canvas_class: Type[Canvas]) -> None:
        self.canvas.destroy()
        self.canvas = new_canvas_class(self.window, self)
        self.canvas.pack(fill="both", expand=True)

