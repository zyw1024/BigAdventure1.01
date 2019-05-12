import random
import pygame
import sound
import game_functions as gf


class Non_Player_Character():
    def __init__(self, ai_settings, screen, target):
        self.is_alive = True
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.target = target
        self.orig_borny, self.orig_bornx = self.ai_settings.npc_born_coordinate
        self.index = 0
        self.tick = -1
        # self.is_start_dialogue = False
        # self.text_surface = None
        # self.text_surface_rect = None
        self.text = []
        self.text_surface = []
        self.text_surface_rect = []
        self.text_index = 0
        self.is_dialogue_finished = False

    def speak(self):
        self.font = pygame.font.SysFont('arial', 36)

        # self.text_surface = self.font.render(self.name + ": " + self.text,
        #                                      False, (255, 0, 0))
        # self.text_surface_rect = self.text_surface.get_rect()
        # self.text_surface_rect.left = self.screen_rect.left + self.screen_rect.width / 2 - self.text_surface_rect.width / 2
        # self.text_surface_rect.top = self.screen_rect.top + self.screen_rect.height / 2 - self.text_surface_rect.height / 2

        self.text_surface.append(self.font.render(self.name + ": " + self.text[0], False, (255, 0, 0)))
        self.text_surface_rect.append(self.text_surface[0].get_rect())
        self.text_surface_rect[0].left = self.screen_rect.left + self.screen_rect.width / 2 - self.text_surface_rect[
            0].width / 2
        self.text_surface_rect[0].top = self.screen_rect.top + self.screen_rect.height / 2 - self.text_surface_rect[
            0].height / 2

    def speak_more(self):
        # self.font = pygame.font.SysFont('arial', 36)
        while self.text_index < len(self.text) - 1:
            self.text_index += 1
            self.text_surface.append(self.font.render(self.text[self.text_index], False, (255, 0, 0)))
            self.text_surface_rect.append(self.text_surface[self.text_index].get_rect())
            self.text_surface_rect[self.text_index].left = self.screen_rect.left + self.screen_rect.width / 2 - \
                                                           self.text_surface_rect[self.text_index].width / 2
            self.text_surface_rect[self.text_index].top = self.text_surface_rect[self.text_index - 1].top + \
                                                          self.text_surface_rect[self.text_index - 1].height

    def update(self):
        self.tick += 1
        if self.index >= len(self.ai_settings.fortune_cat_img) - 1:
            self.index = 0
        else:
            if self.tick % 10 == 0:
                self.index += 1
        self.image = self.images[self.index]

        # if self.rect.colliderect(self.target.rect):
        #     self.speak()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # if self.text_surface_rect != None:
        #     self.screen.blit(self.text_surface, self.text_surface_rect)
        for i in range(len(self.text_surface)):
            self.screen.blit(self.text_surface[i], self.text_surface_rect[i])


class Fortune_Cat(Non_Player_Character):
    def __init__(self, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.name = "Fortune Cat"
        self.text.append("Less money, greater power.[Try the right button]")
        self.text.append("Meow~")
        self.image = self.ai_settings.fortune_cat_img[0]
        self.images = self.ai_settings.fortune_cat_img
        self.width = self.ai_settings.fortune_cat_width
        self.height = self.ai_settings.fortune_cat_height
        self.adjusted_borny = random.uniform(self.orig_borny,
                                             (self.orig_borny + ai_settings.maze_block_width - self.width))
        self.adjusted_bornx = random.uniform(self.orig_bornx,
                                             (self.orig_bornx + ai_settings.maze_block_height - self.height))
        self.rect = pygame.Rect(self.adjusted_borny, self.adjusted_bornx, self.width,
                                self.height)
        self.is_dialogue_finished = False

    def update(self):
        super().update()
        if self.rect.colliderect(self.target.rect) and not self.is_dialogue_finished:
            self.speak()
            self.speak_more()
            sound.fortune_cat_sound(self.ai_settings)
            self.ai_settings.is_coin_attack_valid = True
            self.target.coins += 10
            self.is_dialogue_finished = True


class Death(Non_Player_Character):
    def __init__(self, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.name = "Death"
        self.text.append("Something for Nothing...[Try the mouse wheel]")
        self.text.append("Your soul smells good...")
        self.image = self.ai_settings.Death_img[0]
        self.images = self.ai_settings.Death_img
        self.width = self.ai_settings.Death_width
        self.height = self.ai_settings.Death_height
        self.adjusted_borny = random.uniform(self.orig_borny,
                                             (self.orig_borny + ai_settings.maze_block_width - self.width))
        self.adjusted_bornx = random.uniform(self.orig_bornx,
                                             (self.orig_bornx + ai_settings.maze_block_height - self.height))
        self.rect = pygame.Rect(self.adjusted_borny, self.adjusted_bornx, self.width,
                                self.height)

    def update(self):
        super().update()
        if self.rect.colliderect(self.target.rect) and not self.is_dialogue_finished:
            self.speak()
            self.speak_more()
            sound.Death_sound(self.ai_settings)
            sound.Death_sound(self.ai_settings)
            sound.Death_sound(self.ai_settings)
            self.ai_settings.is_skull_attack_valid = True
            self.is_dialogue_finished = True


class Little_Girl(Non_Player_Character):
    def __init__(self, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.name = "Little Girl"
        self.text.append("What can I do for you? ")
        self.text.append("1.HP 250 ($50)")
        self.text.append("2.HP 550 ($100)")
        self.text.append("3.MP 150 ($50)")
        self.text.append("4.MP 330 ($100)")
        self.image = self.ai_settings.little_girl_img[0]
        self.images = self.ai_settings.little_girl_img
        self.width = self.ai_settings.little_girl_width
        self.height = self.ai_settings.little_girl_height
        self.adjusted_borny = random.uniform(self.orig_borny,
                                             (self.orig_borny + ai_settings.maze_block_width - self.width))
        self.adjusted_bornx = random.uniform(self.orig_bornx,
                                             (self.orig_bornx + ai_settings.maze_block_height - self.height))
        self.rect = pygame.Rect(self.adjusted_borny, self.adjusted_bornx, self.width,
                                self.height)

    def deal(self):
        if self.target.choice == 1 and self.target.coins >= 50:
            self.target.health += self.ai_settings.HP_50coins
            self.target.coins -= 50
            sound.deal_done_sound(self.ai_settings)


        elif self.target.choice == 2 and self.target.coins >= 100:
            self.target.health += self.ai_settings.HP_100coins
            self.target.coins -= 100
            sound.deal_done_sound(self.ai_settings)


        elif self.target.choice == 3 and self.target.coins >= 50:
            self.target.energy += self.ai_settings.MP_50coins
            self.target.coins -= 50
            sound.deal_done_sound(self.ai_settings)


        elif self.target.choice == 4 and self.target.coins >= 100:
            self.target.energy += self.ai_settings.MP_100coins
            self.target.coins -= 100
            sound.deal_done_sound(self.ai_settings)

        self.target.choice = -1

    def update(self):
        super().update()
        if self.rect.colliderect(self.target.rect) and not self.is_dialogue_finished:
            self.speak()
            self.speak_more()
            sound.welcome_sound(self.ai_settings)
            self.is_dialogue_finished = True

        if self.is_dialogue_finished:
            self.deal()



def create_npc(ai_settings, screen, target):
    if ai_settings.level == 1:
        npc = Fortune_Cat(ai_settings, screen, target)
    elif ai_settings.level == 2:
        npc = Death(ai_settings, screen, target)
    elif ai_settings.level == 3:
        npc = Little_Girl(ai_settings, screen, target)
        # npc = Fortune_Cat(ai_settings, screen, target)
    else:
        return
    return npc

# def text_in_center(speaker, text, screen, screen_rect):
#     print("Text!")
#     font = pygame.font.SysFont('arial', 36)
#     text_surface = font.render(speaker + ": " + text,
#                                     False, (255, 0, 0))
#     text_surface_rect = text_surface.get_rect()
#     text_surface_rect.left = screen_rect.left + screen_rect.width / 2 - text_surface_rect.width / 2
#     text_surface_rect.top = screen_rect.top + screen_rect.height / 2 - text_surface_rect.height / 2
#     screen.blit(text_surface, text_surface_rect)
#     pygame.display.flip()
