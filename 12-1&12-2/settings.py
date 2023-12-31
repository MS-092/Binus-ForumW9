class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        
        # 12-1 Blue Sky
        # Change the background color into blue
        self.bg_color = (0, 0, 255)

        # Ship settings.
        self.ship_speed_factor = 1.5

        # Bullet settings.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
