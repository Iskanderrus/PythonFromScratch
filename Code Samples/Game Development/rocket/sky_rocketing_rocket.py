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

    def _check_keydown_events(self, event):
        """ Respond to pressing the key """
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

    def _check_events(self):
        # Watch the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def run_game(self):
        """ Start the main loop of the game """
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    sky_rocketing_rocket = SkyRocketingRocket()
    sky_rocketing_rocket.run_game()
