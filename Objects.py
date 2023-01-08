import pygame
from Settings import *

class Tile(pygame.sprite.Sprite):

#------------------------------------------------------------------------------#
#------------------------------------Constructor-------------------------------#
#------------------------------------------------------------------------------#

    def __init__(self,pos,path,groups):
        super().__init__(groups)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)