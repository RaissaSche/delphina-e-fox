# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Delphina")

image Delphina:
    "delphina"
    xanchor 0.6
    yanchor -0.3

transform leftPos1:
    xpos 0.1

transform leftPos2:
    xpos 0.2

   
image Fox:
    "fox"
    xanchor 0.6
    yanchor -0.3

transform leftPos1:
    xpos 0.1

transform leftPos2:
    xpos 0.2


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
   
    show Delphina at leftPos1
    "blah"

    show Fox at leftPos2
    "blah"

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
