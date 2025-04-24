import flet as ft

def on_click_accept(e):
        print("Accepted application")

def main(page: ft.Page):
    page.title = "Pet application"
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = ft.Colors.BLACK
    page.window_resizable = True

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
                        padding=20,
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

                # Apply button
                ft.Container(
                    alignment=ft.alignment.bottom_center,  
                    padding=ft.Padding(left=325, top=0, right=0, bottom=150),  
                    content=ft.ElevatedButton(
                        content=ft.Text("APPLY", size=15, weight=ft.FontWeight.BOLD),
                        bgcolor="#F06449",
                        color=ft.Colors.WHITE,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            side=ft.BorderSide(1, "#F06449"),
                        ),
                        width=215,
                        height=45,
                        on_click=on_click_accept,  
                    )
                )

                
            ]
        )
    )

    page.add(background)

if __name__ == "__main__":
    ft.app(target=main)
