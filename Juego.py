import pygame
import sys
from pygame.locals import *
import random
from Products import *
import time

class Juego():
    
    i=0
    width = 900
    height = 800
    colour = (227,166,162)
    empezar = True
    megaman = rightMegaman()
    auxlist = megaman.get_sprites()
    speed=100
    

    pygame.init()
    posX=100
    posY=400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Prueba")

    
    while empezar:
        screen.fill(colour)
        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
                empezar = False
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                if i.key==K_LEFT:
                    megaman = leftMegaman()
                    auxlist = megaman.get_sprites()

                    for i in range(0, 7):
                        if i==6:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posX-= speed
                            pygame.display.update()
                            time.sleep(0.1)
                        else:
                            screen.fill(colour)
                            screen.blit(auxlist[i], (posX, posY))
                            posX -= speed
                            pygame.display.update()
                            time.sleep(0.1)


                elif i.key==K_RIGHT:
                    megaman = rightMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,7):
                        if i==6:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posX-= speed
                            pygame.display.update()
                            time.sleep(0.1)
                        else:

                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))
                            posX += speed
                            pygame.display.update()
                            time.sleep(0.1)
                elif i.key==K_UP:
                    megaman = upMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,3):
                        if i==3:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posY-= speed
                            pygame.display.update()
                            time.sleep(0.1)
                        else:

                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))
                            posY -= speed
                            pygame.display.update()
                            time.sleep(0.1)
                elif i.key==K_DOWN:
                    megaman = downMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,2):
                        if i==2:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posY+= speed
                            pygame.display.update()
                            time.sleep(0.15)
                        else:

                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))
                            posY += speed
                            pygame.display.update()
                            time.sleep(0.15)
                elif i.key==K_SPACE:
                    megaman = spaceMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,3):
                        if i==3:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))

                            pygame.display.update()
                            time.sleep(0.2)
                        else:

                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))

                            pygame.display.update()
                            time.sleep(0.2)



            

        




