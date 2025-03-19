from tkinter import Canvas, PhotoImage, NORMAL
from typing import Callable, Any
from pathlib import Path


class CanvasButton:
    def __init__(self, canvas: Canvas, x: int, y: int, image_path: Path, command: Callable[[], Any], state=NORMAL):
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