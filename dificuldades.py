from PPlay.window import * 
from PPlay.gameimage import * 

from jogo import tela

def escolha(dificuldades):
    #Para o uso desse código, é necessário que em sua pasta você contenha os seguintes arquivos: 

    #   media.png           facil_verde.png
    #   facil.png           media_verde.png
    #   dificil.png         dificil_verde.png

    #mal implementação, era mais simples só pedir a tela, fazendo isso você cria uma variável de função que pode desencadear diversos erros
    """#Cria a janela do menu
    dificuldades = Window(1040, 500)

    #Dá um título ao menu
    dificuldades.set_title("Dificuldades")"""


    #Recebe o mouse
    mouse = Window.get_mouse()

    #Recebe o teclado
    teclado = Window.get_keyboard()

    #Gera o botão "MÉDIO"
    media_Colorido = False

    media = GameImage("media.png")
    media.set_position(dificuldades.width/2-media.width/2, dificuldades.height/2-media.height/2)

    #Gera o botão "FÁCIL"
    facil_Colorido = False

    facil = GameImage("facil.png")
    facil.set_position(dificuldades.width/2-facil.width/2, dificuldades.height/2-(media.height/2)-65)

    #Gera o botão "DIFÍCIL"
    dificil_Colorido = False

    dificil = GameImage("dificil.png")
    dificil.set_position(dificuldades.width/2-dificil.width/2, dificuldades.height/2-(media.height/2)+65)

    delay = 0

    #Gameloop
    while True:

                #Volta ao menu
        if(teclado.key_pressed("ESC")):  
            break

        #Controla o botão "FÁCIL"
        if mouse.is_over_object(facil):
            facil = GameImage("facil_verde.png")
            facil.set_position(dificuldades.width/2-facil.width/2, dificuldades.height/2-(media.height/2)-65)

            facil_Colorido = True

            if(mouse.is_button_pressed(1)) and delay>=500:
                tela(1, dificuldades)
                return False

        elif facil_Colorido:
            facil = GameImage("facil.png")
            facil.set_position(dificuldades.width/2-facil.width/2, dificuldades.height/2-(media.height/2)-65)

##############################################################################################################################

        #Controla o botão "MÉDIO"
        if mouse.is_over_object(media):
            media = GameImage("media_verde.png")
            media.set_position(dificuldades.width/2-media.width/2, dificuldades.height/2-media.height/2)

            media_Colorido = True

            if(mouse.is_button_pressed(1)) and delay>=500:
                tela(1.5, dificuldades)
                return False

        elif media_Colorido:
            media = GameImage("media.png")
            media.set_position(dificuldades.width/2-media.width/2, dificuldades.height/2-media.height/2)

##############################################################################################################################

        #Controla o botão "DIFÍCIL"
        if mouse.is_over_object(dificil):
            dificil = GameImage("dificil_verde.png")
            dificil.set_position(dificuldades.width/2-dificil.width/2, dificuldades.height/2-(media.height/2)+65)

            dificil_Colorido = True

            if(mouse.is_button_pressed(1)) and delay>= 500:
                tela(2, dificuldades)
                return False

        elif dificil_Colorido:
            dificil = GameImage("dificil.png")
            dificil.set_position(dificuldades.width/2-dificil.width/2, dificuldades.height/2-(media.height/2)+65)

##############################################################################################################################
	
        dificuldades.set_background_color((0,0,0))
        media.draw()
        facil.draw()
        dificil.draw()
        dificuldades.update()

        delay += 1
