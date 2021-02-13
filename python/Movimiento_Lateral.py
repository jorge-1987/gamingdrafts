import pygame
import time
import random

#Definiciones globales
pygame.init()

pancho = 800
papitas = 600

areajuego = pygame.display.set_mode((pancho,papitas))
pygame.display.set_caption('Movimiento Lateral')

black = (0,0,0)
white = (255,255,255)

jancho = 100
jalto = 20

florderelos = pygame.time.Clock()


def game_loop():
    jposx = 350
    jposy = 560

    jmovx = 0

#PINTAR FONDO
    areajuego.fill(black)
#PINTAR Marco


    termino = False

    while not termino:
        pygame.draw.rect(areajuego, black, [jposx, jposy, jancho, jalto])

        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            termino = True
                        if event.key == pygame.K_LEFT:
                            jmovx = -8
                            #print("A la izquierda")
                        elif event.key == pygame.K_RIGHT:
                            jmovx = 8
                            #print("A la derecha")
        
        
        if (jmovx < 0):
            if (jposx + jmovx) > 1:
                jposx = jposx + jmovx
        else:
            if (jposx + jmovx) < 699:
                jposx = jposx + jmovx

        pygame.draw.rect(areajuego, white, [jposx, jposy, jancho, jalto])
        pygame.display.update()
        florderelos.tick(60)

    return 0


def main():

    #Cuerpo del programa que llama al juego
    areajuego.fill(black)
    restantes = game_loop()
    time.sleep(4)
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()