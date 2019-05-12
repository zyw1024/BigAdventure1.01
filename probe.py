import math
import pygame
import game_functions as gf


class Probe():
    def __init__(self, target, source_rect, ai_settings, screen):
        self.is_alive = True
        self.speed = ai_settings.probe_speed_factor
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.image = self.ai_settings.redbullet_img
        self.rect = self.image.get_rect()

        # Store the position using two decimal numbers
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)

        # Initialize the rect position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        # print(type(target))
        # print("target:", target)
        len_x = target.rect.centerx - self.centerx
        len_y = target.rect.centery - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        if times == 0:
            times = 1
        self.x_speed = len_x / times
        self.y_speed = len_y / times

        self.is_target_found = False
        self.is_collide_wall = False
        self.is_out_of_screen = False

    def detect(self, target, probes):
        skip = 0
        for i in range(0, len(self.ai_settings.walls)):
            if self.rect.colliderect(self.ai_settings.walls[i].rect):
                self.is_collide_wall = True
                skip = 1
                break
                # print("Probe collide wall!")

        if skip == 0:
            if self.rect.centerx < self.screen_rect.left or self.rect.centerx > self.screen_rect.right or \
                    self.rect.centery < self.screen_rect.top or self.centery > self.screen_rect.bottom:
                self.is_out_of_screen = True
                skip = 1
                # print("Probe out of screen!")

        if skip == 0 and self.rect.colliderect(target.rect):
            self.is_target_found = True
            # print("Probe collide player!")

    def update(self, target, probes):
        # is_collide_wall = False
        # is_out_of_screen = False
        # is_target_found = False
        # is_collide_wall = self.is_collide_wall
        # is_out_of_screen = self.is_out_of_screen
        # is_target_found = self.is_target_found4
        if self.is_alive:
            self.detect(target, probes)
            # Update the bullet's position
            self.centerx += self.x_speed
            self.centery += self.y_speed
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery



    def blitme(self):
        self.screen.blit(self.image, self.rect)
