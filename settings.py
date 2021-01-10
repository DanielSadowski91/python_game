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
        self.bullets_allowed = 3

        #settings for alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #flet_direction -1 = left, 1 = right
        self.fleet_direction = 1
