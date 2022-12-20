import pygame, sys
from Player import Player

#------------------------------------------------------------------------------#
#-----------------------------Initialization-----------------------------------#
#------------------------------------------------------------------------------#
class Game:

    def __init__(self):
        player_sprite = Player((screen_height/2,screen_width/2),5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)
#------------------------------------------------------------------------------#
#-------------------------------GAME LOOP--------------------------------------#
#------------------------------------------------------------------------------#
if __name__ == '__main__':

    #--------------------------Setup Screen--------------------------#
    pygame.init()
    screen_height = 600
    screen_width = 600
    screen = pygame.display.set_mode((screen_height,screen_width))
    pygame.display.set_caption('Cock Fight')
    #----------------------------------------------------------------#
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))
        game.run()
        pygame.display.update()
        clock.tick(60)

