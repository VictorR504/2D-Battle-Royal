import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        # Get direction from player
        direction = player.status.split('_')[0]

        # grafik
        self.image = pygame.Surface((8,8))

        # placment
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,5))

        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,5))

        else:
            self.rect = self.image.get_rect(center = player.rect.center)