"""Game invasion"""
import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class for resources managment and a way for working game"""

    def __init__(self):
        """Initializing the game and opening its resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)



    def run_game(self):
        """
        Starting the main loop
        """
        while True:
            #Waiting for any key
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #screen refreshing during each loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Displaying the last modified screen
            pygame.display.flip()

if __name__ == '__main__':
    #activate the game
    ai = AlienInvasion()
    ai.run_game()
