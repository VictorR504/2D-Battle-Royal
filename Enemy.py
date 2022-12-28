import pygame 
from Entity import Entity
from os import walk

class Enemy(Entity):
    def __init__(self, pos, groups,obstacle_sprite,create_attack,destroy_weapon,damage_player):
        super().__init__(groups)
        self.sprite_type = 'enemy'
        self.obstacle_sprite = obstacle_sprite

        # graphics setup
        self.import_graphics()
        self.status = 'idle'
        self.image = pygame.image.load('Tiles/EnemyAnimation/idle/idle.png').convert_alpha()

        # movment
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)

        # stats
        self.speed = 2
        self.attack_radius = 50
        self.notice_radius = 700
        self.health = 3
        self.resistans = 3
        self.attack_damage = 1

        # Attacking
        self.can_attack = True
        self.attack_cooldown = 400
        self.attack_time = None

        self.create_attack = create_attack
        self.destroy_weapon = destroy_weapon

        self.damage_player = damage_player

        # invincibillity timer
        self.vulnerble = True
        self.hit_time = None
        self.duration = 300


    # reusing this method in two classes, add this tom 
    def import_folder(self,path):
            surface_list = []

            for _,__,img_files in walk(path):
                for image in img_files:
                    full_path = path + '/' + image
                    image_surf = pygame.image.load(full_path).convert_alpha()
                    surface_list.append(image_surf)

            return surface_list



    def import_graphics(self):
        self.animations = {'idle': [], 'move':[], 'attack':[]}
        main_path = f'Tiles/EnemyAnimation/'
        for animation in self.animations.keys():
            self.animations[animation] = self.import_folder(main_path + animation)



    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)

        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        return (distance,direction)



    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'



    def actions(self,player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage,self.create_attack())
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()



    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerble:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)



    def cooldown(self):
        current_time = pygame.time.get_ticks()
        
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerble:
            if current_time - self.hit_time >= self.duration:
                self.vulnerble = True


    def get_damage(self,player,attack_type):
        if self.vulnerble:
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            self.hit_time = pygame.time.get_ticks()
            self.vulnerble = False

    def cheack_death(self):
        if self.health <= 0:
            self.kill()
            
    def hit_reaction(self):
        if not self.vulnerble:
            self.direction *= - self.resistans

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldown()
        self.cheack_death()

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)

