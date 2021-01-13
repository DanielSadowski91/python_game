"""Class for button"""
import pygame.font

class Button():
    """Settings for button"""

    def __init__(self, ai_game, msg):
        """Starting button"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Dimension and settings of button
        self.width, self.height = 200,50
        self.button_color = (0, 255, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #creation rect button in the center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Messege showed by button
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Putting messege in generated rect and center text"""
        self.msg_image = self.font.render(msg,True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """show empty button and text above it"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image.rect)
