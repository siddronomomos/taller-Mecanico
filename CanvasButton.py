from tkinter import Canvas, PhotoImage, NORMAL
from typing import Callable, Any, Optional
from pathlib import Path


class CanvasButton:
    def __init__(self, canvas: Canvas, x: int, y: int, command: Callable[[], Any], image_path: Path, hover_image_path: Optional[Path] = None, state=NORMAL):
        self.canvas = canvas
        self.btn_image = PhotoImage(file=image_path)
        self.hover_image = PhotoImage(file=hover_image_path) if hover_image_path else None
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state, image=self.btn_image)
        self.command = command
        self.x = x
        self.y = y

        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonPress-1>", self.on_press)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", self.on_release)
        if self.hover_image:
            canvas.tag_bind(self.canvas_btn_img_obj, "<Enter>", self.on_hover)
            canvas.tag_bind(self.canvas_btn_img_obj, "<Leave>", self.on_leave)

    def on_press(self, event):
        self.canvas.move(self.canvas_btn_img_obj, 1, 1)

    def on_release(self, event):
        self.canvas.move(self.canvas_btn_img_obj, -1, -1)
        self.command()

    def on_hover(self, event):
        if self.hover_image:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.hover_image)

    def on_leave(self, event):
        self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image)