import pygame

class Level:

#------------------------------------------------------------------------------#
#--------------------------------Constructor-----------------------------------#
#------------------------------------------------------------------------------#

    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

#------------------------------------------------------------------------------#
#-----------------------------------Methods------------------------------------#
#------------------------------------------------------------------------------#

    def run(self):
        pass
