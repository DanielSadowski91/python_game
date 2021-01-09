""" Settings for alien invasion"""
class Settings:
    """
    Class for game settings
    """

    def __init__(self):
        """Starting game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #settings for ship
        self.ship_speed = 1.5

        #Settings for bullets
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
