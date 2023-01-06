import pygame, sys
from Settings import *
from Gameplay import Gameplay

#------------------------------------------------------------------------------#
#-----------------------------Initialization-----------------------------------#
#------------------------------------------------------------------------------#
class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Zombie Survival')
        self.clock = pygame.time.Clock()

        self.gameplay = Gameplay()

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
            self.gameplay.run()
            pygame.display.update()
            self.clock.tick(FPS)
     
            
#------------------------------------------------------------------------------#
#---------------------------------Runs My Game---------------------------------#
#------------------------------------------------------------------------------#

game = Game()
game.run()

