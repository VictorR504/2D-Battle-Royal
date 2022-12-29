import pygame

class Attack(pygame.sprite.Sprite):
    def __init__(self,enemy,groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        # Get direction from player
        direction = enemy.status.split('_')[0]

        # grafik
        self.image = pygame.Surface((8,8))

        # placment
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = enemy.rect.midright + pygame.math.Vector2(0,5))

        elif direction == 'left':
            self.rect = self.image.get_rect(midright = enemy.rect.midleft + pygame.math.Vector2(0,5))

        else:
            self.rect = self.image.get_rect(center = enemy.rect.center)