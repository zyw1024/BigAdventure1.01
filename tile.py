import pygame


class Tile():
    def __init__(self, s, x, y):
        self.rect = pygame.Rect(x, y, s.maze_block_width, s.maze_block_height)


class Wall(Tile):
    # def __init__(self, s, x, y):
    #     self.rect = pygame.Rect(x, y, s.maze_block_width, s.maze_block_height)
    pass


class Road(Tile):
    pass
