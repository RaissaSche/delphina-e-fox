screen crimeFox:
    imagebutton:
        auto "/imagebuttons/arma %s.png"
        focus_mask True
        action Jump("arma")

    imagebutton:
        auto "/imagebuttons/camera %s.png"
        focus_mask True
        action Jump("camera")    

    imagebutton:
        auto "/imagebuttons/quem %s.png"
        focus_mask True
        action Jump("quem")       

    imagebutton:
        xanchor 0.5
        yanchor 0.4
        xpos 0.07
        ypos 0.3
        idle "delphina_pb"
        focus_mask True
        action [Show("crimeDelphina"), Hide("crimeFox"), Hide("fox_neutro.png")]

    vbox xalign 0.95 yalign 0.1:
        textbutton "Mapa" action [Show("delegacia")] 

    add "fox_neutro.png" at Position(xpos = 0.2, xanchor=0.5, ypos=0.7, yanchor=0.4)
    

screen crimeDelphina:
    imagebutton:
        auto "/imagebuttons/arvore %s.png"
        focus_mask True
        action Jump("arvore")

    imagebutton:
        auto "/imagebuttons/espirito %s.png"
        focus_mask True
        action Jump("espirito")  

    imagebutton:
        auto "/imagebuttons/energia %s.png"
        focus_mask True
        action Jump("energia")  

    imagebutton:
        xanchor 0.5
        yanchor 0.4
        xpos 0.08
        ypos 0.5
        idle "fox_pb"
        focus_mask True
        action [Show("crimeFox"), Hide("crimeDelphina"), Hide("delphina_neutro.png")]

    vbox xalign 0.95 yalign 0.1:
         textbutton "Mapa" action [Show("delegacia")] 

    add "delphina_neutro.png" at Position(xpos = 0.2, xanchor=0.5, ypos=0.6, yanchor=0.4)  


screen delegacia:
    add "bg delegacia.png" 

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        auto "/imagebuttons/board %s.png"
        focus_mask True
        action [Show("board"), Hide("delegacia")]

screen board: 
    add "bg board.png"
    
    vbox:
        xalign 0.5
        yalign 0.5
        text "Pistas Delphina:"
        text "[pistasDelphina]"
        text "Pistas Fox:"
        text "[pistasFox]"

    vbox xalign 0.95 yalign 0.1:
        textbutton "Mapa" action [Hide("crimeFox"), Hide("board"), Hide("/imagebuttons/board idle.png"), Hide("crimeDelphina"), Hide("bg board.png"), Jump("continuarFox"),] 

        