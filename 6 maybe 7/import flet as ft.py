import flet as ft 
def main(page: ft.Page):
    crusty = ft.Image(src="images/crusty.png",width=100, height= 100)

    page.add(crusty)
ft.run(main=main, assets_dir= "assets")