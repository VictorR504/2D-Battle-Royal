import pygame

#------------------------------------------------------------------------------#
#-----------------------------Class Constructor--------------------------------#
#------------------------------------------------------------------------------#

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,speed):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill(("red"))
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed

#------------------------------------------------------------------------------#
#----------------------------------Methods-------------------------------------#
#------------------------------------------------------------------------------#

    def get_player_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

#------------------------------------------------------------------------------#
#-----------------------------Update Methods-----------------------------------#
#------------------------------------------------------------------------------#

    def update(self):
        self.get_player_input()