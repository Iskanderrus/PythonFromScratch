class Settings:
    """ A class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initialize game's settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 18, 122)

        # Ship settings
        self.ship_height = 82
        self.ship_width = 60
        self.ship_rotation = 90
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 240, 245)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_height = 35
        self.alien_width = 55
        self.alien_speed = 1.0
