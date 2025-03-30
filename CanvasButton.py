from tkinter import Canvas, Event, NORMAL, HIDDEN
from typing import Callable, Any, Optional
from pathlib import Path
from PIL import Image, ImageTk


class CanvasButton:
    def __init__(self, canvas: Canvas, x: int, y: int, command: Callable[[], Any], image_path: Path,
                 hover_image_path: Optional[Path] = None, state=NORMAL, hide_on_click_outside=False,
                 toggle_on_click=False):
        self.canvas = canvas
        self.original_image = Image.open(image_path)
        self.btn_image = ImageTk.PhotoImage(self.original_image)
        self.hover_image = ImageTk.PhotoImage(Image.open(hover_image_path)) if hover_image_path else None
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state, image=self.btn_image)
        self.command = command
        self.x = x
        self.y = y
        self.hide_on_click_outside = hide_on_click_outside
        self.toggle_on_click = toggle_on_click
        self.width = self.btn_image.width()
        self.height = self.btn_image.height()
        self.selected = False

        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonPress-1>", self.on_press)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", self.on_release)
        if self.hover_image:
            canvas.tag_bind(self.canvas_btn_img_obj, "<Enter>", self.on_hover)
            canvas.tag_bind(self.canvas_btn_img_obj, "<Leave>", self.on_leave)

        if hide_on_click_outside:
            canvas.bind("<Button-1>", self.check_outside_click, add=True)

    def on_press(self, event: Event):
        self.canvas.move(self.canvas_btn_img_obj, 1, 1)

    def on_release(self, event: Event):
        self.canvas.move(self.canvas_btn_img_obj, -1, -1)
        self.command()
        if self.toggle_on_click:
            self.toggle_selected()

    def on_hover(self, event: Event):
        if self.hover_image and not self.selected:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.hover_image)

    def on_leave(self, event: Event):
        if not self.selected:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image)

    def check_outside_click(self, event: Event):
        if not (self.x <= event.x <= self.x + self.width and self.y <= event.y <= self.y + self.height):
            self.fade_out()

    def fade_out(self, alpha=255):
        if alpha <= 0:
            self.hide()
            return

        faded_image = self.original_image.copy()
        if faded_image.mode != "RGBA":
            faded_image = faded_image.convert("RGBA")

        r, g, b, a = faded_image.split()
        a = a.point(lambda p: p * (alpha / 255))
        faded_image = Image.merge("RGBA", (r, g, b, a))

        self.btn_image = ImageTk.PhotoImage(faded_image)
        self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image)

        self.canvas.after(50, self.fade_out, alpha - 15)

    def hide(self):
        self.canvas.itemconfig(self.canvas_btn_img_obj, state=HIDDEN)

    def show(self):
        self.canvas.itemconfig(self.canvas_btn_img_obj, state=NORMAL)

    def toggle_selected(self):
        if self.selected:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image)
        else:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.hover_image)
        self.selected = not self.selected

    def reset(self):
        self.selected = False
        self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image)
        self.show()
