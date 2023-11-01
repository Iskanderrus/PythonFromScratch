import pygame
import sys


class Rocket:
    def __init__(self):
        """ Initialize the game, create game resources """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Sky Rocketing Rocket")

    def run_game(self):
        """ Start the main loop of the game """
        while True:
            # Watch the keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()
