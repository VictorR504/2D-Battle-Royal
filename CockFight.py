import pygame, sys
from Settings import *
from Level import Level

#------------------------------------------------------------------------------#
#-----------------------------Initialization-----------------------------------#
#------------------------------------------------------------------------------#
class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('CockFight')
        self.clock = pygame.time.Clock()

        self.level = Level()

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
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
     
            
#------------------------------------------------------------------------------#
#---------------------------------Runs My Game---------------------------------#
#------------------------------------------------------------------------------#

if __name__ == '__main__':
    game = Game()
    game.run()

