import pygame
import sys

from settings import Settings
from rocket import Rocket

class SkyRocketingRocket:
    def __init__(self):
        """ Initialize the game, create game resources """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Sky Rocketing Rocket")
        self.rocket = Rocket(self)

    def run_game(self):
        """ Start the main loop of the game """
        while True:
            # Watch the keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.rocket.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    sky_rocketing_rocket = SkyRocketingRocket()
    sky_rocketing_rocket.run_game()
