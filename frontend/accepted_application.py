import flet as ft

def main(page: ft.Page):
    page.title = "Pet application"
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = ft.Colors.BLACK
    page.window_resizable = True

    page.fonts = {
        "InriaSerif": "static/InriaSerif-Regular.ttf"
    }

    background = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            colors=["#FFAA0C", "#F06449"],
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            tile_mode=ft.GradientTileMode.CLAMP
        ),
        content=ft.Stack(
            expand=True,
            controls=[
                # Paw image
                ft.Container(
                    padding=ft.Padding(left=-5, top=0, right=0, bottom=-0),
                    content=ft.Image(
                        src="static/paw_background.png",
                        width=300,
                        height=300,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.bottom_left,
                ),

                # White container with text content
                ft.Container(
                    padding=ft.Padding(left=60, top=40, right=60, bottom=40),
                    content=ft.Container(
                        expand=True,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=15,
                        padding=40,
                    )
                ),

                # Title Background
                ft.Container(
                    padding=ft.Padding(left=0, top=-65, right=0, bottom=0),
                    content=ft.Image(
                        src="static/title_background.png",
                        width=1500,
                        height=200,
                        expand=True,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.top_center,
                ),

                # Logo Image
                ft.Container(
                    padding=ft.Padding(left=100, top=-65, right=0, bottom=0),
                    content=ft.Image(
                        src="static/logo_paw.png",
                        width=300,
                        height=300,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.top_left,
                ),

                # correct image
                ft.Container(
                    padding=ft.Padding(left=0, top=0, right=0, bottom=50),
                    content=ft.Image(
                        src="static/check_image.png",
                        width=375,
                        height=375,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                ),

                # Text 
                ft.Container(
                    padding=ft.Padding(left=480, top=600, right=0, bottom=0),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text(
                                value="We have received your application",
                                size=36,
                                weight=ft.FontWeight.W_500,
                                color="black",
                                font_family="InriaSerif"
                            ),
                            ft.Text(
                                value=":D",
                                size=28,
                                weight=ft.FontWeight.W_600,
                                color="#F06449",
                                font_family="InriaSerif"
                            )
                        ]
                    )
                )
            ]
        )
    )

    page.add(background)

if __name__ == "__main__":
    ft.app(target=main)
