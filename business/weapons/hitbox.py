"""Defines a hitbox used for attacks"""

import pygame
from business.entities.interfaces import IMonster
from business.entities.interfaces import IHitbox
from business.world.interfaces import IGameWorld

class Hitbox(IHitbox):
    """A hitbox, generally used in attacks"""

    def __init__(self, size: pygame.Vector2, pos: pygame.Vector2):
        self.__size : pygame.Vector2 = size
        self.__pos : pygame.Vector2 = pos
        self.__rect = pygame.Rect(self.__pos.x - self.size.x // 2, self.__pos.y - self.size.y // 2, self.size.x, self.size.y)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size: pygame.Vector2):
        self.__size = new_size

    def __check_collision(self, monster: IMonster):
        return self.__rect.colliderect(monster.sprite.rect)

    def get_enemies_inside(self, world: IGameWorld):
        enemies = []
        for monster in world.monsters:
            if self.__check_collision(monster):
                enemies.append(monster)

        return enemies
