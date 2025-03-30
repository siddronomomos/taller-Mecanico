from pathlib import Path
from tkinter import Canvas, PhotoImage
from CanvasButton import CanvasButton
from mainWindow import mainWindow
from user import User


class  BackgroundCanvas(Canvas):
    def __init__(self, parent: Canvas, controller: mainWindow, user: User) -> None:
        super().__init__(parent, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="flat")
        self.controller = controller
        self.user = user
        self.ASSETS_PATH = Path(__file__).parent / "assets" / "background"
        self.create_widgets()
        self.selected = None

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def create_widgets(self):
        self.image_background = PhotoImage(file=self.relative_to_assets("background.png"))
        self.create_image(640.0, 360.0, image=self.image_background)

        self.top_image = PhotoImage(file=self.relative_to_assets(f"top_{self.user.getPerfil()}.png"))
        self.create_image(765.0, 28.0, image=self.top_image)
        
        self.create_text(1220.0, 12.0, anchor="ne", text=self.user.getUserName(), fill="#FFFFFF", font=("Roboto Regular", 10 * -1), justify="right")
        self.create_text(1220.0, 26.0, anchor="ne", text=self.user.getNombre(), fill="#7E7E7E", font=("Roboto Regular", 10 * -1), justify="right")
    
        self.profile_button = CanvasButton(self, 1228, 10, self.show_logout_button, self.relative_to_assets(f"button_profile.png"), self.relative_to_assets(f"button_profile_hover.png"))
        
        self.home_button = CanvasButton(self, 265, 78, self.go_to_home, self.relative_to_assets(f"button_home.png"))
        self.create_text(284.0, 78.0, anchor="nw", text="/", fill="#7E7E7E", font=("Roboto Regular", 13 * -1))

        self.user_button = CanvasButton(self, 0, 216, self.go_to_user, self.relative_to_assets(f"button_user.png"), self.relative_to_assets(f"button_user_hover.png"))

        self.client_button = CanvasButton(self, 0, 273, self.go_to_client, self.relative_to_assets(f"button_client.png"), self.relative_to_assets(f"button_client_hover.png"))

        self.vehicle_button = CanvasButton(self, 0, 330, self.go_to_vehicle, self.relative_to_assets(f"button_vehicle.png"), self.relative_to_assets(f"button_vehicle_hover.png"))

        self.pieces_button = CanvasButton(self, 0, 387, self.go_to_pieces, self.relative_to_assets(f"button_pieces.png"), self.relative_to_assets(f"button_pieces_hover.png"))

        self.repairs_button = CanvasButton(self, 0, 444, self.go_to_repairs, self.relative_to_assets(f"button_repairs.png"), self.relative_to_assets(f"button_repairs_hover.png"))

        self.welcome_image = PhotoImage(file=self.relative_to_assets("welcome.png"))
        self.create_image(765.0, 416.0, image=self.welcome_image)

    def show_logout_button(self):
        if hasattr(self, 'logout_button'):
            self.logout_button.hide()
            del self.logout_button
        else:
            self.logout_button = CanvasButton(self, 1133, 57, self.logout, self.relative_to_assets(f"button_logout.png"), self.relative_to_assets(f"button_logout_hover.png"), hide_on_click_outside=True)

    def logout(self):
        from loginCanvas import LoginCanvas
        self.user = None
        self.controller.switch_canvas(LoginCanvas)

    def reset_buttons(self):
        if hasattr(self, 'logout_button'):
            self.logout_button.hide()
            del self.logout_button
        self.profile_button.reset()
        self.home_button.reset()
        self.user_button.reset()
        self.client_button.reset()
        self.vehicle_button.reset()
        self.pieces_button.reset()
        self.repairs_button.reset()
        self.selected = None

    def go_to_home(self):
        return
        self.controller.switch_canvas("HomeCanvas")

    def go_to_user(self):
        self.user_button.toggle_selected()

    def go_to_client(self):
        return
        self.controller.switch_canvas("ClientCanvas")

    def go_to_vehicle(self):
        return
        self.controller.switch_canvas("VehicleCanvas")

    def go_to_pieces(self):
        return
        self.controller.switch_canvas("PiecesCanvas")

    def go_to_repairs(self):
        return
        self.controller.switch_canvas("RepairsCanvas")

