import pygame
from Settings import *
from os import walk

class Player(pygame.sprite.Sprite):

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
        self.frame_index = 0
        self.animation_speed = 0.15

        # Movment Setup
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.create_attack = create_attack
        self.destroy_weapon = destroy_weapon

        self.obstacle_sprite = obstacle_sprite
        

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
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()

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

    def cooldowns(self):

        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_weapon()

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


#------------------------------------------------------------------------------#
#-------------------------------------Update-----------------------------------#
#------------------------------------------------------------------------------#

    def update(self):
        self.input()
        self.get_status()
        self.cooldowns()
        self.animate()
        self.move(self.speed)