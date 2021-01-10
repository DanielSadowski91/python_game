"""ALien"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for only alien"""

    def __init__(self, ai_game):
        """Creating an alien and setting position of alien"""
        super().__init__()
        self.screen = ai_game.screen

        #loading alien image and setting his atr rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #putting new alien in left top corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storing horizontal position of alien
        self.x = float(self.rect.x)
        