from PPlay.window import * 
from PPlay.sprite import *
from PPlay.gameimage import *
from inimigos import criar_inimigos
from inimigos import mover_inimigos
from inimigos import move_down
import random
from PPlay.collision import *


def tela(dificuldade, tela):
    #mal implementação, era mais simples só pedir a tela, fazendo isso você cria uma variável de função que pode desencadear diversos erros
    """"#Cria a janela do menu
    tela = Window(1040, 500)

    #Dá um título ao menu
    tela.set_title("Space Invanders")"""


    #Recebe acesso ao teclado
    teclado = Window.get_keyboard()

    nave = Sprite("nave.png")
    nave.set_position(tela.width/2-nave.width/2, tela.height*9/10-nave.height)

    #Bala
    balas = []

    #Fundo
    fundo = GameImage("fundo.png")
    fundo.set_position(0, 0)

    contador = 1

    tela.delay(50)

    quantidade_de_linhas = random.randint(2,4)
    quantidade_de_colunas = random.randint(4,6)
    matriz_de_inimigos = criar_inimigos(tela, quantidade_de_linhas, quantidade_de_colunas) #definir primeiro o tamanho da linha e depois o da coluna
    dir = 1 #direção dos inimigos
    vely = 50 #20

    score = 0

    #Gameloop
    while True:

        #Volta ao menu
        if(teclado.key_pressed("ESC")):  
            break

        #Movimento da nave
        if(teclado.key_pressed("D")):  
            nave.move_x(200*tela.delta_time()*dificuldade)

        if(teclado.key_pressed("A")):  
            nave.move_x(-200*tela.delta_time()*dificuldade)

        if(nave.x<0):
            nave.x = 0

        if((nave.x+nave.width)>tela.width):
            nave.x = tela.width-nave.width

        ##################################################
        if (teclado.key_pressed("SPACE") and (contador>1)):
            bala = Sprite("bala.png")
            balas.append(bala)
            bala.set_position(nave.x+nave.width/2-bala.width/2, nave.y-nave.height/2)
            contador = 0

        for bala in balas:
            bala.move_y(-200*tela.delta_time())
            if (bala.y > tela.height + bala.height):
                balas.remove(bala)

        contador += tela.delta_time()*1.2*dificuldade

        for bala in balas:
            for n in range (len(matriz_de_inimigos)-1,-1, -1): #começa por baixo
                for inimigo in matriz_de_inimigos[n]:
                    if Collision.collided(bala, inimigo):
                        balas.remove(bala) if bala in balas else 1 #tava dando algum erro aqui então precisei colocar isso para resolver o problema
                        matriz_de_inimigos[n].remove(inimigo)
                        score += int(1000*inimigo.y**(-1)) if inimigo.y!=0 else 10
                        break

        fundo.draw()
        for bala in balas:
            bala.draw()
        for n in range(len(matriz_de_inimigos)):
            for inimigo in matriz_de_inimigos[n]:
                test = mover_inimigos(inimigo, dificuldade, tela, dir)
                if test == True:
                    dir *= -1
                    move_down(matriz_de_inimigos, vely, dificuldade, tela)
                if inimigo.y >= tela.height - inimigo.height:
                    return False
        nave.draw()
        tela.draw_text((str(f"{(int((tela.delta_time())**(-1)))}" if tela.delta_time() else 0)), tela.width/300, tela.height/300, 20, [255, 0, 0])
        tela.draw_text((str(score)), tela.width - 20*(len(str(score))), tela.height/300, 30, [255, 255, 255])

        tela.update()
