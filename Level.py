import pygame
from Settings import *
from Tile import Tile
from Player import Player

class Level:

#------------------------------------------------------------------------------#
#--------------------------------Constructor-----------------------------------#
#------------------------------------------------------------------------------#

    def __init__(self):

        # get the display surface

        self.visible_sprites = CustomDrawAndCamera()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite set-up
        self.create_map()

#------------------------------------------------------------------------------#
#-----------------------------------Methods------------------------------------#
#------------------------------------------------------------------------------#

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)

#------------------------------------------------------------------------------#
#-----------------------------------Run Method---------------------------------#
#------------------------------------------------------------------------------#

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


# Make screen follw player, HARD TO FOLLOW...WEIRD MATH!
class CustomDrawAndCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.half_width = self.display_surface.get_size()[0] / 2 # //
        self.half_height = self.display_surface.get_size()[1] / 2 # //

        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):

        # Getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
        
        
        
        