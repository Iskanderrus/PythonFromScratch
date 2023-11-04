import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, star_screen):
        super().__init__()
        self.screen = star_screen.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/pngwing.com.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
