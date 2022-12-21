import pygame
from Settings import *

class Tile(pygame.sprite.Sprite):

#------------------------------------------------------------------------------#
#------------------------------------Constructor-------------------------------#
#------------------------------------------------------------------------------#

    def __init__(self,pos,groups):
        super().__init__(groups)
        # self.image = pygame.image.load('../down a folder/folder name/file name.png').convert_alpha()
        self.image = pygame.Surface((60,60))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)