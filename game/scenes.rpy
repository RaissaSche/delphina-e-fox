screen crimeFox:
    imagebutton:
        auto "/imagebuttons/arma %s.png"
        focus_mask True
        action Jump("arma")

    imagebutton:
        xanchor 0.5
        yanchor 0.4
        xpos 0.07
        ypos 0.3
        idle "delphina_pb"
        action [Show("crimeDelphina"), Hide("crimeFox"), Hide("fox_neutro.png")]

    add "fox_neutro.png" at Position(xpos = 0.2, xanchor=0.5, ypos=0.7, yanchor=0.4)
    


screen crimeDelphina:
    imagebutton:
        auto "/imagebuttons/arvore %s.png"
        focus_mask True
        action Jump("arvore")

    imagebutton:
        xanchor 0.5
        yanchor 0.4
        xpos 0.08
        ypos 0.5
        idle "fox_pb"
        action [Show("crimeFox"), Hide("crimeDelphina"), Hide("delphina_neutro.png")]
    add "delphina_neutro.png" at Position(xpos = 0.2, xanchor=0.5, ypos=0.6, yanchor=0.4)  