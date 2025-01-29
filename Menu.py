from PPlay.window import * 
from PPlay.gameimage import * 

from jogo import tela
from dificuldades import escolha

def setranking(janela):
    janela.set_title("ranking")
    lista_aux = []
    lista = []
    teclado = Window.get_keyboard()
    with open("registros.txt", "r") as registro:
        line = registro.readline()
        while line != '':
            lista.append(line.rstrip("\n"))
            line = registro.readline()
    matriz = []
    for n in range(len(lista)):
        nome, pontos = lista[n].split("&")
        lista_aux.append(nome)
        lista_aux.append(pontos)
        matriz.append(lista_aux)
        lista_aux = []
    matriz.sort(key = lambda x: (-int(x[1]), str(x[0])))

    while True:
        janela.set_background_color([0, 0, 0])
        if teclado.key_pressed("ESC"):
            return False
        for n in range(5):
            try:
                janela.draw_text(str(matriz[n][0]) + "-" + str(matriz[n][1]), janela.width/3, janela.height/9 + n*80, 50, [100, 0, 100])
            except IndexError:
                break
        janela.update()

def menu():
    #Para o uso desse código, é necessário que em sua pasta você contenha os seguintes arquivos: 

    #   jogar.png           jogar_verde.png
    #   dificuldade.png     dificuldade_verde.png
    #   ranking.png         ranking_verde.png
    #   sair.png            sair_verde.png

    #Cria a janela do menu
    menu = Window(1040, 500)

    #Dá um título ao menu
    menu.set_title("Menu")

    #Recebe o mouse
    mouse = Window.get_mouse()

    #Gera o botão "JOGAR"
    jogar_Colorido = False

    jogar = GameImage("jogar.png")
    jogar.set_position(menu.width/2-jogar.width/2, menu.height/2-(jogar.height/2)-100)

    #Gera o botão "DIFICULDADE"
    dificuldade_Colorido = False

    dificuldade = GameImage("dificuldade.png")
    dificuldade.set_position(menu.width/2-dificuldade.width/2, menu.height/2-(jogar.height/2)-45)

    #Gera o botão "RANKING"
    ranking_Colorido = False

    ranking = GameImage("ranking.png")
    ranking.set_position(menu.width/2-ranking.width/2, menu.height/2-(jogar.height/2)+10)

    #Gera o botão "SAIR"
    sair_Colorido = False

    sair = GameImage("sair.png")
    sair.set_position(menu.width/2-sair.width/2, menu.height/2-(jogar.height/2)+65)


    #Gameloop
    while True:

        #Controla o botão "JOGAR"
        if mouse.is_over_object(jogar):
            jogar = GameImage("jogar_verde.png")
            jogar.set_position(menu.width/2-jogar.width/2, menu.height/2-(jogar.height/2)-100)

            jogar_Colorido = True

            if(mouse.is_button_pressed(1)):
                tela(1, menu)

        elif jogar_Colorido:
            jogar = GameImage("jogar.png")
            jogar.set_position(menu.width/2-jogar.width/2, menu.height/2-(jogar.height/2)-100)

    ##############################################################################################################################

        #Controla o botão "DIFICULDADE"
        if mouse.is_over_object(dificuldade):
            dificuldade = GameImage("dificuldade_verde.png")
            dificuldade.set_position(menu.width/2-dificuldade.width/2, menu.height/2-(jogar.height/2)-45)

            dificuldade_Colorido = True

            if(mouse.is_button_pressed(1)):
                escolha(menu)

        elif dificuldade_Colorido:
            dificuldade = GameImage("dificuldade.png")
            dificuldade.set_position(menu.width/2-dificuldade.width/2, menu.height/2-(jogar.height/2)-45)

    ##############################################################################################################################

    #Controla o botão "RANKING"
        if mouse.is_over_object(ranking):
            ranking = GameImage("ranking_verde.png")
            ranking.set_position(menu.width/2-ranking.width/2, menu.height/2-(jogar.height/2)+10)

            ranking_Colorido = True

            if(mouse.is_button_pressed(1)):
                setranking(menu)


        elif ranking_Colorido:
            ranking = GameImage("ranking.png")
            ranking.set_position(menu.width/2-ranking.width/2, menu.height/2-(jogar.height/2)+10)

    ##############################################################################################################################

    #Controla o botão "SAIR"
        if mouse.is_over_object(sair):
            sair = GameImage("sair_verde.png")
            sair.set_position(menu.width/2-sair.width/2, menu.height/2-(jogar.height/2)+65)

            sair_Colorido = True

            if(mouse.is_button_pressed(1)):
                menu.close()   

        elif sair_Colorido:
            sair = GameImage("sair.png")
            sair.set_position(menu.width/2-sair.width/2, menu.height/2-(jogar.height/2)+65)

    ##############################################################################################################################

        menu.set_background_color((0,0,0))
        jogar.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()
        menu.update()

menu()