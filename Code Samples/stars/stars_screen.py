import sys
import pygame


class StarScreen:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        # Adding full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height - 70
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('My Stars')

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """ Redraw the screen during each pass through the loop """
        self.screen.fill((0, 94, 184))
        pygame.display.flip()

    def _check_events(self):
        """ Track keyboard and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    my_star_sky = StarScreen()
    my_star_sky.run_game()