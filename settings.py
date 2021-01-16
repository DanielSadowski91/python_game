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
        self.ship_limit = 3

        #Settings for bullets
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #settings for alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #change game speed
        self.speedup_scale = 1.1

        #change number of points after alien hit
        self.score_scale = 1.5

        self.initalize_dynamic_settings()


    def initalize_dynamic_settings(self):
        """changing settings in game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #flet_direction -1 = left, 1 = right
        self.fleet_direction = 1

        #score
        self.alien_points = 50

    def increase_speed(self):
        """Changing speed settings and alien score"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
