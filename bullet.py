"""Settings of bullet"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullets managment fired from ship"""

    def __init__(self, ai_game):
        """Creation bullet in actual position of ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Creation rect bullet in (0,0)
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #position of bullet is a float
        self.y_high = float(self.rect.y)

    def update(self):
        """bullet on screen"""
        #update position of bullet
        self.y_high -= self.settings.bullet_speed
        #update position of rect bullet
        self.rect.y = self.y_high

    def draw_bullet(self):
        """Display bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
