from PPlay.sprite import *
from PPlay.window import *


def criar_inimigos(janela, tam_linha, tam_coluna):
    matriz_de_inimigos = []
    for n in range(tam_linha):
        linha_de_inimigos=[]
        for m in range(tam_coluna):
            monstro = Sprite("invader1.png")
            monstro.set_position(janela.width/8+m*monstro.width/2+m*monstro.width, janela.height/14+n*monstro.height/2+n*monstro.height)
            linha_de_inimigos.append(monstro)
        matriz_de_inimigos.append(linha_de_inimigos)
    return matriz_de_inimigos

def mover_inimigos(inimigo, dificuldade, janela, dir):
    dx = 100 * dificuldade * janela.delta_time()* dir
    inimigo.x += dx
    inimigo.draw()
    if inimigo.x+inimigo.width>janela.width and dir>0:
        return True
    if inimigo.x<0 and dir < 0:
        return True
    return False

    """dx = 200 * dificuldade * janela.delta_time()
    dy = 50 * dificuldade * janela.delta_time()
    dir = True
    for n in range(len(matriz_de_inimigos)):
        for inimigo in matriz_de_inimigos[n]:
            if inimigo.x + inimigo.width >= janela.width:
                if dx>0 and dir == True:
                    dx *= - 1
                    dir = False
                inimigo.y += dy
                inimigo.x += dx
                print(dx)
            if inimigo.x < 0 and dx < 0:
                if dx<0 and dir == False:
                    dx *= -1
                    dir = True
                inimigo.x += dx
                inimigo.y += dy
            inimigo.x += dx
            inimigo.draw()"""

def move_down(matriz_de_inimigos, dy, dificuldade, janela):
    for n in range(len(matriz_de_inimigos)):
        for inimigo in matriz_de_inimigos[n]:
            inimigo.y += dy * dificuldade

