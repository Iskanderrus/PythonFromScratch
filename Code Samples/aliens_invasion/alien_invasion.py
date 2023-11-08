import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """ Initialize the game and create game resources. """

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Adding full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height - 70
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Create an instance to store current game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in active state
        self.game_active = False

        # Make the Play button
        self.level_1_button = Button(self, "Level 1", center_deviation_x=-300)
        self.level_2_button = Button(self, "Level 2")
        self.level_3_button = Button(self, "Level 3", center_deviation_x=300)
        # self.play_button = Button(self, "Play")

    def _select_level_buttons(self, mouse_pos):
        if not self.game_active:
            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Center the ship
            self.ship.center_ship()

            if self.level_1_button.rect.collidepoint(mouse_pos):
                self._create_fleet()
                self.game_active = True
                # Hide the mouse cursor
                pygame.mouse.set_visible(False)

            elif self.level_2_button.rect.collidepoint(mouse_pos):
                # level 2 settings applied
                self.settings.increase_speed()
                self.settings.alien_height *= 0.95
                self.settings.alien_width *= 0.95
                self.settings.bullets_allowed += 2
                self._create_fleet()
                self.game_active = True
                # Hide the mouse cursor
                pygame.mouse.set_visible(False)

            elif self.level_3_button.rect.collidepoint(mouse_pos):
                # level 3 settings applied
                self.settings.increase_speed()
                self.settings.increase_speed()
                self.settings.alien_height *= 0.925
                self.settings.alien_width *= 0.925
                self.settings.bullets_allowed += 3
                self._create_fleet()
                self.game_active = True
                # Hide the mouse cursor
                pygame.mouse.set_visible(False)

    # def _check_play_button(self, mouse_pos):
    #     """ Start a new game when the player clicks Play """
    #     button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    #     if button_clicked and not self.game_active:
    #         # Reset the game statistics
    #         self.settings.initialize_dynamic_settings()
    #         self.game_active = True
    #
    #         # Get rid of any remaining bullets and aliens
    #         self.bullets.empty()
    #         self.aliens.empty()
    #
    #         # Create a new fleet and center the ship
    #         self._create_fleet()
    #         self.ship.center_ship()
    #
    #         # Hide the mouse cursor
    #         pygame.mouse.set_visible(False)

    def _check_aliens_bottom(self):
        """ Check if any alien reached the bottom of the screen """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if ship got hit
                self._ship_hit()
                break

    def _ship_hit(self):
        """ Respond to the ship being hit by an alien """
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """ Create the fleet of the aliens """
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 5 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 3 * alien_height

    def _create_alien(self, x_position, y_position):
        """ Create an alien and place it in the row """
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_fleet_edges(self):
        """ Respond appropriately if any of the aliens have reached an edge """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Drop the entire fleet and change the fleet's direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """ Update the position of all aliens in the fleet """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _update_bullets(self):
        """ Updates position of the bullets and get rid of old bullets """
        self.bullets.update()

        # Get rid of all bullets that disappeared behind the screen

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        # Check for any bullets that have hit aliens
        # If so, get rid of both alien and bullet
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_screen(self):
        """ Redraw the screen during each pass through the loop """
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive
        if not self.game_active:
            # self.play_button.draw_button()
            self.level_1_button.draw_button()
            self.level_2_button.draw_button()
            self.level_3_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_events(self):
        """ Track keyboard and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_pos = pygame.mouse.get_pos()
            #     self._check_play_button(mouse_pos)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._select_level_buttons(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # Action if a key is hit
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Action if a key is released
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypress """
        if event.key == pygame.K_p:
            self.game_active = True
            pygame.mouse.set_visible(False)
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ Respond to key releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
