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

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="flat")
        self.canvas.pack(fill="both", expand=True)

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def switch_canvas(self, new_canvas_class: Type[Canvas]) -> None:
        """Replaces the current canvas with a new one."""
        self.canvas.destroy()
        self.canvas = new_canvas_class(self.window, self)
        self.canvas.pack(fill="both", expand=True)

