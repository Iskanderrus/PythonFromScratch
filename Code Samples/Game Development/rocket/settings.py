class Settings:
    """ A Class to store all settings for Star Rocketing Rocket """

    def __init__(self):
        """ Initialize the game's settings """

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (176, 224, 230)

        # Rocket settings
        self.rocket_height = 85
        self.rocket_width = 52
        self.rocket_rotation = 90
        self.rocket_speed = 1.5
