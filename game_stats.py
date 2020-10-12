class GameStats():
    """Track statistics for Alien Invader"""

    def __init__(self,ai_settings):
        """"Initialize statics"""
        self.ai_settings = ai_settings
        self.reset_status = ai_settings
        self.reset_stats()

        #Start Alien Invasion in an active state.
        self.game_active = True

        #Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize staticstics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

        # High score should never be reset.
        self.high_score = 0