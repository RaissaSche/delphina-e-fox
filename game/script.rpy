# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Delphina", color="#212121")
define f = Character("Fox")
define m = Character("Martinho")
define md = Character("Maria Degolada")

define cenaCrimeAtual = 1

image Delphina:
    im.FactorScale("delphina_neutro.png", 0.7)
    xanchor 0.6
    yanchor -0.3
   
image Fox:
    im.FactorScale("fox_neutro.png", 0.7)
    xanchor 0.6
    yanchor -0.3

image Martinho:
    im.Flip(im.FactorScale("martinho_neutro.png", 0.7), horizontal=True)
    xanchor 0.6
    yanchor -0.3   


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg crime
 
#     show Martinho at right

#     m "Uma pena, uma moça tão jovem…"  
#     show Delphina at left with dissolve
#     m "Ei! O que está fazendo aqui, nem te chamei ainda!"

# menu:    
#     "Senti que tinha algo errado, por isso me adiantei. Como vai, detetive Martinho?":
#         jump resposta

#     "Os mortos do além túmulo me mandaram aqui pra te ver Martinho! Buuuuuu!":
#         jump resposta

#     "Vi as Luzes da esquina e pensei em dar um oi… Oi, Martinho!":
#         jump resposta 

# label resposta:
#     m "Você sempre me assusta, Delphina! Credo!"
#     jump continuar

label continuarFox:
    scene bg crime

    hide Martinho
    hide Delphina
    hide textbox

    call screen crimeFox

label continuarDelphina:
    scene bg crime
    
    hide Martinho
    hide Delphina
    hide textbox

    call screen crimeDelphina

# if cenaCrimeAtual == 1:
#     call screen crimeFox
# elif cenaCrimeAtual == 2:
#     call screen crimeDelphina    

#itens Fox
label arma:
    "Cliquei na arma"
    jump continuarFox
    
label camera:
    "Cliquei na camera"
    jump continuarFox  

label quem:
    "Cliquei em quem"
    jump continuarFox      

#itens Delphina
label arvore:
    "Cliquei na arvore"   
    jump continuarDelphina

label espirito:
    "Cliquei no espirito"   
    jump continuarDelphina

label energia:
    "Cliquei na energia"   
    jump continuarDelphina

label fim:
    "Fim!"     

    # This ends the game.

return
