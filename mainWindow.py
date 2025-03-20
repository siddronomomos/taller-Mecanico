from tkinter import Tk
from pathlib import Path

class mainWindow:
    def __init__(self):
        self.window = Tkin()
        self.window.geometry("1280x720")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Taller Mecanico")
        self.ASSETS_PATH = Path(__file__).parent / "assets" / "main"
        self.window.iconbitmap(self.relative_to_assets("icon.ico"))

    
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')