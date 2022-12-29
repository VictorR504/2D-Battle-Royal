import pygame
from Settings import *
from os import walk
from Entity import Entity

class Player(Entity):

#------------------------------------------------------------------------------#
#------------------------------------Constructor-------------------------------#
#------------------------------------------------------------------------------#

    def __init__(self,pos,groups,obstacle_sprite,create_attack,destroy_weapon):
        super().__init__(groups)
        self.image = pygame.image.load('Tiles/PlayerAnimation/player_idel.png').convert_alpha()
        #self.image = pygame.Surface((40,40))
        #self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-20)

        # Graphics Setup
        self.import_player_assets()
        self.status = 'right'

        # stats
        self.health = 3
        self.attack_damage = 1
      

        # Movment Setup
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.create_attack = create_attack
        self.destroy_weapon = destroy_weapon

        self.obstacle_sprite = obstacle_sprite

        # Getting attacked
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500
        

#------------------------------------------------------------------------------#
#------------------------------------Methods-----------------------------------#
#------------------------------------------------------------------------------#

    def import_player_assets(self):
        character_path = 'Tiles/PlayerAnimation/'
        self.animations = { 'right_idle': [], 'left_idle': [], 'right': [], 'left': [], 'left_attack': [], 'right_attack': [] }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = self.import_folder(full_path)

        # print(self.animations)

    def get_status(self):

        # idle 
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    # ovverid idle
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        
        if self.attacking == False:
            self.status = self.status.replace('_attack', '_idle')


    def import_folder(self,path):
        surface_list = []

        for _,__,img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

        return surface_list

    def input(self):
        keys = pygame.key.get_pressed()

        # Movment 
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'right'
        elif keys[pygame.K_DOWN]:
            self.direction.y = +1
            self.status = 'left'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = +1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        # Attack
        if keys[pygame.K_RCTRL] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()


    def cooldowns(self):

        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_weapon()

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        # flicker
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

        

    def get_full_weapon_damage(self):
        base_damage = self.attack_damage
        weapon_damage = self.damage
        return base_damage + weapon_damage

#------------------------------------------------------------------------------#
#-------------------------------------Update-----------------------------------#
#------------------------------------------------------------------------------#

    def update(self):
        self.input()
        self.get_status()
        self.cooldowns()
        self.animate()
        self.move(self.speed)