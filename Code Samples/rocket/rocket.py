import pygame
from settings import Settings

class Rocket:
    """ A class to manage the rocket """

    def __init__(self, rocket_game):
        """ Initialize the rocket and set its start position """
        self.screen = rocket_game.screen
        self.settings = Settings()
        self.screen_rect = rocket_game.screen.get_rect()

        # Load the rocket image and get its rect
        self.image = pygame.image.load('images/rocket.png')
        self.image = pygame.transform.scale(self.image, (self.settings.rocket_width, self.settings.rocket_height))
        self.rect = self.image.get_rect()

        # Start each new rocket at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the rocket at its current location """
        self.screen.blit(self.image, self.rect)
