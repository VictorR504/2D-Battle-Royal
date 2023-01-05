import pygame
from os import walk
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.damage = 0
        self.direction = pygame.math.Vector2()

    def move(self,speed):
        # Check i vector has a length..! 
        if self.direction.magnitude() != 0:
            # If it has a lenght, set it to 1
            self.direction = self.direction.normalize() # If not, player will walk faster in a diagnal direction

    # Set speed and Checks for collisons...!
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self,directrion):
        if directrion == 'horizontal':
            for sprite in self.obstacle_sprite:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        
        if directrion == 'vertical':
            for sprite in self.obstacle_sprite:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Moving Down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Moving Up
                        self.hitbox.top = sprite.hitbox.bottom      

    # Get flickering animations....
    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0: 
            return 255
        else:
            return 0

    def import_folder(self,path):
        surface_list = []

        for _,__,img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

        return surface_list

