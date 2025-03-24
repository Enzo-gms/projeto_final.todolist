import flet as ft
from view.interface import carregar_interface

def main(page: ft.Page):
    carregar_interface(page)

ft.app(target=main)