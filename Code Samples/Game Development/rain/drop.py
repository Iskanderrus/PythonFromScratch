import pygame
from pygame.sprite import Sprite


class Drop(Sprite):

    def __init__(self, rain_fall):
        super().__init__()
        self.screen = rain_fall.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/drop.png')
        self.image = pygame.transform.scale(self.image, (25, 35))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.drop_speed = 3.0

        self.y = float(self.rect.y)

    def _convert_image(self):
        self.image = pygame.image.load('images/splash.png')
        self.image = pygame.transform.scale(self.image, (65, 75))

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom

    def update(self):
        self.y += self.drop_speed
        self.rect.y = self.y
