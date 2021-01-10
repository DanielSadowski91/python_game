"""ALien"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for only alien"""

    def __init__(self, ai_game):
        """Creating an alien and setting position of alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #loading alien image and setting his atr rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #putting new alien in left top corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing horizontal position of alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """return True when alien is nearby edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moving alien on the right or left"""
        self.x += (self.settings.alien_speed *
                    self.settings.fleet_direction)
        self.rect.x = self.x
