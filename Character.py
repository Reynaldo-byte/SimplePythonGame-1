

import pygame
from pygame.sprite import Sprite
from pygame import *
import time


class Character(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.direction = 1
        self.cont = 0
        self.speed = 20
        self.movementLeft = True
        self.movementRight = True
        self.movementUp=True

    def defPositions(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY

    def set_sprites(self, images):
        self.graphics = images
        self.image = self.graphics[self.direction][self.cont]
        # self.rect = self.sprite.get_rect()

    def update(self):
        # self.image= self.graphics [1][0]
        pressed = pygame.key.get_pressed()

        if pressed[K_SPACE]:
            self.direction=4
            try:
                self.image = self.graphics[self.direction][self.cont]
                self.cont += 1
                self.cont %= len(self.graphics[self.direction])
                if self.cont == 1:
                    time.sleep(3)
                else:
                    time.sleep(0.1)
            except:
                print("Que velocidad!!")

        if self.movementLeft:
            if pressed[K_LEFT]:
                self.posX -= self.speed
                time.sleep(0.06)
                self.direction = 0
        if self.movementRight:
            if pressed[K_RIGHT]:
                self.posX += self.speed
                time.sleep(0.06)
                self.direction = 1
        if self.movementUp:
            if pressed[K_UP]:
                self.direction = 2
                self.posY -= self.speed
                time.sleep(0.06)

            """elif pressed[K_UP]:
            self.direction = 2
            for i in range(0,3):
                self.posY -= self.speed
                self.image = self.graphics[self.direction][i]
                print("me voy de la casa si esto no funiona xdd :(")
                time.sleep(0.3)
        elif pressed[K_DOWN]:
            self.posY += self.speed
            self.direction = 3
            time.sleep(0.08)"""

        if pressed[K_RIGHT] or pressed[K_LEFT] or pressed[K_SPACE] or pressed[K_UP]:
            try:
                self.image = self.graphics[self.direction][self.cont]
                self.cont += 1
                self.cont %= len(self.graphics[self.direction])
            except:
                print("Que velocidad!!")
            if self.posY<250:
                self.posY+=30
                time.sleep(0.1)
            try:

                self.image = self.graphics[self.direction][self.cont]
                self.cont += 1
                self.cont %= len(self.graphics[self.direction])
            except:
                print()

            if self.posX < 0:
                self.movementLeft = False
                self.direction=6
                try:

                    self.image = self.graphics[self.direction][self.cont]
                    self.cont += 1
                    self.cont %= len(self.graphics[self.direction])
                except:
                    print()
                else:
                    self.movementLeft = True

            if self.posX > 650:
                self.movementRight = False
                self.direction = 5
                try:

                    self.image = self.graphics[self.direction][self.cont]
                    self.cont += 1
                    self.cont %= len(self.graphics[self.direction])
                except:
                    print()
            else:
                self.movementRight = True
        else:
            self.cont = 0
            self.image = self.graphics[self.direction][0]

    def drawCharacter(self, screen):
        screen.blit(self.image, (self.posX, self.posY))