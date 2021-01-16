""" doc for gamestats"""
class GameStats:
    """checking statistic data in game 'Alien Invasion' """

    def __init__(self, ai_game):
        """Initation of statistic data"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Run game in inactive state
        self.game_active = False

        #highest score never reset
        self.high_score = 0

    def reset_stats(self):
        """ Variable statistic data in the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
