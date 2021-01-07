""" Settings for ship"""
import pygame

class Ship:
    """ Class for ship managment"""

    def __init__(self, ai_game):
        """Starting the ship and his entry position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #each new ship appears at the bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """display ship in his actual position"""
        self.screen.blit(self.image,self.rect)
