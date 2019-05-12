import pygame
import sys
import sound
import bullet as b
import game_functions as gf
# from game_functions import mouse_x, mouse_y
global tick
tick = 0


class Player():

    def __init__(self, ai_settings, screen, enemies):
        """Initialize the player"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.tick = -1
        self.is_alive = True
        self.health = self.ai_settings.player_health
        self.energy = self.ai_settings.player_energy
        self.normal_attack_consumption = self.ai_settings.player_normal_attack_consumption
        self.coins = 0
        # self.coins = 1000
        self.choice = -1
        self.atk = self.ai_settings.player_atk
        self.shoot_interval = self.ai_settings.player_shoot_interval
        self.enemies = enemies

        # Load the player image and get it's rect.
        self.image = ai_settings.player_left[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new player at the entrance to the maze.
        if self.ai_settings.startx == 0:
            self.rect.left = 0
        elif self.ai_settings.startx == ai_settings.maze_width - 1:
            self.rect.right = ai_settings.screen_width
        else:
            self.rect.centerx = self.ai_settings.startx * ai_settings.maze_block_width + (ai_settings.maze_block_width / 2)
        if self.ai_settings.starty == 0:
            self.rect.top = 0
        elif self.ai_settings.starty == ai_settings.maze_height - 1:
            self.rect.bottom = ai_settings.screen_height
        else:
            self.rect.centery = self.ai_settings.starty * ai_settings.maze_block_height + (ai_settings.maze_block_height / 2)

        # Store a decimal value for the player's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # print("self.centerx",type(self.centerx),self.centerx)

        # movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_down = False

        #mouse status
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_button_left = False
        self.mouse_button_right = False
        self.mouse_wheel = False


    def attack(self, bullets):
        source_atk = self.atk
        source_rect = self.rect
        bullet = b.RedBullet(source_rect, source_atk, self.enemies, self.mouse_x, self.mouse_y, self.ai_settings, self.screen)
        sound.player_normal_attack_sound(self.ai_settings)
        bullets.append(bullet)
        self.energy -= 1

    def coin_attack(self, bullets):
        if self.ai_settings.is_coin_attack_valid:
            source_atk = self.atk * 1.2
            source_rect = self.rect
            bullet = b.CoinBullet(source_rect, source_atk, self.enemies, self.mouse_x, self.mouse_y, self.ai_settings, self.screen)
            sound.player_coin_attack_sound(self.ai_settings)
            bullets.append(bullet)
            self.coins -= 1

    def skull_attack(self, bullets):
        if self.ai_settings.is_skull_attack_valid:
            source_atk = self.atk * 1.5
            source_rect = self.rect
            bullet = b.Skull_Bullet(source_rect, source_atk, self.enemies, self.mouse_x, self.mouse_y, self.ai_settings, self.screen)
            sound.player_skull_attack_sound(self.ai_settings)
            bullets.append(bullet)
            self.health -= 10

    def update(self, bullets):
        #Time update
        self.tick += 1
        #test
        # self.health = 3000

        # Check for End Game
        if self.rect.colliderect(self.ai_settings.end) and \
                (self.rect.left <= self.screen_rect.left or
                 self.rect.right >= self.screen_rect.right or \
                    self.rect.top <= self.screen_rect.top or
                 self.rect.bottom >= self.screen_rect.bottom ):
            self.ai_settings.gamedone = True
            self.ai_settings.player_pre_health = self.health
            self.ai_settings.player_pre_energy = self.energy
            self.ai_settings.player_pre_coins = self.coins

        #Update the player's position
        collidebottom, collidetop, collideright, collideleft, is_collide_wall = gf.collide_walls(self)
        # if (is_collide_wall):
        #     print("player collide the wall!")

        if self.is_alive:
            if self.moving_right and self.rect.right < self.screen_rect.right and collideright != 1:
                self.centerx += self.ai_settings.player_speed_factor
            if self.moving_left and self.rect.left > 0 and collideleft != 1:
                self.centerx -= self.ai_settings.player_speed_factor
            if self.moving_top and self.rect.top > self.screen_rect.top and collidetop != 1:
                self.centery -= self.ai_settings.player_speed_factor
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom and collidebottom != 1:
                self.centery += self.ai_settings.player_speed_factor

            # Update rect object from self.center.
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

            global tick
            tick += 1

            #Update  moving images
            if self.ai_settings.player_index >= (len(self.ai_settings.player_left) - 1):
                self.ai_settings.player_index = 0
            if self.mouse_x - self.centerx < 0:
                self.image = self.ai_settings.player_left[self.ai_settings.player_index]
            elif self.mouse_x - self.centerx > 0:
                self.image = self.ai_settings.player_right[self.ai_settings.player_index]
            if(tick % self.ai_settings.img_change_interval == 0):
                self.ai_settings.player_index += 1

            #Press mouse left button to attack
            if self.mouse_button_left:
                # self.attack(bullets)
                if self.energy >= self.normal_attack_consumption:
                    if self.tick % self.shoot_interval == 0:
                        self.attack(bullets)

            elif self.mouse_button_right:
                if self.coins >= 1:
                    if self.tick % self.shoot_interval == 0:
                        self.coin_attack(bullets)

            elif self.mouse_wheel:
                if self.health >= 0:
                    if self.tick % self.shoot_interval == 0:
                        self.skull_attack(bullets)

        #Player dead
        if self.health <= 0:
            #Update death images
            if self.ai_settings.player_death_index >= (len(self.ai_settings.player_death)):
                self.image = self.ai_settings.player_death[len(self.ai_settings.player_death) - 1]
                self.is_alive = False
            else:
                self.image = self.ai_settings.player_death[self.ai_settings.player_death_index]
            if tick % 10 == 0:
                self.ai_settings.player_death_index +=1

    def blitme(self):
        """Draw the player at it's current location."""
        self.screen.blit(self.image, self.rect)