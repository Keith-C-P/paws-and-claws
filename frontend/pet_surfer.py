from os import path
from math import pi
import flet as ft

class PetCard(ft.Container):
    def __init__(self, name: str= "Bartholomeow", 
        age: str = "69", 
        breed: str= "British Shorthair", 
        sex: str = "Female", 
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
                            ft.Container(height = 5),
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
    def __init__(self):
        super().__init__("/")
        
        self.cards = ft.Container( 
            content = ft.Row(
                controls=[
                    PetCard() for _ in range(6)
                ],
                wrap = True,
                spacing = 10,
                run_spacing = 10,
                width = 1080,
            ),
            alignment = ft.alignment.top_center,
            expand = True
        )

        self.MainView = ft.Container( 
            content = ft.Container(
                content = ft.Column(
                    controls= [
                        self.cards
                    ],
                ),
                bgcolor = ft.Colors.WHITE,
                border_radius = 20,
                margin = 75,
                width = 1295,
                expand = True,
                clip_behavior= ft.ClipBehavior.HARD_EDGE
            ),
            alignment= ft.alignment.center,
            expand= True,
        )
        
        self.controls = [
            ft.Container(
                content = ft.Stack(
                    controls = [
                        ft.Container(
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
                        ),
                        ft.Container(
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
                        ),
                        self.MainView
                    ],
                    expand=True
                ),
                expand = True,
                gradient = ft.LinearGradient(
                    colors = ['#F06449', '#EB2600'], 
                    begin = ft.alignment.top_right, 
                    end = ft.alignment.bottom_left
                ),
            ),
        ]

def main(page: ft.Page):
    page.title = "Paws and Claws"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if e.route == "/":
            page.views.append(PetSurfer())
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