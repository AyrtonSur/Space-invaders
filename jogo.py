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

    quantidade_de_linhas = random.randint(3,4)
    quantidade_de_colunas = random.randint(3,4)
    matriz_de_inimigos = criar_inimigos(tela, quantidade_de_linhas, quantidade_de_colunas) #definir primeiro o tamanho da linha e depois o da coluna
    dir = 1 #direção dos inimigos
    vely = 50 #20

    score = 0

    vida = 3

    FPS = 0
    current_fps = 0

    tempo_tiro = tela.time_elapsed()
    time_fps = tela.time_elapsed()
    invicible_time = tela.time_elapsed() - 2000

    balas_inimigos = []

    invicible = False
    animation = False

    tiro_especial = 0
    timer = 2

    #Gameloop
    while True:

        #Volta ao menu
        if teclado.key_pressed("ESC") or vida <= 0:
            nome = input("Digite o seu nome: ")
            with open("registros.txt", "a") as registro:
                registro.write(nome + "&" + str(score) + "\n")
            return False

        #Movimento da nave
        if(teclado.key_pressed("D")) and timer >= 2:
            nave.move_x(200*tela.delta_time()*dificuldade)

        if(teclado.key_pressed("A")) and timer >= 2:
            nave.move_x(-200*tela.delta_time()*dificuldade)

        if(nave.x<0):
            nave.x = 0

        if((nave.x+nave.width)>tela.width):
            nave.x = tela.width-nave.width

        ##################################################
        if (teclado.key_pressed("SPACE") and (contador>1)) and len(matriz_de_inimigos) > 0 and timer >= 2:
            bala = Sprite("bala.png")
            balas.append(bala)
            bala.set_position(nave.x+nave.width/2-bala.width/2, nave.y-nave.height/2)
            contador = 0

        matriz_de_inimigos = [elemento for elemento in matriz_de_inimigos if elemento]

        if tela.time_elapsed() - tempo_tiro > 1000 and len(matriz_de_inimigos) > 0 and tiro_especial<2:
            bala = Sprite("shoot_enemy.png")
            invader1 = random.randint(0, len(matriz_de_inimigos)-1)
            if len(matriz_de_inimigos[invader1])-1 < 0 and len(matriz_de_inimigos)>0:
                invader1 = random.randint(0, len(matriz_de_inimigos)-1)

            invader2 = random.randint(0, len(matriz_de_inimigos[invader1])-1)
            invader = matriz_de_inimigos[invader1][invader2]
            bala.set_position(invader.x+invader.width/2-bala.width/2, invader.y+invader.height/2)
            balas_inimigos.append(bala)
            tempo_tiro = tela.time_elapsed()
            tiro_especial += 1
        elif tela.time_elapsed() - tempo_tiro > 1000 and len(matriz_de_inimigos) > 0 and tiro_especial >= 2:
            bala = Sprite("shoot_enemy_special.png")
            invader1 = random.randint(0, len(matriz_de_inimigos)-1)
            if len(matriz_de_inimigos[invader1])-1 < 0 and len(matriz_de_inimigos)>0:
                invader1 = random.randint(0, len(matriz_de_inimigos)-1)

            invader2 = random.randint(0, len(matriz_de_inimigos[invader1])-1)
            invader = matriz_de_inimigos[invader1][invader2]
            bala.set_position(invader.x+invader.width/2-bala.width/2, invader.y+invader.height/2)
            balas_inimigos.append(bala)
            tempo_tiro = tela.time_elapsed()
            tiro_especial = 0



        for bala in balas:
            bala.move_y(-200*tela.delta_time())
            if (bala.y < 0):
                balas.remove(bala)
        for bala in balas_inimigos:
            bala.move_y(200*tela.delta_time())
            if (bala.y > tela.height + bala.height):
                balas_inimigos.remove(bala)


        contador += tela.delta_time()*1.2*dificuldade

        for bala in balas:
            for n in range (len(matriz_de_inimigos)-1,-1, -1): #começa por baixo
                for inimigo in matriz_de_inimigos[n]:
                    if Collision.collided(bala, inimigo):
                        balas.remove(bala) if bala in balas else 1 #tava dando algum erro aqui então precisei colocar isso para resolver o problema
                        matriz_de_inimigos[n].remove(inimigo)
                        score += int(1000*inimigo.y**(-1)) if inimigo.y!=0 else 10
                        break

        for bala in balas_inimigos:
            if Collision.collided(bala, nave) and invicible == False and bala.image_file == "shoot_enemy.png":
                balas_inimigos.remove(bala) if bala in balas_inimigos else 1
                nave.set_position(tela.width / 2 - nave.width / 2, tela.height * 9 / 10 - nave.height)
                vida -= 1
                timer = 2
                invicible = True
                animation = True
                invicible_time = tela.time_elapsed()
            elif Collision.collided(bala, nave) and invicible == False and bala.image_file == "shoot_enemy_special.png":
                balas_inimigos.remove(bala) if bala in balas_inimigos else 1
                timer = 0

        fundo.draw()
        for bala in balas:
            bala.draw()
        for bala in balas_inimigos:
            bala.draw()
        for n in range(len(matriz_de_inimigos)):
            for inimigo in matriz_de_inimigos[n]:
                test = mover_inimigos(inimigo, dificuldade, tela, dir)
                if test == True:
                    dir *= -1
                    move_down(matriz_de_inimigos, vely, dificuldade, tela)
                if inimigo.y >= tela.height - inimigo.height:
                    return False

        if invicible == True and tela.time_elapsed() - invicible_time > 2000:
            invicible = False

        if animation == False and tela.time_elapsed() - invicible_time <= 2000:
            nave.draw()
            animation = True
        elif animation == False and tela.time_elapsed() - invicible_time > 2000:
            nave.draw()
        else:
            animation = False

        tela.draw_text(str(current_fps), tela.width/300, tela.height/300, 20, [255, 0, 0])
        tela.draw_text((str(score)), tela.width - 20*(len(str(score))), tela.height/300, 30, [255, 255, 255])

        FPS += 1
        if tela.time_elapsed() - time_fps > 100:
            time_fps = tela.time_elapsed()
            current_fps = FPS
            FPS = 0


        if len(matriz_de_inimigos) < 1 and len(balas) < 1:
            quantidade_de_linhas = random.randint(3, 4)
            quantidade_de_colunas = random.randint(3, 4)
            matriz_de_inimigos = criar_inimigos(tela, quantidade_de_linhas, quantidade_de_colunas)
            dir = 1
            dificuldade += 0.1

        timer += 0.004
        tela.update()