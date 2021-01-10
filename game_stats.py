""" doc for gamestats"""
class GameStats:
    """checking statistic data in game 'Alien Invasion' """

    def __init__(self, ai_game):
        """Initation of statistic data"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Variable statistic data in the game"""
        self.ships_left = self.settings.ship_limit
