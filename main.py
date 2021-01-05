import sys

import pygame

class AlienInvasion:
    """Class for resources managment and a way for working game"""

    def __init__(self):
        """Initializing the game and opening its resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        Starting the main loop
        """
        while True:
            #Waiting for any key
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Displaying the last modified screen
            pygame.display.flip()
    
if __name__ == '__main__':
    #activate the game
    ai = AlienInvasion()
    ai.run_game()

