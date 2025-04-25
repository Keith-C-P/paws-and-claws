import flet as ft
from os import path
from views import view_handler

def main(page: ft.Page):
    page.title = ""
    page.fonts = {
        "Inria Serif": path.join(path.dirname(__file__), "frontend", "static", "InriaSerif-Regular.ttf"),
    }

    def route_change(route: ft.RouteChangeEvent) -> None:
        print(f"Current Route: {page.route}")
        page.views.clear()
        view = view_handler(page).get(page.route, ft.View(controls=[ft.Text("404 Not Found")]))
        page.views.append(view)
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
