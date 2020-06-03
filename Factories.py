# Esta es nuestra clase de fabricas, ya que usamos el patron Abstract Factory
from Products import *

# Farica abstracta que tiene como metodos mover izq y mover der

class AbstractFactory():
    def moveLeft(self): pass
    def moveRight(self): pass


# Fabrica concreta que produce sprites de cada personaje

class MegamanSpritesFactory(AbstractFactory):

    def moveLeft(self):
        left = leftMegaman()
        return left.get_sprites()

    def moveRight(self):
        right = rightMegaman()
        return right.get_sprites
    def moveup(self):
        up = upMegaman()
        return up.get_sprites
    def movedown(self):
        down=downMegaman()
        return down.get_sprites
    def space(self):
        space=spaceMegaman()
        return space.get_sprites()

