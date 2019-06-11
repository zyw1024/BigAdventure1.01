import sound


class Treasure():
    def __init__(self, ai_settings, screen, target):
        self.ai_settings = ai_settings
        self.screen = screen
        self.target = target
        self.is_alive = True

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Ruby(Treasure):
    def update(self):
        if self.rect.colliderect(self.target):
            self.target.health += self.health_supply
            sound.ruby_sound(self.ai_settings)
            self.is_alive = False


class Sapphire(Treasure):
    def update(self):
        if self.rect.colliderect(self.target):
            self.target.energy += self.energy_supply
            sound.sapphire_sound(self.ai_settings)
            self.is_alive = False


class Ruby_raw(Ruby):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.ruby_raw_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.health_supply = self.ai_settings.ruby_raw_health_supply


class Ruby_round(Ruby):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.ruby_round_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.health_supply = self.ai_settings.ruby_round_health_supply


class Ruby_dragon(Ruby):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.ruby_dragon_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.health_supply = self.ai_settings.ruby_dragon_health_supply


class Sapphire_raw(Sapphire):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.sapphire_raw_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.energy_supply = self.ai_settings.sapphire_raw_energy_supply


class Sapphire_round(Sapphire):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.sapphire_round_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.energy_supply = self.ai_settings.sapphire_round_energy_supply


class Sapphire_dragon(Sapphire):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.sapphire_dragon_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.energy_supply = self.ai_settings.sapphire_dragon_energy_supply


class Coins(Treasure):
    def update(self):
        if self.rect.colliderect(self.target):
            if self.coins_num == self.ai_settings.some_coins_num:
                sound.some_coins_sound(self.ai_settings)
            elif self.coins_num == self.ai_settings.lots_of_coins_num:
                sound.lots_of_coins_sound(self.ai_settings)
            else:
                sound.massive_coins_sound(self.ai_settings)

            self.target.coins += self.coins_num
            self.is_alive = False


class Some_coins(Coins):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.some_coins_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.coins_num = self.ai_settings.some_coins_num


class Lots_of_coins(Coins):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.lots_of_coins_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.coins_num = self.ai_settings.lots_of_coins_num


class Massive_coins(Coins):
    def __init__(self, x, y, ai_settings, screen, target):
        super().__init__(ai_settings, screen, target)
        self.image = self.ai_settings.massive_coins_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.coins_num = self.ai_settings.massive_coins_num
