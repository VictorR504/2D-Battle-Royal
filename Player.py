import pygame
from Settings import *

class Player(pygame.sprite.Sprite):

#------------------------------------------------------------------------------#
#------------------------------------Constructor-------------------------------#
#------------------------------------------------------------------------------#

    def __init__(self,pos,groups,obstacle_sprite):
        super().__init__(groups)
        # self.image = pygame.image.load('../down a folder/folder name/file name.png').convert_alpha()
        self.image = pygame.Surface((40,40))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5
        self.obstacle_sprite = obstacle_sprite

        self.direction = pygame.math.Vector2()

#------------------------------------------------------------------------------#
#------------------------------------Methods-----------------------------------#
#------------------------------------------------------------------------------#

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,speed):
        # Check i vector has a length..!
        if self.direction.magnitude() != 0:
            # If it has a lenght, set it to 1
            self.direction = self.direction.normalize()

        # Set speed and Checks for collisons...!
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')



    def collision(self,directrion):
        if directrion == 'horizontal':
            for sprite in self.obstacle_sprite:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        
        if directrion == 'vertical':
            for sprite in self.obstacle_sprite:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # Moving Down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # Moving Up
                        self.rect.top = sprite.rect.bottom

#------------------------------------------------------------------------------#
#-------------------------------------Update-----------------------------------#
#------------------------------------------------------------------------------#

    def update(self):
        self.input()
        self.move(self.speed)