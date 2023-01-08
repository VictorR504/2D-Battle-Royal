import pygame
from os import walk
from Settings import *

class Tile(pygame.sprite.Sprite):

    def __init__(self,pos,path,groups):
        super().__init__(groups)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        
# Just a test to try some other kind of animation.....NYI
class Grass(pygame.sprite.Sprite):

    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('Tiles/grass/idle/Grass_Animation_01.png').convert_alpha() # Add a varible Path insted to be able to set diffrent pictures and animations in the same class
        self.rect = self.image.get_rect(topleft = pos)
        self.status = 'idle'
        self.import_assets()
        self.animation_speed = 0.15
        self.frame_index = 0

    def import_folder(self,path): # Add agrument to be able to take a set Path to picture assets
        surface_list = []

        for _,__,img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

        return surface_list

    def import_assets(self): # Write pre determind paths and dict and just add aguments to the method/funktion to be able to have many diffrent objects with animations....! Should be doeable...i Hope!!!
        object_path = 'Tiles/grass/'
        self.animations = {'idle': [] }

        for animation in self.animations.keys():
            full_path = object_path + animation
            self.animations[animation] = self.import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        self.animate()