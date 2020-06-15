import pygame
import sys
from pygame.locals import *
from random import randint

from menu import *
from Products import *
import time
import Character
from Director import *
from Builder import *
from Character import *
import loadImages


class Juego:
    def ventana(numero):

        width = 900
        height = 600

        empezar=True

        pygame.init()
        posX = 100
        posY = 250


        pygame.display.set_caption("Prueba")
        auxDirector = Director()

        if numero==1:
            auxDirector.setBuilder(GokuBuilder())
        else:
            if numero==0:
                auxDirector.setBuilder(MegamanBuilder())
        charac = auxDirector.getChar()
        charac.defPositions(posX, posY)
        background = loadImages.load("background/mexBack.jpeg")
        screen = pygame.display.set_mode((width, height))
        while empezar:
            for i in pygame.event.get():
                if i.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    empezar = False


            screen.blit(background, (0, 0))
            charac.update()
            charac.drawCharacter(screen)
            pygame.display.update()





