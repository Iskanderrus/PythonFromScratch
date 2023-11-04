import sys
import pygame
from random import randint
from star import Star


class StarScreen:
    def __init__(self):
        pygame.init()
        self.stars = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        # Adding full screen mode
        self.screen_height = 800
        self.screen_width = 900
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        pygame.display.set_caption('My Stars')
        self._create_stars()

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """ Redraw the screen during each pass through the loop """
        self.screen.fill((0, 94, 184))
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        """ Track keyboard and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_stars(self):
        """ Create the fleet of the aliens """
        # Make an alien
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height
        while current_y < (self.screen_height - 1 * star_height):
            while current_x < (self.screen_width - 1 * star_width):
                current_x = randint(0, self.screen.get_width())
                current_y = randint(0, self.screen.get_height())
                self._create_star(current_x, current_y)
                current_x += 3 * star_width
            current_x = star_width
            current_y += 3.75 * star_height

    def _create_star(self, x_position, y_position):
        """ Create an alien and place it in the row """
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)


if __name__ == '__main__':
    my_star_sky = StarScreen()
    my_star_sky.run_game()