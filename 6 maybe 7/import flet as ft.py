import flet as ft 
def main(page: ft.Page):

#function
    def inviceible_pep(e):
        if pep_switch.value == False:
            pep.opacity = 0.0
        else:
            pep.opacity = 1.0
    
    def inviceible_baky(e):
        if baky_switch.value == False:
            bacon.opacity = 0.0
        else:
            bacon.opacity = 1.0

    def inviceible_bbq(e):
        if bbq_switch.value == False:
            bbq.opacity = 0.0
        else:
            bbq.opacity = 1.0
    




#switches
    baky_switch = ft.Switch(label = "baky", value = True, on_change = inviceible_baky)
    pep_switch = ft.Switch(label = "pep", value = True ,on_change = inviceible_pep)
    bbq_switch = ft.Switch(label = "bbq", value = True, on_change = inviceible_bbq)


#the stack
    crusty = ft.Image(src = "images/crusty.png")
    pep = ft.Image(src = "images/pep.png")
    bacon = ft.Image(src = "images/baky.png")
    bbq = ft.Image(src = "images/bbq.png")


    
    
    the_pizz = ft.Stack(controls = [
        crusty,
        bacon,
        bbq,
        pep],
        width=300, height =300)


    page.add(the_pizz,pep_switch, baky_switch,bbq_switch)
ft.run(main=main, assets_dir= "assets")