import pygame

#------------------------------------------------------------------------------#
#-----------------------------Class Constructor--------------------------------#
#------------------------------------------------------------------------------#

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,speed):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill(('blue'))
        self.rect = self.image.get_rect(topleft =(x,y))
        self.speed = speed

    def movment(self):
        pass # set movment,

    def update(self):
        pass

    