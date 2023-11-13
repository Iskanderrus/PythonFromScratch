import pygame
from settings import Settings
from pygame.sprite import Sprite


class Ship(Sprite):
    """ A class to manage the ship """

    def __init__(self, ai_game):
        super().__init__()
        """ Initialize the ship and set its staring position """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (self.settings.ship_height, self.settings.ship_width))
        self.image = pygame.transform.rotate(self.image, self.settings.ship_rotation)

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flag. Start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """ Center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """ Update the ship's position based on the movement flag """
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)