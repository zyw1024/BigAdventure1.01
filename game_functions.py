import sys
import pygame


global mouse_x, mouse_y


def check_events(player):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.moving_right = True
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.moving_left = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.moving_top = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.moving_down = True

        if event.type == pygame.KEYDOWN:
            player.choice = -1
            if event.key == ord('1'):
                player.choice = 1
            elif event.key == ord('2'):
                player.choice = 2
            elif event.key == ord('3'):
                player.choice = 3
            elif event.key == ord('4'):
                player.choice = 4
            elif event.key == ord('5'):
                player.choice = 5
            elif event.key == ord('6'):
                player.choice = 6
            elif event.key == ord('7'):
                player.choice = 7
            elif event.key == ord('8'):
                player.choice = 8
            elif event.key == ord('9'):
                player.choice = 9
            elif event.key == ord('0'):
                player.choice = 0
            print("choice = ", player.choice)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.moving_right = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.moving_left = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.moving_top = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.moving_down = False

        # global mouse_x, mouse_y
        if event.type == pygame.MOUSEMOTION:
            player.mouse_x, player.mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            player.mouse_button_left, player.mouse_wheel, player.mouse_button_right = pressed_array

        if event.type == pygame.MOUSEBUTTONUP:
            pressed_array = pygame.mouse.get_pressed()
            player.mouse_button_left, player.mouse_wheel, player.mouse_button_right = pressed_array



def check_game_control_event():
    is_restart = False
    is_quit = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('r'):
                is_restart = True
            elif event.key == ord('q'):
                is_quit = True


    return is_restart, is_quit

def check_interaction_event():
    for event in pygame.event.get():
        print("======================================")
        if event.type == pygame.KEYDOWN:
            print("KEY DOWN!")
            if event.key == ord('1'):
                choice = 1
            elif event.key == ord('2'):
                choice = 2
            elif event.key == ord('3'):
                choice = 3
            elif event.key == ord('4'):
                choice = 4
            elif event.key == ord('5'):
                choice = 5
            elif event.key == ord('6'):
                choice = 6
            elif event.key == ord('7'):
                choice = 7
            elif event.key == ord('8'):
                choice = 8
            elif event.key == ord('9'):
                choice = 9
            elif event.key == ord('0'):
                choice = 0
            print("choice = ",choice)
            return  choice

def blit_all(ai_settings, screen, player, monsters, bullets, probes, treasures, npc):
    # def blit_all(ai_settings, screen, player, skeleton):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    # screen.fill(ai_settings.bg_color)
    # screen.blit(ai_settings.bg, (0, 0))
    # Draw the walls
    for i in range(0, len(ai_settings.walls)):
        wallrect = pygame.draw.rect(screen, (0, 0, 0), ai_settings.walls[i].rect)
        for k, v in sorted(ai_settings.wall_stone.items(), reverse=True):
            if i % k == 0:
                screen.blit(v, wallrect)
                break
    for i in range(0, len(ai_settings.roads)):
        roadrect = pygame.draw.rect(screen, (0, 0, 0), ai_settings.roads[i].rect)
        for k, v in sorted(ai_settings.road_stone.items(), reverse=True):
            if i % k == 0:
                screen.blit(v, roadrect)
                break

    startrect = pygame.draw.rect(screen, (255, 255, 255), ai_settings.start.rect)
    screen.blit(ai_settings.start_img, startrect)
    endrect = pygame.draw.rect(screen, (255, 255, 255), ai_settings.end.rect)
    screen.blit(ai_settings.end_img, endrect)

    player.blitme()

    for monster in monsters:
        monster.blitme()

    for bullet in bullets:
        bullet.blitme()

    # for probe in probes:
        # probe.blitme()

    for treasure in treasures:
        treasure.blitme()

    if npc != None:
        npc.blitme()

    # # Make the most recently drawn screen visible.
    # pygame.display.flip()


def collide_walls(self):
    """Detect if a object collide a wall and return collided side of the object"""
    is_collide_wall = False
    collidebottom = 0
    collidetop = 0
    collideright = 0
    collideleft = 0
    for i in range(0, len(self.ai_settings.walls)):
        if self.rect.colliderect(self.ai_settings.walls[i].rect):
            is_collide_wall = True
            if self.rect.bottom >= self.ai_settings.walls[i].rect.top and \
                    self.rect.right - self.ai_settings.walls[i].rect.left > 2 and \
                    self.rect.left - self.ai_settings.walls[i].rect.right < - 2:
                if self.rect.bottom - self.ai_settings.walls[i].rect.top <= 2:
                    collidebottom = 1
                    # print("collidebottom")
                    continue
            if self.rect.top <= self.ai_settings.walls[i].rect.bottom and \
                    self.rect.right - self.ai_settings.walls[i].rect.left > 2 and \
                    self.rect.left - self.ai_settings.walls[i].rect.right < - 2:
                if self.ai_settings.walls[i].rect.bottom - self.rect.top <= 2:
                    collidetop = 1
                    # print("collidetop")
                    continue
            if self.rect.right >= self.ai_settings.walls[i].rect.left and \
                    self.rect.top - self.ai_settings.walls[i].rect.bottom < - 2 and \
                    self.rect.bottom - self.ai_settings.walls[i].rect.top > 2:
                if self.rect.right - self.ai_settings.walls[i].rect.left <= 2:
                    collideright = 1
                    # print("collideright")
                    continue
            if self.rect.left <= self.ai_settings.walls[i].rect.right and \
                    self.rect.top - self.ai_settings.walls[i].rect.bottom < - 2 and \
                    self.rect.bottom - self.ai_settings.walls[i].rect.top > 2:
                if self.ai_settings.walls[i].rect.right - self.rect.left <= 2:
                    collideleft = 1
                    # print("collideleft")

    return collidebottom, collidetop, collideright, collideleft, is_collide_wall



