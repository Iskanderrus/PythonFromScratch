import numpy as np


class Settings:
    """ A class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initialize game's static settings """
        # Screen settings
        self.alien_points = None
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = list(np.random.choice(range(256), size=3))

        # Ship settings
        self.ship_height = 82
        self.ship_width = 60
        self.ship_rotation = 90
        self.ship_speed = 4.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = list(np.random.choice(range(256), size=3))
        self.bullets_allowed = 5

        # Alien settings
        self.alien_height = 35
        self.alien_width = 55
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game """
        self.ship_speed = 2.5
        self.bullet_speed = 2.5
        self.alien_speed = 0.9
        self.bg_color = list(np.random.choice(range(256), size=3))
        self.bullet_color = list(np.random.choice(range(256), size=3))

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """ Increase speed settings """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

