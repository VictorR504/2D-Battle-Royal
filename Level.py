import pygame
from Settings import *
from Tile import Tile
from Player import Player
from Weapon import Weapon
from Enemy import Enemy
from EnemyAttack import Attack

class Level:

#------------------------------------------------------------------------------#
#--------------------------------Constructor-----------------------------------#
#------------------------------------------------------------------------------#

    def __init__(self):

        # get the display surface

        self.visible_sprites = CustomDrawAndCamera()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprite
        self.current_attack = None
        self.attacking_enemy = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

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
                    Tile((x,y),[self.obstacle_sprites])

                if col == 'e':
                    self.enemy = Enemy((x,y),[self.visible_sprites, self.attackable_sprites],self.obstacle_sprites,self.enemy_attack,self.stop_attacking,self.damage_player)

                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.create_attack,self.destroy_weapon)



    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def enemy_attack(self):
        self.attacking_enemy = Attack(self.enemy,[self.visible_sprites,self.attack_sprites])

    def stop_attacking(self):
        if self.attacking_enemy:
            self.attacking_enemy.kill()
        self.attacking_enemy = None

    def destroy_weapon(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprite = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprite:
                    for target_sprite in collision_sprite:
                        target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def damage_player(self, amount):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()


#------------------------------------------------------------------------------#
#-----------------------------------Run Method---------------------------------#
#------------------------------------------------------------------------------#

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()


# Make screen follw player, HARD TO FOLLOW...WEIRD MATH!
class CustomDrawAndCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.half_width = self.display_surface.get_size()[0] / 2 # //
        self.half_height = self.display_surface.get_size()[1] / 2 # //

        self.offset = pygame.math.Vector2()

        # Creating the floor on the map
        self.floor_surf = pygame.image.load('Tiles/bakground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):

        # Getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery): # Ripted from internet, 
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
        
    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
        
        