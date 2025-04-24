from os import path
import flet as ft

class RegisterTextBox(ft.TextField):
    def __init__(self, label: str, hint_text: str| None = None, password: bool | None = None, on_change: ft.OptionalEventCallable = None):
        super().__init__(
            label = label,
            hint_text = hint_text if hint_text else label,
            hint_fade_duration= 0,
            hint_style = ft.TextStyle(
                color = "#999999"
            ),
            text_size = 16,
            fill_color=ft.Colors.WHITE,
            border_width = 0.5,
            password = True if password else None,
            can_reveal_password = True if password else None,
            on_change = on_change
        )
        self.valid = False

class AdopterSignUp(ft.View):
    def __init__(self, titletext: str = "Login"):
        super().__init__("/")

        self.error_message_color = ft.Colors.RED
        self.error_border_color = ft.Colors.RED

        #Content
        self.image = ft.Image(
            src = path.join(path.dirname(__file__), "static", "cat2.jpg"), # TODO align image properly
            height=1000,
            width=900,
            fit=ft.ImageFit.FIT_HEIGHT,
            #offset=ft.Offset(0.1, 0),
            #alignment = ft.alignment.center_left,
        )
        
        self.image_overlay_text = ft.Container(
        content=ft.Text(
            spans=[
                ft.TextSpan(
                    text="PAWS",
                    style=ft.TextStyle(
                        size=40, 
                        color=ft.Colors.BLACK, 
                        weight=ft.FontWeight.NORMAL, 
                        font_family="Inria Serif", 
                    ),
                ),
                ft.TextSpan(
                    text=" & ",
                    style=ft.TextStyle(
                        size=40, 
                        color="#F06449", 
                        weight=ft.FontWeight.NORMAL, 
                        font_family="Inria Serif", 
                    ),
                ),
                ft.TextSpan(
                    text="CLAWS",
                    style=ft.TextStyle(
                        size=40, 
                        color=ft.Colors.BLACK, 
                        weight=ft.FontWeight.NORMAL, 
                        font_family="Inria Serif", 
                    ),
                ),
            ],
            offset=ft.Offset(-0.1, 0.1),
        ),
        image=ft.Image(
            src=path.join(path.dirname(__file__), "static", "paw.png"), # TODO make the paw show up
            width=100,
            height=100,
            fit=ft.ImageFit.CONTAIN,
            #offset=ft.Offset(0,0),
        ),
        alignment=ft.alignment.top_right,
        padding=10
        )

        self.image_container = ft.Container(
        content=ft.Stack(
        controls=[
            self.image,
            self.image_overlay_text
        ],
        width=805,
        height=1000
        ),
        padding=0,
        width=805,
        border_radius=ft.BorderRadius(0, 10, 0, 10),
        bgcolor=ft.Colors.BLACK,
        )

        self.TitleText = ft.ShaderMask(
            content=ft.Text(
                value=titletext,
                font_family="Inter",
                size=40,
                color=ft.Colors.WHITE,
            ),
            shader=ft.LinearGradient(
                colors=["#F95B3C", "#EB2600"],
                stops = [0.0, 0.65,],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
            ),
            blend_mode=ft.BlendMode.SRC_IN,
        )
        #self.first_name = RegisterTextBox("First Name") # TODO add hint texts
        #self.first_name.width = 200
        #self.last_name = RegisterTextBox("Last Name")
        #self.last_name.width = 200
        self.email = RegisterTextBox("Email")
        self.password = RegisterTextBox("Password", password = True)
        #self.confirm_password = RegisterTextBox("Confirm Password", password = True)

        self.login_button = ft.Container(
            content = ft.Text("Login", size=16, color="#000000"),
            width = 150,
            height = 35,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,  # No solid background
            border=ft.border.all(width = 0.5, color = "#AAAAAA"),
            border_radius=5,  # Makes it rounded
            on_click=self.on_click_login,
            on_hover=self.on_hover_login,
        )

        self.error_message = ft.Text(value="", 
            font_family="Inter", 
            size="12", 
            color=ft.Colors.RED
        )
        self.Form1 = ft.Container(
            content = ft.Column(
                controls= [
                    self.TitleText,
                    self.email,
                    self.password,
                    self.login_button,
                    self.error_message
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            expand = True,
            margin = ft.margin.symmetric(horizontal = 20),
            alignment= ft.alignment.center_right,
            # bgcolor= ft.Colors.BLACK,
        )
        

        self.MainView = ft.Container(
            content=ft.Row(
                controls=[
                    self.Form1,
                    self.image_container,
                ],
                alignment= ft.MainAxisAlignment.START
            ),
            margin = 60,
            width = 1_265,
            alignment = ft.alignment.center,
            border_radius = 10,
            bgcolor = "#F5F5F5",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=12.1,
                color=ft.Colors.with_opacity(0.25, ft.Colors.BLACK),
                offset=ft.Offset(15, 20),
                blur_style=ft.ShadowBlurStyle.NORMAL,
            )
            # expand = True,
        )
        

        self.controls = [
            ft.Container(
                content = ft.Row(
                    controls=[
                        self.MainView
                    ],
                    alignment= ft.MainAxisAlignment.CENTER
                ),
                expand = True,
                gradient = ft.LinearGradient(
                    colors = ['#F06449', '#FFAA0C'], 
                    begin = ft.alignment.top_right, 
                    end = ft.alignment.bottom_left
                ),
            )
        ]

    def on_hover_login(self, e: ft.ControlEvent):
        text_control = e.control.content

        if isinstance(text_control, ft.Text):
            if e.data == "true":
                text_control.color = ft.Colors.WHITE
                e.control.border = ft.border.all(width=0.5, color="#F95B3C")
                e.control.gradient = ft.LinearGradient(
                    colors=["#EB2600", "#F95B3C"],
                    stops=[0.0, 0.75],
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                )
                e.control.bgcolor = None
            else:
                text_control.color = "#000000"
                e.control.border = ft.border.all(width=0.5, color="#AAAAAA")
                e.control.gradient = None
                e.control.bgcolor = ft.Colors.WHITE
            text_control.update() 
            e.control.update()

    def on_click_login(self, e: ft.ControlEvent): #TODO connect to login backend
        pass
    
    def error(self, message: str):
        self.error_message.value = message

def main(page: ft.Page):
    page.fonts = {
        "Inria Serif": path.join(path.dirname(__file__), "static", "InriaSerif-Regular.ttf"),
    }
    page.title = "Login"

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if e.route == "/":
            page.views.append(AdopterSignUp())
        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == "__main__":
    ft.app(main)