from tkinter import Canvas, Event, NW
from pathlib import Path
from typing import Literal
from PIL import Image, ImageTk, ImageDraw, ImageFont


class Toast:
    def __init__(self, parent: Canvas, message: str, duration: int = 2000, type: Literal["info", "success", "warning", "error"] = "info", corner_radius: int = 10) -> None:
        self.parent = parent
        self.message = message
        self.duration = duration
        self.type = type
        self.corner_radius = corner_radius
        self.alpha = 1.0
        self.images = []  # Prevent garbage collection
        self.colors = {
            "info": "#2196F3",
            "success": "#4CAF50",
            "warning": "#FFC107",
            "error": "#F44336",
        }

        self.bg_color = self.colors.get(self.type, "#2196F3")
        self.padding = 20  # Padding around the text
        self.font_size = 16  # Default font size
        self.font = ImageFont.load_default()  # Default font
        self.create_toast()
        self.show_toast()

    def create_rounded_rectangle(self, width, height, radius, color, alpha=1.0):
        img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        alpha = int(alpha * 255)
        fill_color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) + (alpha,)
        draw.rounded_rectangle((0, 0, width, height), radius, fill=fill_color)
        img_tk = ImageTk.PhotoImage(img)
        self.images.append(img_tk)  # Store reference
        return img_tk

    def create_text_image(self, text, font_size=16, color="white", alpha=1.0):
        font = ImageFont.truetype("arial.ttf", font_size)  # Use a truetype font for better scaling
        dummy_img = Image.new("RGBA", (1, 1))
        draw = ImageDraw.Draw(dummy_img)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        img = Image.new("RGBA", (text_width + 10, text_height + 10), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        font_color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) + (int(alpha * 255),)
        draw.text((5, 5), text, fill=font_color, font=font)

        img_tk = ImageTk.PhotoImage(img)
        self.images.append(img_tk)  # Store reference
        return img_tk, text_width, text_height

    def create_toast(self) -> None:
        # Calcular dinámicamente el tamaño del toast basado en el texto
        self.text_img, text_width, text_height = self.create_text_image(self.message, font_size=self.font_size, color="#FFFFFF")
        self.width = text_width + self.padding * 2  # Ajustar el ancho basado en el texto y el padding
        self.height = max(text_height + self.padding * 2, 50)  # Altura mínima para evitar que sea demasiado pequeño

        canvas_width = self.parent.winfo_width()
        canvas_height = self.parent.winfo_height()

        self.x = (canvas_width - self.width) // 2
        self.y = canvas_height - int(self.height * 2.5)

        # Crear el rectángulo de fondo
        self.bg_img = self.create_rounded_rectangle(self.width, self.height, self.corner_radius, self.bg_color)
        self.bg = self.parent.create_image(self.x, self.y, image=self.bg_img, anchor=NW)

        # Posicionar el texto completamente centrado dentro del rectángulo
        self.text = self.parent.create_image(
            self.x + (self.width // 2),  # Centrado horizontalmente
            self.y + (self.height // 2),  # Centrado verticalmente
            image=self.text_img,
            anchor="center"  # Anclado al centro
        )
        self.parent.tag_raise(self.text)

        # Vincular clics fuera del toast para cerrarlo
        self.parent.bind("<Button-1>", self.check_outside_click, add=True)
        self.parent.after(self.duration, self.fade_out)

    def check_outside_click(self, event: Event) -> None:
        if not (self.x <= event.x <= self.x + self.width and self.y <= event.y <= self.y + self.height):
            self.fade_out()

    def fade_out(self, alpha=1.0):
        if alpha <= 0:
            self.parent.delete(self.bg)
            self.parent.delete(self.text)
            del self
            return

        self.bg_img = self.create_rounded_rectangle(self.width, self.height, self.corner_radius, self.bg_color, alpha)
        self.parent.itemconfig(self.bg, image=self.bg_img)

        self.text_img, _, _ = self.create_text_image(self.message, font_size=self.font_size, color="#FFFFFF", alpha=alpha)
        self.parent.itemconfig(self.text, image=self.text_img)

        self.parent.after(50, self.fade_out, alpha - 0.05)

    def show_toast(self) -> None:
        self.parent.itemconfig(self.bg, state="normal")
        self.parent.itemconfig(self.text, state="normal")
        self.parent.tag_raise(self.text)  # Asegurar que el texto esté encima
