import pygame, sys
from Settings import *

#------------------------------------------------------------------------------#
#-----------------------------Initialization-----------------------------------#
#------------------------------------------------------------------------------#
class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.clock = pygame.time.Clock()

#------------------------------------------------------------------------------#
#---------------------------------Game Loop------------------------------------#
#------------------------------------------------------------------------------#

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(('black'))
            pygame.display.update()
            self.clock.tick(FPS)
            pygame.display.set_caption('CockFight')
            

#------------------------------------------------------------------------------#
#---------------------------------Runs My Game---------------------------------#
#------------------------------------------------------------------------------#

if __name__ == '__main__':
    game = Game()
    game.run()

