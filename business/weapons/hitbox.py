import pygame
from business.entities.interfaces import IMonster

class Hitbox:
    def __init__(self, size: pygame.Vector2, pos: pygame.Vector2, rect: pygame.rect):
        self.__rect = rect

    def get_enemies_inside(self):
        pass
