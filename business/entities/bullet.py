"""Module for a bullet entity that moves towards a target direction."""

import math

from pygame import Vector2
from business.entities.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite


class Bullet(MovableEntity, IBullet):
    """A bullet that moves towards a target direction."""

    def __init__(self, source, enemy_pos, speed):
        super().__init__(source, speed, BulletSprite(enemy_pos))
        self._logger.debug("Created %s", self)
        self._dir =  self.__calculate_direction(source, enemy_pos)

    def __calculate_direction(self, source, enemy_pos):
        direction = source - enemy_pos
        y = direction.y
        x = direction.x

        if x != 0:
            x = -x/x
            
        if y != 0:
            y = -y/y

        return Vector2(x, y)

    @property
    def hits_remaining(self) -> int:
        pass

    def take_damage(self, amount):
        pass

    def update(self, _: IGameWorld):
        # Move bullet towards the target direction
        self.move(self._dir)

    @property
    def damage_amount(self):
        pass

    def __str__(self):
        return f"Bullet(pos=({self._pos.x, self._pos.y}), dir=({self.__dir_x, self.__dir_y}))"
