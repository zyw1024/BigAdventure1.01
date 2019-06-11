import random

import pygame


class BGM():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        pygame.mixer.music.load(self.ai_settings.bgm[0])
        pygame.mixer.music.set_volume(0.3)
        self.index = 0

    def update(self):
        pygame.mixer.music.fadeout(3500)
        if self.index < len(self.ai_settings.bgm) - 1:
            self.index += 1
        else:
            self.index = 0
        pygame.mixer.music.load(self.ai_settings.bgm[self.index])

    def play(self):
        pygame.mixer.music.play(loops=-1)
        pass


def victory_sound(ai_settings):
    victory_sound = ai_settings.victory_sound
    # victory_sound.set_volume(1)
    victory_sound.play()


def defeat_sound(ai_settings):
    defeat_sound = ai_settings.defeat_sound[0]
    defeat_sound.set_volume(0.4)
    defeat_sound.play(loops=0)
    print("defeat sound")


def ruby_sound(ai_settings):
    ruby_sound = ai_settings.ruby_sound
    ruby_sound.set_volume(1)
    ruby_sound.play()


def sapphire_sound(ai_settings):
    sapphire_sound = ai_settings.sapphire_sound
    sapphire_sound.set_volume(1)
    sapphire_sound.play()


def player_normal_attack_sound(ai_settings):
    player_normal_attack_sound = ai_settings.player_normal_attack_sound
    player_normal_attack_sound.play()


def player_coin_attack_sound(ai_settings):
    player_coin_attack_sound = ai_settings.player_coin_attack_sound
    player_coin_attack_sound.set_volume(1.0)
    player_coin_attack_sound.play()


def player_skull_attack_sound(ai_settings):
    player_skull_attack_sound = ai_settings.player_skull_attack_sound
    player_skull_attack_sound.set_volume(1.0)
    player_skull_attack_sound.play()


def some_coins_sound(ai_settings):
    some_coins_sound = ai_settings.some_coins_sound
    some_coins_sound.set_volume(0.5)
    some_coins_sound.play()


def lots_of_coins_sound(ai_settings):
    lots_of_coins_sound = ai_settings.lots_of_coins_sound
    lots_of_coins_sound.set_volume(1.5)
    lots_of_coins_sound.play()


def massive_coins_sound(ai_settings):
    massive_coins_sound = ai_settings.massive_coins_sound
    massive_coins_sound.set_volume(1.5)
    massive_coins_sound.play()


def Death_sound(ai_settings):
    Death_sound = ai_settings.Death_sound
    Death_sound.set_volume(1.0)
    Death_sound.play()


def fortune_cat_sound(ai_settings):
    fortune_cat_sound = ai_settings.fortune_cat_sound
    fortune_cat_sound.set_volume(1.0)
    fortune_cat_sound.play()


def welcome_sound(ai_settings):
    if random.randint(1, 2) == 1:
        welcome_sound = ai_settings.welcome_sound_normal
    else:
        welcome_sound = ai_settings.welcome_sound_happy
    welcome_sound.set_volume(1)
    welcome_sound.play()


def deal_done_sound(ai_settings):
    deal_done_sound = ai_settings.deal_done_sound
    deal_done_sound.set_volume(1.0)
    deal_done_sound.play()


def player_minor_wound_sound(ai_settings):
    # index = random.randint(0, len(ai_settings.player_minor_wound_sound) - 1)
    # player_minor_wound_sound = ai_settings.player_minor_wound_sound[index]
    # player_minor_wound_sound.set_volume(1.0)
    # player_minor_wound_sound.play()
    index = random.randint(0, len(ai_settings.player_middle_wound_sound) - 1)
    player_middle_wound_sound = ai_settings.player_middle_wound_sound[index]
    player_middle_wound_sound.set_volume(1.0)
    player_middle_wound_sound.play()


def player_middle_wound_sound(ai_settings):
    index = random.randint(0, len(ai_settings.player_middle_wound_sound) - 1)
    player_middle_wound_sound = ai_settings.player_middle_wound_sound[index]
    player_middle_wound_sound.set_volume(1.0)
    player_middle_wound_sound.play()


def player_severe_wound_sound(ai_settings):
    index = random.randint(0, len(ai_settings.player_severe_wound_sound) - 1)
    player_severe_wound_sound = ai_settings.player_severe_wound_sound[index]
    player_severe_wound_sound.set_volume(1.0)
    player_severe_wound_sound.play()
