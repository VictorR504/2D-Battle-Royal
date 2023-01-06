import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        # Get direction from player
        direction = player.status.split('_')[0]
        # graphics settings
        image_path = f'Tiles/weapon/{direction}.png'
        self.image = pygame.image.load(image_path)

        # Placment of weapon (string name of direction == same name in directory)
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-35,5))

        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(35,5))

        else:
            self.rect = self.image.get_rect(center = player.rect.center)