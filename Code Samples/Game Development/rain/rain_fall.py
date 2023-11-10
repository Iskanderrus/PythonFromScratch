import sys
import pygame
from random import randint
from drop import Drop


class RainFall:
    def __init__(self):
        pygame.init()
        self.drops = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        # Adding full screen mode
        self.screen_height = 900
        self.screen_width = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Rainy Day')
        self._create_drops()

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self._update_screen()
            self._update_drops()
            self.clock.tick(60)

    def _update_drops(self):
        self._check_rain_edges()
        self.drops.update()

    def _update_screen(self):
        """ Redraw the screen during each pass through the loop """
        self.screen.fill((230, 230, 250))
        self.drops.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        """ Track keyboard and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_drops(self):
        """ Create the fleet of the aliens """
        # Make an alien
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        current_x, current_y = drop_width, drop_height
        while current_y < (self.screen_height - 3 * drop_height):
            while current_x < (self.screen_width - 2 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width
            current_x = drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x_position, y_position):
        """ Create an alien and place it in the row """
        new_drop = Drop(self)
        new_drop.x = x_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.drops.add(new_drop)

    def _check_rain_edges(self):
        drops_to_remove = []
        for drop in self.drops.sprites():
            if drop.check_edges():
                self._change_image()
                drops_to_remove.append(drop)

        for drop in drops_to_remove:
            drop.kill()  # Remove the drop from the sprite group

        # Check if all drops are removed, then create a new row
        if len(self.drops) == 0:
            self._create_drops()

    def _change_image(self):
        for drop in self.drops.sprites():
            drop._convert_image()
            break

if __name__ == '__main__':
    my_rainy_day = RainFall()
    my_rainy_day.run_game()
