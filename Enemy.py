import pygame 
from Entity import Entity
from os import walk

class Enemy(Entity):
    def __init__(self, pos, groups,obstacle_sprite):
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

    def import_folder(self,path):
            surface_list = []

            for _,__,img_files in walk(path):
                for image in img_files:
                    full_path = path + '/' + image
                    image_surf = pygame.image.load(full_path).convert_alpha()
                    surface_list.append(image_surf)

            return surface_list

    def import_graphics(self):
        self.animations = {'idle': [], 'move':[]}
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

        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        if self.status == 'attack':
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.move(self.speed)
        self.animate()

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)
