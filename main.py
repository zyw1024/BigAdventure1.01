import sys

import non_player_character
import sound
from monster import *
from player import Player
from settings import Settings

print("Hello from Yiwen Zhang")


def run_game():
    GAME_OVER = False
    WIN = False
    # Initialize pygame, settings and create screen object.
    pygame.init()
    pygame.font.init()
    ai_settings = Settings()

    bgm = sound.BGM(ai_settings)
    bgm.play()
    # screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen_rect = screen.get_rect()
    # screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("BigAdventure - Level " + str(ai_settings.level))

    # Initialize bullets list
    bullets = []

    # Initialize monsters
    monsters = []

    # Create a Player.
    player = Player(ai_settings, screen, monsters)

    # Initialize probes
    probes = []

    # Initialize treasures
    treasures = []

    # Initialize npc
    npc = None

    # Create monsters
    for i in range(len(ai_settings.monster_born_coordinate)):
        monsters.append(create_monster(ai_settings, screen, player, probes, treasures))
        ai_settings.monster_born_coordinate.pop()

    # Start main loop for the game.
    while True:
        if player.is_alive == False:
            GAME_OVER = True
            pygame.mixer.music.fadeout(1000)
            sound.defeat_sound(ai_settings)

        if ai_settings.gamedone:
            ai_settings.gamedone = False
            ai_settings.level += 1
            sound.victory_sound(ai_settings)
            if ai_settings.level == 5:
                WIN = True
            pygame.display.set_caption("BigAdventrue - Level " + str(ai_settings.level))
            ai_settings.loadnewsettings()
            bgm.update()
            bgm.play()

            monsters = []
            npc = None
            player = None
            player = Player(ai_settings, screen, monsters)
            player.health = ai_settings.player_pre_health
            player.energy = ai_settings.player_pre_energy + ai_settings.mission_complete_energy_bonus
            player.coins = ai_settings.player_pre_coins
            probes = []
            treasures = []

            # create monsters
            for i in range(len(ai_settings.monster_born_coordinate)):
                monsters.append(create_monster(ai_settings, screen, player, probes, treasures))
                ai_settings.monster_born_coordinate.pop()

        #Check player's events and check whether there is a need to restart
        if gf.check_events(player):
            run_game()

        if not GAME_OVER and not WIN:
            # Update all elements from here
            if player.is_alive:
                player.update(bullets)
            for monster in monsters:
                if monster.is_alive:
                    monster.update(player, bullets, probes)
                else:
                    monsters.remove(monster)

            # create npcs
            if len(monsters) == 0 and npc == None:
                npc = non_player_character.create_npc(ai_settings, screen, player)

            if npc != None:
                npc.update()

            for bullet in bullets:
                if bullet.is_alive:
                    bullet.update()
                else:
                    bullets.remove(bullet)
            for probe in probes:
                if probe.is_alive:
                    probe.update(player, probes)
                else:
                    probes.remove(probe)

            for treasure in treasures:
                if treasure.is_alive:
                    treasure.update()
                else:
                    treasures.remove(treasure)

            gf.blit_all(ai_settings, screen, player, monsters, bullets, probes, treasures, npc)

            # font = pygame.font.Font(None, 50)
            fontObj = pygame.font.SysFont('arial', 36)
            textSurfaceObj1 = fontObj.render("HP " + str(player.health),
                                             False, (255, 0, 0))
            textRectObj1 = textSurfaceObj1.get_rect()
            textRectObj1.left = screen_rect.left
            textRectObj1.top = screen_rect.top

            textSurfaceObj2 = fontObj.render("MP " + str(player.energy),
                                             False, (255, 0, 0))
            textRectObj2 = textSurfaceObj2.get_rect()
            textRectObj2.left = screen_rect.left
            textRectObj2.top = screen_rect.top + textRectObj1.height

            textSurfaceObj3 = fontObj.render("Coins " + str(player.coins),
                                             False, (255, 0, 0))
            textRectObj3 = textSurfaceObj3.get_rect()
            textRectObj3.left = screen_rect.left
            textRectObj3.top = screen_rect.top + textRectObj1.height * 2

            # textSurfaceObj4 = fontObj.render("Monsters num" + str(len(monsters)),
            #                                  False, (255, 0, 0))
            # textRectObj4 = textSurfaceObj4.get_rect()
            # textRectObj4.left = screen_rect.left
            # textRectObj4.top = screen_rect.top + textRectObj1.height * 3

            screen.blit(textSurfaceObj1, textRectObj1)
            screen.blit(textSurfaceObj2, textRectObj2)
            screen.blit(textSurfaceObj3, textRectObj3)
            # screen.blit(textSurfaceObj4, textRectObj4)

        elif WIN:
            # font = pygame.font.Font(None, 80)
            fontObj = pygame.font.SysFont('arial', 36)
            textSurfaceObj = fontObj.render("You Win!" + "R to restart, Q to quit",
                                            False, (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.left = screen_rect.left + screen_rect.width / 2 - textRectObj.width / 2
            textRectObj.top = screen_rect.top + screen_rect.height / 2 - textRectObj.height / 2
            screen.blit(textSurfaceObj, textRectObj)
            is_restart, is_quit = gf.check_game_control_event()
            if is_restart:
                run_game()
            if is_quit:
                pygame.quit()
        # else:
        #     # font = pygame.font.Font(None, 80)
        #     font = pygame.font.SysFont('arial', 36)
        #     # text_surface = font.render("GAME OVER!",
        #     #                                 False, (0, 0, 0), (255, 0, 0))
        #     text_surface = font.render("GAME OVER!" + "R to restart, Q to quit",
        #                                     False, (0, 0, 0))
        #     text_surface_rect = text_surface.get_rect()
        #     text_surface_rect.left = screen_rect.left + screen_rect.width / 2 - text_surface_rect.width / 2
        #     text_surface_rect.top = screen_rect.top + screen_rect.height / 2 - text_surface_rect.height / 2
        #     screen.blit(text_surface, text_surface_rect)
        #     is_restart, is_quit = gf.check_game_control_event()
        #     if is_restart:
        #         main()
        #     if is_quit:
        #         pygame.quit()
        pygame.display.flip()

        # while GAME_OVER == True:
        if GAME_OVER == True:
            fontObj = pygame.font.SysFont('arial', 36)
            textSurfaceObj = fontObj.render("GAME OVER!" + "R to restart, Q to quit",
                                            False, (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.left = screen_rect.left + screen_rect.width / 2 - textRectObj.width / 2
            textRectObj.top = screen_rect.top + screen_rect.height / 2 - textRectObj.height / 2
            screen.blit(textSurfaceObj, textRectObj)
            pygame.display.flip()

            is_restart, is_quit = gf.check_game_control_event()
            if is_restart:
                run_game()
            if is_quit:
                sys.quit()


run_game()
