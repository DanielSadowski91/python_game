""" Settings for ship"""
import pygame

class Ship:
    """ Class for ship managment"""

    def __init__(self, ai_game):
        """Starting the ship and his entry position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #loading ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #each new ship appears at the bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #location of ship is saved as float
        self.x = float(self.rect.x)

        #Option for moving ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update of ship position basen on x"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update location of rect based of self.x value
        self.rect.x = self.x

    def blitme(self):
        """display ship in his actual position"""
        self.screen.blit(self.image,self.rect)
