import random
import pygame
import math
import bullet as b
import game_functions as gf
import probe as p
import treasure as ts
import numpy as np

global tick
tick = -1


# global bullets
# bullets = []


class Monster():
    def __init__(self, target, ai_settings, screen, probes, treasures):
        self.is_alive = True
        self.tick = -1
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.orig_borny, self.orig_bornx = ai_settings.monster_born_coordinate[-1]

        self.img_index = 0
        self.boom_img_index = 0

        self.lower_threshold = self.ai_settings.lower_threshold
        self.discover_prt = self.ai_settings.discover_prt
        self.target = target
        self.is_move_to_target = False

        self.rest_time = self.ai_settings.rest_time

        self.treasures = treasures

    def attack(self, target, bullets):
        source_atk = self.atk
        source_rect = self.rect
        if self.rank == 1:
            bullet = b.BlueBullet(source_rect, source_atk, target, self.ai_settings, self.screen)
        elif self.rank == 2:
            bullet = b.Fireball(source_rect, source_atk, target, self.ai_settings, self.screen)
        elif self.rank == 3:
            bullet = b.Lightning_ball(source_rect, source_atk, target, self.ai_settings, self.screen)
        elif self.rank == 4:
            bullet = b.Black_fireball(source_rect, source_atk, target, self.ai_settings, self.screen)

        bullets.append(bullet)

    def detect(self, target, probes):
        # The new probe should be created after the last one "dead"
        if not self.probe.is_alive:
            self.probe = p.Probe(target, self.rect, self.ai_settings, self.screen)
            probes.append(self.probe)
            # print("probe append:", self.probe)
            # print("detecting...")

    def stop(self):
        while self.tick % self.rest_time <= self.rest_time * random.randint(1, 4) / 10:
            self.x_speed = 0
            self.y_speed = 0
            self.tick += 1

    def patrol(self):
        # Position
        self.x_speed_positive = random.uniform(self.speed / 2, + self.speed * math.sqrt(2) / 2)
        self.y_speed_positive = random.uniform(self.speed / 2, + self.speed * math.sqrt(2) / 2)
        self.x_speed_negative = random.uniform(-self.speed * math.sqrt(2) / 2, -self.speed / 2)
        self.y_speed_negative = random.uniform(-self.speed * math.sqrt(2) / 2, -self.speed / 2)

        if self.is_collide_wall:
            if self.collidetop == 1:
                self.y_speed = self.y_speed_positive + 0.5
            if self.collidebottom == 1:
                self.y_speed = self.y_speed_negative + 0.5
            if self.collideright == 1:
                # self.x_speed = self.x_speed_negative + 0.5
                self.x_speed = self.x_speed_negative - 0.5
            if self.collideleft == 1:
                self.x_speed = self.x_speed_positive + 0.5

        # When mnonster out of screen, adjust
        if self.centerx <= self.screen_rect.left:
            self.x_speed = self.x_speed_positive + 0.5
        if self.centerx >= self.screen_rect.right:
            self.x_speed = self.x_speed_negative - 0.5
        if self.centery <= self.screen_rect.top:
            self.y_speed = self.y_speed_positive + 0.5
        elif self.centery >= self.screen_rect.bottom:
            self.y_speed = self.y_speed_negative - 0.5



        # Change the direction
        else:
            if self.tick % 55 == 0:
                if random.randint(1, 100) >= 49:
                    self.x_speed = self.x_speed_positive
                else:
                    self.x_speed = self.x_speed_negative
                if random.randint(1, 100) >= 49:
                    self.y_speed = self.y_speed_positive
                else:
                    self.y_speed = self.y_speed_negative

    def move_to_target(self, target):
        # If collide wall then change the direction
        if self.is_collide_wall:
            self.x_speed_positive = random.uniform(self.speed / 2, + self.speed * math.sqrt(2) / 2)
            self.y_speed_positive = random.uniform(self.speed / 2, + self.speed * math.sqrt(2) / 2)
            self.x_speed_negative = random.uniform(-self.speed * math.sqrt(2) / 2, -self.speed / 2)
            self.y_speed_negative = random.uniform(-self.speed * math.sqrt(2) / 2, -self.speed / 2)
            if self.collidetop == 1:
                self.y_speed = self.y_speed_positive + 0.5
            if self.collidebottom == 1:
                self.y_speed = self.y_speed_negative + 0.5
            if self.collideright == 1:
                self.x_speed = self.x_speed_negative + 0.5
            if self.collideleft == 1:
                self.x_speed = self.x_speed_positive + 0.5
            return

        if self.tick % 100 >= 55:
            # print("Patrol when moving to target")
            self.patrol()
            return

        len_x = self.target.rect.centerx - self.centerx
        len_y = self.target.rect.centery - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)

        times = s / self.speed
        if s >= self.atk_distance:
            self.is_target_within_range = False
            if times == 0:
                times = 1
            self.x_speed = len_x / times
            self.y_speed = len_y / times

        else:
            self.is_target_within_range = True
            self.patrol()

    def update(self, target, bullets, probes):
        # Time update
        global tick
        tick += 1
        self.tick += 1

        if self.health <= 0:
            # Update death images
            self.image = self.boom_image[self.boom_img_index]
            if self.boom_img_index >= (len(self.ai_settings.skeleton_soldier_boom) - 1):
                self.image = self.ai_settings.skeleton_soldier_boom[len(self.ai_settings.skeleton_soldier_boom) - 1]
                self.is_alive = False
                self.drop_treasure()

            if self.tick % 7 == 0:
                self.boom_img_index += 1


        else:
            self.is_target_within_range = False

            # Update the collision status between monster and walls
            self.collidebottom, self.collidetop, self.collideright, self.collideleft, self.is_collide_wall = gf.collide_walls(
                self)

            # Store the position using two decimal numbers
            self.centerx = float(self.rect.centerx)
            self.centery = float(self.rect.centery)
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

            # Detect the target
            if self.tick % self.discover_prt == 0:
                self.detect(target, probes)
            if self.probe.is_collide_wall or self.probe.is_out_of_screen:
                self.is_move_to_target = False
                self.probe.is_alive = False
            elif self.probe.is_target_found:
                self.is_move_to_target = True
                self.probe.is_alive = False

            # Choose the action depending on the result of detection
            if self.is_move_to_target:
                # print("I should move to my target.")
                self.move_to_target(target)
            else:
                # print("Target missed. Patrolling...")
                self.patrol()
                if self.tick % 101 == 0:
                    self.stop()

            # Update the new positions
            self.centerx += self.x_speed
            self.centery += self.y_speed
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

            if self.is_target_within_range:
                # if tick % self.ATKPRT < self.lower_threshold:
                if self.tick % self.ATKPRT < self.lower_threshold:
                    self.attack(target, bullets)

            # Update moving images
            if not self.is_move_to_target:
                if self.x_speed > 0:
                    self.image = self.image_right[self.img_index]
                else:
                    self.image = self.image_left[self.img_index]
            # face to the target when moving to it
            else:
                if self.rect.centerx > target.rect.centerx:
                    self.image = self.image_left[self.img_index]
                else:
                    self.image = self.image_right[self.img_index]
            # update image index
            if self.tick % self.ai_settings.img_change_interval == 0:
                self.img_index += 1
            if self.img_index > (len(self.image_left) - 1):
                self.img_index = 0

    def drop_treasure(self):
        if self.rank == 1:
            p_drop_rarity1 = self.ai_settings.p_drop_rank1 * self.ai_settings.p_drop_rarity1_under_rank1
            p_drop_rarity2 = self.ai_settings.p_drop_rank1 * self.ai_settings.p_drop_rarity2_under_rank1
            p_drop_rarity3 = self.ai_settings.p_drop_rank1 * self.ai_settings.p_drop_rarity3_under_rank1

        elif self.rank == 2:
            p_drop_rarity1 = self.ai_settings.p_drop_rank2 * self.ai_settings.p_drop_rarity1_under_rank2
            p_drop_rarity2 = self.ai_settings.p_drop_rank2 * self.ai_settings.p_drop_rarity2_under_rank2
            p_drop_rarity3 = self.ai_settings.p_drop_rank2 * self.ai_settings.p_drop_rarity3_under_rank2

        elif self.rank == 3:
            p_drop_rarity1 = self.ai_settings.p_drop_rank3 * self.ai_settings.p_drop_rarity1_under_rank3
            p_drop_rarity2 = self.ai_settings.p_drop_rank3 * self.ai_settings.p_drop_rarity2_under_rank3
            p_drop_rarity3 = self.ai_settings.p_drop_rank3 * self.ai_settings.p_drop_rarity3_under_rank3

        elif self.rank == 4:
            p_drop_rarity1 = self.ai_settings.p_drop_rank4 * self.ai_settings.p_drop_rarity1_under_rank4
            p_drop_rarity2 = self.ai_settings.p_drop_rank4 * self.ai_settings.p_drop_rarity2_under_rank4
            p_drop_rarity3 = self.ai_settings.p_drop_rank4 * self.ai_settings.p_drop_rarity3_under_rank4

        p_drop_none = 1 - p_drop_rarity1 - p_drop_rarity2 - p_drop_rarity3
        p1 = np.array([self.ai_settings.p_drop_red, self.ai_settings.p_drop_blue, self.ai_settings.p_drop_coins])
        p2 = np.array([p_drop_rarity1, p_drop_rarity2, p_drop_rarity3, p_drop_none])
        final_drop_kind = np.random.choice(['red', 'blue','coins'], p=p1.ravel())
        final_drop_rarity = np.random.choice([1, 2, 3, -1], p=p2.ravel())

        if final_drop_rarity != -1:
            if final_drop_kind == 'red':
                if final_drop_rarity == 1:
                    treasure = ts.Ruby_raw(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                           self.target)
                elif final_drop_rarity == 2:
                    treasure = ts.Ruby_round(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                             self.target)
                elif final_drop_rarity == 3:
                    treasure = ts.Ruby_dragon(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                              self.target)

            if final_drop_kind == 'blue':
                if final_drop_rarity == 1:
                    treasure = ts.Sapphire_raw(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                               self.target)
                elif final_drop_rarity == 2:
                    treasure = ts.Sapphire_round(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                                 self.target)
                elif final_drop_rarity == 3:
                    treasure = ts.Sapphire_dragon(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                                  self.target)

            if final_drop_kind == 'coins':
                if final_drop_rarity == 1:
                    treasure = ts.Some_coins(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                               self.target)
                if final_drop_rarity == 2:
                    treasure = ts.Lots_of_coins(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                             self.target)
                if final_drop_rarity == 3:
                    treasure = ts.Massive_coins(self.rect.centerx, self.rect.centery, self.ai_settings, self.screen,
                                             self.target)


            # if final_drop_rarity != -1:
            #     self.treasures.append(treasure)
            self.treasures.append(treasure)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Skeleton_soldier(Monster):
    def __init__(self, target, ai_settings, screen, probes, treasures):
        super().__init__(target, ai_settings, screen, probes, treasures)

        self.rank = self.ai_settings.skeleton_soldier_rank

        self.image = self.ai_settings.skeleton_soldier_left[0]
        self.image_left = self.ai_settings.skeleton_soldier_left
        self.image_right = self.ai_settings.skeleton_soldier_right
        self.boom_image = self.ai_settings.skeleton_soldier_boom

        self.width = self.ai_settings.skeleton_soldier_width
        self.height = self.ai_settings.skeleton_soldier_height

        self.adjusted_borny = random.uniform(self.orig_borny,
                                             (self.orig_borny + ai_settings.maze_block_width - self.width))
        self.adjusted_bornx = random.uniform(self.orig_bornx,
                                             (self.orig_bornx + ai_settings.maze_block_height - self.height))

        self.rect = pygame.Rect(self.adjusted_borny, self.adjusted_bornx, self.ai_settings.skeleton_soldier_width,
                                self.ai_settings.skeleton_soldier_height)

        self.health = self.ai_settings.skeleton_soldier_health
        self.speed = ai_settings.skeleton_soldier_speed_factor
        self.atk_distance = self.ai_settings.skeleton_soldier_atk_distance
        self.atk = self.ai_settings.skeleton_soldier_atk
        self.ATKPRT = self.ai_settings.skeleton_soldier_ATKPRBT * float(random.uniform(0.5, 1.5)) + random.randint(0,
                                                                                                                   10)

        # Create the first probe of this monster
        self.probe = p.Probe(self.target, self.rect, self.ai_settings, self.screen)
        probes.append(self.probe)
        self.x_speed = 0
        self.y_speed = 0
        self.is_target_within_range = False


class Unicorn(Monster):
    def __init__(self, target, ai_settings, screen, probes, treasures):
        super().__init__(target, ai_settings, screen, probes, treasures)

        self.rank = self.ai_settings.unicorn_rank

        self.image = self.ai_settings.unicorn_left[0]
        self.image_left = self.ai_settings.unicorn_left
        self.image_right = self.ai_settings.unicorn_right
        self.boom_image = self.ai_settings.unicorn_boom

        self.width = self.ai_settings.unicorn_width
        self.height = self.ai_settings.unicorn_height

        self.adjusted_borny = random.uniform(self.orig_borny,
                                             (self.orig_borny + ai_settings.maze_block_width - self.width))
        self.adjusted_bornx = random.uniform(self.orig_bornx,
                                             (self.orig_bornx + ai_settings.maze_block_height - self.height))

        self.rect = pygame.Rect(self.adjusted_borny, self.adjusted_bornx, self.ai_settings.unicorn_width,
                                self.ai_settings.unicorn_height)

        self.health = self.ai_settings.unicorn_health
        self.speed = ai_settings.unicorn_speed_factor
        self.atk_distance = self.ai_settings.unicorn_atk_distance
        self.atk = self.ai_settings.unicorn_atk
        self.ATKPRT = self.ai_settings.unicorn_ATKPRBT * float(random.uniform(0.5, 1.5))

        # Create the first probe of this monster
        self.probe = p.Probe(self.target, self.rect, self.ai_settings, self.screen)
        probes.append(self.probe)
        self.x_speed = 0
        self.y_speed = 0
        self.is_target_within_range = False


class Blue_dragon(Monster):
    def __init__(self, target, ai_settings, screen, probes, treasures):
        super().__init__(target, ai_settings, screen, probes, treasures)

        self.rank = self.ai_settings.blue_dragon_rank

        self.image = self.ai_settings.blue_dragon_left[0]
        self.image_left = self.ai_settings.blue_dragon_left
        self.image_right = self.ai_settings.blue_dragon_right
        self.boom_image = self.ai_settings.blue_dragon_boom

        self.width = self.ai_settings.blue_dragon_width
        self.height = self.ai_settings.blue_dragon_height

        self.adjusted_borny = random.uniform(self.orig_borny,
                                             (self.orig_borny + ai_settings.maze_block_width - self.width))
        self.adjusted_bornx = random.uniform(self.orig_bornx,
                                             (self.orig_bornx + ai_settings.maze_block_height - self.height))

        self.rect = pygame.Rect(self.adjusted_borny, self.adjusted_bornx, self.ai_settings.blue_dragon_width,
                                self.ai_settings.blue_dragon_height)

        self.health = self.ai_settings.blue_dragon_health
        self.speed = ai_settings.blue_dragon_speed_factor
        self.atk_distance = self.ai_settings.blue_dragon_atk_distance
        self.atk = self.ai_settings.blue_dragon_atk
        self.ATKPRT = self.ai_settings.blue_dragon_ATKPRBT * float(random.uniform(0.5, 1.5))

        # Create the first probe of this monster
        self.probe = p.Probe(self.target, self.rect, self.ai_settings, self.screen)
        probes.append(self.probe)
        self.x_speed = 0
        self.y_speed = 0
        self.is_target_within_range = False


class Black_dragon(Monster):
    def __init__(self, target, ai_settings, screen, probes, treasures):
        super().__init__(target, ai_settings, screen, probes, treasures)

        self.rank = self.ai_settings.black_dragon_rank

        self.image = self.ai_settings.black_dragon_left[0]
        self.image_left = self.ai_settings.black_dragon_left
        self.image_right = self.ai_settings.black_dragon_right
        self.boom_image = self.ai_settings.black_dragon_boom

        self.width = self.ai_settings.black_dragon_width
        self.height = self.ai_settings.black_dragon_height

        self.adjusted_borny = random.uniform(self.orig_borny,
                                             (self.orig_borny + ai_settings.maze_block_width - self.width))
        self.adjusted_bornx = random.uniform(self.orig_bornx,
                                             (self.orig_bornx + ai_settings.maze_block_height - self.height))

        self.rect = pygame.Rect(self.adjusted_borny, self.adjusted_bornx, self.ai_settings.black_dragon_width,
                                self.ai_settings.black_dragon_height)

        self.health = self.ai_settings.black_dragon_health
        self.speed = ai_settings.black_dragon_speed_factor
        self.atk_distance = self.ai_settings.black_dragon_atk_distance
        self.atk = self.ai_settings.black_dragon_atk
        self.ATKPRT = self.ai_settings.black_dragon_ATKPRBT * float(random.uniform(0.5, 1.5))

        # Create the first probe of this monster
        self.probe = p.Probe(self.target, self.rect, self.ai_settings, self.screen)
        probes.append(self.probe)
        self.x_speed = 0
        self.y_speed = 0
        self.is_target_within_range = False


def create_monster(ai_settings, screen, target, probes, treasures):
    p = np.array([ai_settings.skeleton_soldier_possibility,
                  ai_settings.unicorn_possibility,
                  ai_settings.blue_dragon_possibility,
                  ai_settings.black_dragon_possibility])
    index = np.random.choice([0, 1, 2, 3], p=p.ravel())

    if index == 0:
        monster = Skeleton_soldier(target, ai_settings, screen, probes, treasures)
    elif index == 1:
        monster = Unicorn(target, ai_settings, screen, probes, treasures)
    elif index == 2:
        monster = Blue_dragon(target, ai_settings, screen, probes, treasures)
    else:
        monster = Black_dragon(target, ai_settings, screen, probes, treasures)
    return monster
