from os import path
from math import pi
import flet as ft
from database import get_all_pets_details

class ProfileDropdown(ft.Container):
    def __init__(self, top = 0, left = 0, bottom = None, right = None):
        super().__init__()
        self.applications_button = ft.Container(
            content= ft.Text(
                value = "Applications",
                color = "#F06449",
                font_family = "Inter",
                size = 25
            ),
            bgcolor = ft.Colors.WHITE,
            border_radius = 10,
            alignment = ft.alignment.center,
            width = 210,
            height = 55,
            shadow = ft.BoxShadow(
                spread_radius = 0, 
                blur_radius = 4, 
                color = ft.Colors.with_opacity(0.5, ft.Colors.BLACK), 
                offset = (4,4)
            ),
        )

        self.settings_button = ft.Container(
            content= ft.Text(
                value = "Settings",
                color = "#F06449",
                font_family = "Inter",
                size = 25
            ),
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            alignment= ft.alignment.center,
            width=210,
            height=55,
            shadow= ft.BoxShadow(
                spread_radius=0, 
                blur_radius=4, 
                color=ft.Colors.with_opacity(0.5, ft.Colors.BLACK), 
                offset=(4,4)
            ),
        )

        self.logout_button = ft.Container(
            content= ft.Text(
                value = "LOG OUT",
                color = ft.Colors.WHITE,
                font_family = "Inter",
                size = 25
            ),
            bgcolor="#F06449",
            border_radius=10,
            alignment= ft.alignment.center,
            width=210,
            height=65,
            shadow= ft.BoxShadow(
                spread_radius=0, 
                blur_radius=4, 
                color=ft.Colors.with_opacity(0.5, ft.Colors.BLACK), 
                offset=(4,4)
            ),
        )

        self.gradient = ft.LinearGradient(
            colors = [ft.Colors.with_opacity(1, '#FF674A'), ft.Colors.with_opacity(1, '#8A3A2A')],
            begin = ft.alignment.top_center,
            end = ft.alignment.bottom_center,
        )
        self.border_radius = 20
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        self.padding = 10
        self.height = 735
        self.width = 250
        self.alignment = ft.alignment.center

        self.content = ft.Column(
            controls=[
                self.applications_button,
                self.settings_button,
                self.logout_button,
            ],
        )

class PetCard(ft.Container):
    def __init__(self, name: str= "Bartholomeow", 
        age: str = "69", 
        sex: str = "Female", 
        breed: str= "British Shorthair", 
        address: str= "Skibidi Pet Center, 1234 Sigma Street, Al Nahdha", 
        thumbnail_name: str= "placeholder.jpg"
        ):

        super().__init__()
        self.height = 425
        self.width = 345
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=4,
            color=ft.Colors.with_opacity(0.25, ft.Colors.BLACK),
            offset=ft.Offset(5, 5),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        )
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 20 

        self.thumbnail = ft.Image(
            src = path.join(path.dirname(__file__), "static", thumbnail_name),
            height = 250,
            width = self.width,
            fit = ft.ImageFit.COVER
        )
        self.thumbnail_container = ft.Container(
            content=self.thumbnail,
            padding= 0,
            height= 250,
            width = self.width,
            border_radius = ft.BorderRadius(20, 20, 0, 0),
            bgcolor=ft.Colors.BLACK
        )
        self.name = ft.Text(
            value = name,
            font_family="Inria Serif",
            size = 35,
            color = ft.Colors.BLACK,
        )
        self.sex = ft.Icon(
            name = ft.Icons.MALE_SHARP if sex == "male" else ft.Icons.FEMALE_SHARP, 
            color = "#446CFF" if sex == "male" else "#FF6DA0", 
            size = 40
        ) 
        self.age = ft.Text(
            value = age + " years",
            font_family="Inter",
            size = 18,
            color = "#525252"
        )
        self.breed = ft.Text(
            value = breed,
            font_family="Inria Serif",
            size = 18,
            color = ft.Colors.BLACK
        )
        self.address = ft.Text( # TODO add text wrap
            value = address,
            font_family="Inria Serif",
            size = 15,
            color = ft.Colors.BLACK,
            width = self.width - 50,
            max_lines=2,
            overflow= ft.TextOverflow.ELLIPSIS
        )

        self.content = ft.Column(
            controls=[
                self.thumbnail_container,
                ft.Container(
                    content = ft.Column(
                        controls =[ 
                            ft.Row(
                                controls = [    
                                    self.name,
                                    self.sex
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            self.age,
                            self.breed,
                            ft.Container(height = 5), #spacing / filler
                            ft.Row(
                                controls = [
                                    ft.Icon(name = ft.Icons.LOCATION_PIN, color = "#C2213A"),
                                    self.address,
                                ],
                                spacing = 10,
                                alignment = ft.MainAxisAlignment.START,
                            )
                        ],
                        spacing = 0,
                    ),
                    padding = 8,
                )
            ],
            alignment=ft.MainAxisAlignment.START
        )

class PetSurfer(ft.View):
    def __init__(
            self, 
            page: ft.Page,
        ):
        super().__init__("/pet-surfer")        
        self.profile = ft.Container(
            content= ft.Container(
                content=ft.Icon(name = ft.Icons.PERSON, color="#FC935E", size = 70),
                bgcolor="#FFFFFF",
                border_radius=12,
                # height= 68.6
                expand= True
            ),
            bgcolor="#F06449",
            border_radius = 15,
            padding = 5,
            width = 77.5,
            height= 74,
            
            on_click= self.profile_dropdown
        )

        self.logo_img = ft.Image(
            src=path.join(path.dirname(__file__), "static", "logo_paw.png"), 
            fit=ft.ImageFit.COVER, 
            width=375, 
            height=101, 
            expand=True
        )

        self.logo = ft.Container(content=self.logo_img)

        self.TopBar = ft.Container(
            content = ft.Row(
                controls=[
                    self.logo,
                    self.profile
                ],
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                height = 105,
            ),
            gradient = ft.LinearGradient(
                colors = ['#F4D8D3', '#E4EAE9'],
                stops = [0.5,1.5],
                begin = ft.alignment.top_right,
                end = ft.alignment.bottom_left
            ),
            padding = 20
        )

        self.cards = ft.Container( 
            content = ft.Row(
                controls=[
                ],
                wrap = True,
                spacing = 10,
                run_spacing = 10,
                width = 1080,
                scroll=ft.ScrollMode.HIDDEN,
            ),
            alignment = ft.alignment.top_center,
            expand = True
        )

        self.MainView = ft.Container( 
            content = ft.Container(
                content = ft.Column(
                    controls= [
                        self.TopBar,
                        self.cards
                    ],
                ),
                bgcolor = ft.Colors.WHITE,
                border_radius = 20,
                margin = 50,
                width = 1700,
                expand = True,
                clip_behavior= ft.ClipBehavior.HARD_EDGE
            ),
            alignment= ft.alignment.center,
            expand= True,
        )

        paw1 = ft.Container(
            content = ft.Image(
                src = path.join(path.dirname(__file__), "static", "paw.svg"),
                height = 340,
                width = 340,
                color= "#420000",
                anti_alias = True,
                rotate = 26 * (pi/ 180),
                fit = ft.ImageFit.SCALE_DOWN,
            ),
            bottom = -40,
            left = -40,
        )

        paw2 = ft.Container(
            content = ft.Image(
                src = path.join(path.dirname(__file__), "static", "paw.svg"),
                height = 340,
                width = 340,
                color= "#BA5444",
                anti_alias = True,
                rotate = -150 * (pi/ 180),
                fit = ft.ImageFit.SCALE_DOWN,
            ),
            top = -55,
            right = -40,
        )

        self.stack: ft.Stack = ft.Stack(
            controls = [
                paw1,
                paw2,
                self.MainView
            ],
            expand=True
        )
        
        self.controls = [
            ft.Container(
                content = self.stack,
                expand = True,
                gradient = ft.LinearGradient(
                    colors = ['#F06449', '#EB2600'], 
                    begin = ft.alignment.top_right, 
                    end = ft.alignment.bottom_left
                ),
            ),
        ]
    
    def profile_dropdown(self, e: ft.ControlEvent):
        dropdown = next((c for c in self.stack.controls if isinstance(c, ProfileDropdown)), None)
        if dropdown in self.stack:
            self.stack.controls.remove(dropdown)
        else:
            self.stack.controls.append(ProfileDropdown(left=1470, top=184))
        self.update()
    
    def did_mount(self):
        self.load_pet_cards()
    
    def load_pet_cards(self):
        self.pet_details = get_all_pets_details()
        self.cards.content.controls = [
            PetCard(*detail) for detail in self.pet_details
        ]
        self.update()

def main(page: ft.Page):
    page.title = "Paws and Claws"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if e.route == "/":
            page.views.append(PetSurfer(page))
        page.update()

    page.on_route_change = route_change
    page.go("/")

# def main1(page: ft.Page):
#     page.title = "Card Trial"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     page.add(
#         PetCard()
#     )

if __name__ == "__main__":
    ft.app(main)