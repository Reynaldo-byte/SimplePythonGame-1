# Esta es nuestra clase de fabricas, ya que usamos el patron Abstract Factory
from Products import *


# Farica abstracta que tiene como metodos mover izq y mover der


class AbstractFactory():
    def moveLeft(self): pass

    def moveRight(self): pass

    def moveDown(self): pass

    def moveUp(self): pass

    def power(self): pass

    def choqueI(self): pass

    def choqueD(self): pass

# Fabrica concreta que produce sprites de cada personaje

class MegamanSpritesFactory(AbstractFactory):

    def moveLeft(self):
        left = leftMegaman()
        return left.get_sprites()

    def moveRight(self):
        right = rightMegaman()
        return right.get_sprites()

    def moveUp(self):
        up = upMegaman()
        return up.get_sprites()

    def moveDown(self):
        down = downMegaman()
        return down.get_sprites()

    def power(self):
        power = powerMegaman()
        return power.get_sprites()
    def choqueI(self):
        choqueI = choqueIMegaman()
        return choqueI.get_sprites()

    def choqueD(self):
        choqueD = choqueDMegaman()
        return choqueD.get_sprites()

class GokuSpritesFactory(AbstractFactory):

    def moveLeft(self):
        left = leftGoku()
        return left.get_sprites()

    def moveRight(self):
        right = rightGoku()
        return right.get_sprites()

    def moveDown(self):
        down = downGoku()
        return down.get_sprites()

    def moveUp(self):
        up = upGoku()
        return up.get_sprites()

    def power(self):
        power = powerGoku()
        return power.get_sprites()

    def choqueI(self):
        choqueI = choqueIGoku()
        return choqueI.get_sprites()

    def choqueD(self):
        choqueD = choqueDGoku()
        return choqueD.get_sprites()

class mainFactory(AbstractFactory):
    def moveRight():
        right = personajes()
        return right.get_sprites()