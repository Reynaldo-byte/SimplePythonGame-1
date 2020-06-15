import pygame
import sys
from pygame.locals import *
from random import randint
from Products import *
import time
import Character
from Director import *
from Builder import *
from Character import *
import loadImages
from Juego import Juego





class menu():
    def seleccion():
        i = 0
        width = 900
        height = 600
        colour = (227, 166, 162)
        personajes=0
        empezar=True

        pygame.init()

        posX = 100
        posY = 250
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Prueba")
        fuente = pygame.font.Font(None, 20)

        text = "derecha kakaroto, izquierda Megaman"
        mensaje = fuente.render(text, 1, (255, 255, 255))
        screen.blit(mensaje, (15, 250))
        pygame.display.flip()





        while empezar:

            for i in pygame.event.get():

                if i.type == pygame.KEYUP:
                    if i.key == K_LEFT:
                        print("0")
                        auxlist = mainFactory.moveRight()
                        screen.fill(colour)
                        screen.blit(auxlist[0], (posX, posY))
                        pygame.display.update()
                        time.sleep(0.1)
                        pygame.quit()

                        personajes = 0

                        Juego.ventana(personajes)
                        sys.exit()


                    if i.key == K_RIGHT:
                        print("1")
                        auxlist = mainFactory.moveRight()
                        screen.fill(colour)
                        screen.fill(colour)
                        screen.blit(auxlist[1], (posX, posY))
                        pygame.display.update()
                        time.sleep(0.1)

                        personajes = 1
                        Juego.ventana(personajes)
                        pygame.quit()
















