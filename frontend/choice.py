import flet as ft
from os import path
from math import pi

class BackgroundOnly(ft.View):
    def __init__(self):
        super().__init__("/")

        # Set up static asset paths
        base_path = path.dirname(__file__)
        left_image_path = path.join(base_path, "static", "left_background.png")
        paw_image_path = path.join(base_path, "static", "paw1.png")
        paw_svg_path = path.join(base_path, "static", "paw.svg")
        paw_image2_path = path.join(base_path, "static", "paw2.png")

        # --- LEFT (Business) Panel ---
        left_image = ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Image(src=left_image_path, fit=ft.ImageFit.COVER, width=float("inf"), height=float("inf"), expand=True),
                    ft.Image(src=paw_image2_path, width=185, height=185, right=80, top=105),
                    ft.Container(content=self.create_business_ui(), alignment=ft.alignment.top_center, padding=ft.padding.only(top=170)),
                ]
            ),
            expand=1,
            border_radius=ft.BorderRadius(top_left=50, top_right=0, bottom_left=50, bottom_right=0),  
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
        )

        # --- RIGHT (Adopters) Panel ---
        right_content = ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Image(src=paw_image_path, width=200, height=200, left=65, top=375),
                    self.create_login_ui(),
                ]
            ),
            expand=1,
        )

        # --- Centered White Panel Holding Both Sides ---
        white_rounded_container = ft.Container(
            content=ft.Row(controls=[left_image, right_content], expand=True, spacing=0),
            bgcolor=ft.Colors.WHITE,
            border_radius=50,
            padding=0,
            margin=55,
            expand=True,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
        )

        # --- Full Page Stack ---
        self.controls = [
            ft.Container(
                content=ft.Stack(
                    controls=[
                        self.create_background_gradient(),
                        self.create_paw_image(paw_svg_path, bottom=-40, left=-40, rotate=26),
                        self.create_paw_image(paw_svg_path, top=-55, right=-40, rotate=-150),
                        white_rounded_container,
                    ],
                    expand=True,
                ),
                expand=True,
            )
        ]

    # --- Background Gradient ---
    def create_background_gradient(self):
        return ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                colors=["#F06449", "#FFAA0C"],
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_left,
            ),
        )

    # --- Rotated Paw Decorations ---
    def create_paw_image(self, path, **kwargs):
        return ft.Container(
            content=ft.Image(
                src=path,
                height=275,
                width=340,
                color="#420000",
                anti_alias=True,
                rotate=kwargs.get("rotate", 0) * (pi / 180),
                fit=ft.ImageFit.SCALE_DOWN,
            ),
            **kwargs,
        )

    # --- Adopters Panel ---
    def create_login_ui(self):
        return ft.Column(
            controls=[
                ft.Container(content=self.create_personal_badge(), alignment=ft.alignment.top_center, padding=ft.padding.only(top=235)),
                self.create_title_row("For", "Adopters"),
                self.create_login_button("Login", self.on_click_login),
                self.create_signup_redirect_text(),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=10,
        )

    def create_personal_badge(self):
        return ft.Container(
            content=ft.Text("PERSONAL", size=15, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
            bgcolor="#F06449",
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=6, vertical=2),
            alignment=ft.alignment.center,
            width=135,
            margin=ft.padding.symmetric(horizontal=20, vertical=10),
        )

    def create_signup_redirect_text(self):
        self.signup_text = ft.Text("Sign Up", size=14, color="#000000", weight=ft.FontWeight.BOLD)
        return ft.Column(
            controls=[
                ft.Text("Don't have an account?", size=14, color="#202020", text_align=ft.TextAlign.CENTER),
                ft.Container(
                    content=self.signup_text,
                    on_click=self.on_click_signup_redirect,
                    on_hover=self.on_hover_signup_text,
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def on_click_signup_redirect(self, e):
        print("Redirect to sign up...")

    def on_hover_signup_text(self, e: ft.ControlEvent):
        self.signup_text.color = "#F06449" if e.data == "true" else "#000000"
        self.signup_text.update()

    # --- Business Panel ---
    def create_business_ui(self):
        return ft.Column(
            controls=[
                ft.Container(content=self.create_business_badge(), alignment=ft.alignment.top_center, padding=ft.padding.only(top=65)),
                self.create_title_row("For", "Shelters"),
                self.create_login_button("Login", self.on_click_business_login),
                self.create_contact_text(),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

    def create_business_badge(self):
        return ft.Container(
            content=ft.Text("BUSINESS", size=15, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
            bgcolor="#F06449",
            border_radius=8,
            padding=ft.padding.symmetric(horizontal=6, vertical=2),
            alignment=ft.alignment.center,
            width=135,
            margin=ft.padding.symmetric(horizontal=20, vertical=10),
        )

    def create_contact_text(self):
        self.contact_text = ft.Text("Contact Us", size=14, color="#000000", weight=ft.FontWeight.BOLD)
        return ft.Column(
            controls=[
                ft.Text("Don't have an account?", size=14, color="#202020", text_align=ft.TextAlign.CENTER),
                ft.Container(
                    content=self.contact_text,
                    on_click=self.on_click_contact,
                    on_hover=self.on_hover_contact_text,
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def on_click_contact(self, e):
        print("Redirect to contact page...")

    def on_hover_contact_text(self, e: ft.ControlEvent):
        self.contact_text.color = "#F06449" if e.data == "true" else "#000000"
        self.contact_text.update()

    # --- Shared Components ---
    def create_title_row(self, prefix, label):
        return ft.Row(
            controls=[
                ft.Text(prefix, size=40, color="#000000"),
                ft.Text(label, size=40, color="#F06449"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def create_login_button(self, text, click_handler):
        return ft.ElevatedButton(
            content=ft.Text(text, size=15, weight=ft.FontWeight.NORMAL),
            bgcolor=ft.Colors.WHITE,
            color="#000000",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                side=ft.BorderSide(1, "#F06449"),
            ),
            width=215,
            height=45,
            on_click=click_handler,
        )

    def on_click_login(self, e):
        print("Adopter logged in!")

    def on_click_business_login(self, e):
        print("Shelter logged in!")


# --- Entry Point ---
def main(page: ft.Page):
    page.title = "Paws and Claws"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if e.route == "/":
            view = BackgroundOnly()
            view.page = page
            page.views.append(view)
        page.update()

    page.on_route_change = route_change
    page.go("/")


if __name__ == "__main__":
    ft.app(main)
