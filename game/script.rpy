# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Delphina", color="#364f98")
define f = Character("Fox", color="d25e5e")
define m = Character("Martinho", color="cc9900")
define md = Character("Maria Degolada", color="660096")
#define moi

define cenaCrimeAtual = 1

define pistasDelphina = [0,0,0]
define pistasFox = [0,0,0]

image Delphina:
    im.FactorScale("delphina_neutro.png", 0.7)
    xanchor 0.6
    yanchor -0.3

image Delphina flip:
    im.Flip(im.FactorScale("delphina_neutro.png", 0.7), horizontal=True)
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

image MariaDegolada:
    im.FactorScale("mariadegolada_neutro.png", 0.7)
    xalign 0.5
    yalign 0.5
    # xanchor 0.6
    # yanchor -0.3
    # xpos 0.8
    # ypos 0.3

# The game starts here.

label start:

    play music "/audio/dark.mp3" volume 0.8

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg crime
 
    show Martinho at right

    m "Uma pena, uma moça tão jovem…"  
    show Delphina at left with dissolve
    m "Ei! O que está fazendo aqui, nem te chamei ainda!"

menu:    
    "Senti que tinha algo errado, por isso me adiantei. Como vai, detetive Martinho?":
        jump resposta

    "Os mortos do além túmulo me mandaram aqui pra te ver Martinho! Buuuuuu!":
        jump resposta

    "Vi as Luzes da esquina e pensei em dar um oi… Oi, Martinho!":
        jump resposta 

label resposta:
    m "Você sempre me assusta, Delphina! Credo!"
    jump continuarFox

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
    show Fox at left
    f "Essa faca é de uma coleção muito exclusiva que a vítima postou online! No post ela fala que faria um picnic hoje mais cedo… Que maneira de terminar o dia. Infelizmente ela está sozinha na foto, mas alguns comentários são promissores."

    $ pistasFox[0] = 1
    jump continuarFox
    
label camera:
    show Fox at left
    f "A roupa que a vítima está corresponde às fotos do post de hoje, mas está faltando uma corrente de coração, provável que o assassino tenha levado…"
    
    show MariaDegolada at right 
    md "Meu colar… Era um presente…"

    hide Fox
    show Delphina at left
    d "Você lembra de quem você ganhou?"
    md "De alguém muito próximo…"

    hide Delphina
    hide MariaDegolada
    show Fox at left
    f "Falando sozinha de novo, Delphina?"
    show Delphina flip at right
    d "Tem como você procurar nesse seu telefone de quem ela ganhou esse colar?"
    f "Claro, fofura, ela ganhou do namorado dela, parece que temos nosso primeiro suspeito… Pera, como você sabe que ela ganhou o colar?"
    d "Quando falo sozinha descubro muita coisa."

    $ pistasFox[1] = 1
    jump continuarFox  

label quem:
    show Fox at left
    f "Segundo meu sistema de reconhecimento facial, ela é Maria Teles da Conceição, 23 anos e era muito ativa nas redes sociais. Isso é bom e ruim ao mesmo tempo, vou precisar de um computador para achar alguns suspeitos."
    hide Fox
    show Delphina flip at right
    d "Sua maquininha não faz tudo?"
    show Fox at left
    hide Delphina
    f "O 3g aqui não é tão bom assim…"
    hide Fox
    show Delphina flip at right
    d "3g?"
    show Fox at left
    hide Delphina
    f "Deixa pra lá..."

    $ pistasFox[2] = 1
    jump continuarFox      

#itens Delphina
label arvore:
    show Delphina at left
    d "Essa árvore é a mesma que aconteceu um assassinato em 1862, muitos acreditam que o espírito da vítima ainda quer vingança. Será que o assassino escolheu esse lugar por acaso?"  
    $ pistasDelphina[0] = 1
    jump continuarDelphina

label espirito:
    show Delphina at left
    d "Olá querida, sinto muito pelo que aconteceu contigo." 
    hide Delphina
    show MariaDegolada at right
    md "O que aconteceu comigo… Estou com frio…"
    hide MariaDegolada
    show Delphina at left
    d "Infelizmente, querida, sua vida foi tirada de você… "
menu:    
    "Você lembra quem fez isso com você?":
        show MariaDegolada at right
        "Maria Degolada" "Sinto que eu o conhecia… Mas tudo parece tão vago..."
        jump finalArvore
    "Você lembra como veio aqui?":
        show MariaDegolada at right
        "Maria Degolada" "Alguém me chamou aqui, parecia ser um pedido de desculpas..."
        jump finalArvore

label finalArvore:
    hide MariaDegolada
    show Delphina at left
    d "Não se preocupe, vamos achar quem fez isso contigo. Ande comigo, talvez se lembre de algo no caminho."        
    $ pistasDelphina[1] = 1 
    jump continuarDelphina

label energia:
    show Delphina at left
    d "Consigo sentir a energia do assassino, ele estava muito enfurecido, com muito ciúmes. Foi algo passional, mas planejado. Era algo tão fixo em sua mente que ficou impregnado em seus passos. Infelizmente a energia se dissipa ao sair da cena do crime."  
    $ pistasDelphina[2] = 1 
    jump continuarDelphina

label fim:
    "Fim!"     

    # This ends the game.

return
