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

class ShelterSignUp(ft.View):
    def __init__(self, titletext: str = "Sign Up"):
        super().__init__("/")

        self.error_message_color = ft.Colors.RED
        self.error_border_color = ft.Colors.RED

        #Content
        self.image = ft.Image(
            src = path.join(path.dirname(__file__), "static", "cat1.jpg"),
            height=1000,
            width=805,
            fit=ft.ImageFit.COVER
        )
        self.image_container = ft.Container(
            content = self.image,
            padding = 0,
            width = 805,
            border_radius = ft.BorderRadius(10, 0, 10, 0),
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
                colors=["#EB2600", "#F95B3C"],
                stops = [0.0, 0.65,],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
            ),
            blend_mode=ft.BlendMode.SRC_IN,
        )
        self.shelter_name = RegisterTextBox("Shelter Name") # TODO add hint texts 
        self.email = RegisterTextBox("Email")
        self.password = RegisterTextBox("Password", password = True)
        self.confirm_password = RegisterTextBox("Confirm Password", password = True)

        self.house = RegisterTextBox(
            label = "Line 1",
            hint_text="House No./ Block/ Lane"
        )
        self.street = RegisterTextBox(
            label="Line 2", 
            hint_text="Street / Landmark"
        )
        self.area = RegisterTextBox(
            label = "Line 3",
            hint_text = "Area"
        )
        self.city = RegisterTextBox("City")
        self.city.width = 200
        self.pincode = RegisterTextBox("Pincode", "123456")
        self.pincode.width = 200
        self.phone = RegisterTextBox("Phone", "9876543210")
        self.phone.prefix_text = "+91 "
        self.next_button =  ft.Container(
            content =
                ft.Text(
                    value = r"Next →",
                    font_family="Inter",
                    size = 18,
                    color = "#202020",
                    # bgcolor = ft.Colors.BLACK
                ),
            alignment = ft.alignment.center_right,
            on_hover = ShelterSignUp.on_hover_next,
            on_click = self.on_click_next,
            # border=ft.Border(bottom=ft.BorderSide(1, color= "#202020"))
            # bgcolor = ft.Colors.GREY
        )
        self.back_button = ft.Container(
            content =
                ft.Text(
                    value = r"← Back",
                    font_family="Inter",
                    size = 18,
                    color = "#202020",
                    # bgcolor = ft.Colors.BLACK
                ),
            alignment = ft.alignment.center_left,
            on_hover = ShelterSignUp.on_hover_next,
            on_click = self.on_click_back,
            # border=ft.Border(bottom=ft.BorderSide(1, color= "#202020"))
            # bgcolor = ft.Colors.GREY
        )
        
        self.register_button = ft.Container(
            content = ft.Text("Register", size=16, color="#000000"),
            width = 150,
            height = 35,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,  # No solid background
            border=ft.border.all(width = 0.5, color = "#AAAAAA"),
            border_radius=5,  # Makes it rounded
            on_click=self.on_click_register,
            on_hover=self.on_hover_register,
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
                    self.shelter_name,
                    self.email,
                    self.password,
                    self.confirm_password,
                    self.next_button,
                    self.error_message
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            expand = True,
            margin = ft.margin.symmetric(horizontal = 20),
            alignment= ft.alignment.center,
            # bgcolor= ft.Colors.BLACK,
        )
        self.Form2 = ft.Container( # add register button
            content = ft.Column(
                controls= [
                    self.TitleText,
                    self.house,
                    self.street,
                    self.area,
                    ft.Row( 
                        controls = [
                            self.city,
                            self.pincode,
                        ],
                    ),
                    self.phone, # TODO add register button
                    ft.Row(
                        controls=[
                            self.back_button,
                            self.register_button
                        ],
                        alignment= ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    self.error_message,
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            expand = True,
            margin = ft.margin.symmetric(horizontal = 20),
            alignment= ft.alignment.center,
            animate_offset= ft.Animation(100)
            # bgcolor= ft.Colors.BLACK,
        )

        self.MainView = ft.Container(
            content=ft.Row(
                controls=[
                    self.image_container,
                    self.Form1
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

    def on_click_next(self, e: ft.ControlEvent):
        self.switch_form()

    def on_click_back(self, e: ft.ControlEvent):
        self.switch_form()

    def switch_form(self):
        self.MainView.content.controls[1] = self.Form2 if self.MainView.content.controls[1] == self.Form1 else self.Form1
        self.MainView.update()
    
    def on_hover_next(e: ft.ControlEvent):
        text_control = e.control.content
        if isinstance(text_control, ft.Text):
            text_control.color = "#EB2600" if e.data == "true" else "#202020"
            text_control.update()
    
    def on_hover_register(self, e: ft.ControlEvent):
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

    def on_click_register(self, e: ft.ControlEvent): #TODO implement form validation and re-route to login
        pass
    
    def error(self, message: str):
        self.error_message.value = message

def main(page: ft.Page):
    page.title = "Paws and Claws"

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if e.route == "/":
            page.views.append(ShelterSignUp())
        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == "__main__":
    ft.app(main)