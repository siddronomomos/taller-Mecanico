from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage
from dbUser import dbUser
from user import User
from CanvasButton import CanvasButton
from mainWindow import mainWindow
from Toast import Toast
from backgroundCanvas import BackgroundCanvas

class LoginCanvas(Canvas):
    def __init__(self, parent: Canvas, controller: mainWindow) -> None:
        super().__init__(parent, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="flat")
        self.controller = controller
        self.ASSETS_PATH = Path(__file__).parent / "assets" / "login"
        self.create_widgets()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def create_widgets(self):
        self.image_background = PhotoImage(file=self.relative_to_assets("background.png"))
        self.create_image(638.0, 360.0, image=self.image_background)

        self.entry_image = PhotoImage(file=self.relative_to_assets("entry_background.png"))
        self.create_image(960.0, 319.5, image=self.entry_image)
        
        self.entry_username = Entry(self, bd=0, bg="#444444", fg="#FFFFFF", highlightthickness=0, validate="key")
        self.entry_username.place(x=841.5, y=295.0, width=237.0, height=51.0)
        self.entry_username.configure(validatecommand=(self.register(self.limit_input), '%P'))

        self.entry_password = Entry(self, bd=0, bg="#444444", fg="#FFFFFF", highlightthickness=0, show='*')
        self.entry_password.place(x=841.5, y=385.0, width=184.0, height=51.0)
        self.entry_password.configure(validatecommand=(self.register(self.limit_input), '%P'))
        
        self.image_eye_closed = PhotoImage(file=self.relative_to_assets("eye_closed.png"))
        self.image_eye_open = PhotoImage(file=self.relative_to_assets("eye_open.png"))

        self.eye_button = self.create_image(1079.0, 412.0, image=self.image_eye_closed)
        self.tag_bind(self.eye_button, "<ButtonPress-1>", lambda e: self.show_hide_password())

        self.login_button = CanvasButton(self, 880, 501, self.login, self.relative_to_assets("login_button.png"), self.relative_to_assets("login_button_hover.png"))

    def limit_input(self, new_value: str) -> bool:
        return len(new_value) <= 30

    def show_hide_password(self):
        if self.entry_password.cget('show') == '':
            self.entry_password.config(show='*')
            self.itemconfig(self.eye_button, image=self.image_eye_closed)
        else:
            self.entry_password.config(show='')
            self.itemconfig(self.eye_button, image=self.image_eye_open)

    def login(self) -> None:
        u = User()
        db = dbUser()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if not username or not password:
            _ = Toast(self, "Por favor, complete todos los campos", 2000, "warning", corner_radius=20)
            del _
            return

        u.setUserName(username)
        u.setPassword(password)
        u = db.login(u)

        if not u:
            _ = Toast(self, "Usuario o contraseña incorrectos", 2000, "error", corner_radius=20)
            del _
            return
        
        
        self.controller.switch_canvas(BackgroundCanvas, u)