"""Game invasion"""
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Class for resources managment and a way for working game"""

    def __init__(self):
        """Initializing the game and opening its resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #container for statistic data and scoreboard class
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Creation of button "game"
        self.play_button = Button(self, msg = "Game")

    def run_game(self):
        """
        Starting the main loop
        """
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """reaction for generated presses from keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """start new game after press button game"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reset game settings
            self.settings.initalize_dynamic_settings()

            #reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #delete aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            #hide mouse
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self,event):
        """reaction for any press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """reaction for keyup"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creating new bullet and adding that bullet to new group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and deleting bullets that are off the screen"""
        self.bullets.update()

        #delete bullets that are off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Reaction for collision between bullet and alien"""
        #Check if bullet hitted alien, if yes - delete both
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #delete bullets and creating new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #changing game level
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Reaction for collision between alien and ship"""
        if self.stats.ships_left > 0 :
            #Reduce value saved in ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #delete content of list aliens and bullet
            self.aliens.empty()
            self.bullets.empty()

            #Creation of new fleet and centering ship
            self._create_fleet()
            self.ship.center_ship()

            #Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Checking if some aliens reached bottom edge of screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #the same like hitting ship
                self._ship_hit()
                break

    def _update_aliens(self):
        """Update position of all aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        #detecting collision between alien and ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #searching for aliens whose reached bottom edge of screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Creating an army of aliens"""
        #creating alien and setting alien count in a row
        #distance between each alien is equal to alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #finding how many rowf of alien, can be on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #creating an army of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """creating and alien and storing him in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """reaction when alien reach edge of screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Moving fleet down and changing direction of movement"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #screen refreshing during each loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #show scoreboard
        self.sb.show_score()

        #show button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    #activate the game
    ai = AlienInvasion()
    ai.run_game()
