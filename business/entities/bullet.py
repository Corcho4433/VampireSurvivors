"""Module for a bullet entity that moves towards a target direction."""

import settings

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
        self._charges = 1 # que se determine la cantidad internamente
        self.__damage = 5

    def __calculate_direction(self, source, enemy_pos):
        direction = source - enemy_pos
        y = direction.y
        x = direction.x

        if x != 0:
            x = -x / abs(x)

        if y != 0:
            y = -y / abs(y)

        return Vector2(x, y)

    @property
    def charges_remaining(self) -> int:
        return self._charges

    @property
    def damage_amount(self):
        return self.__damage

    def use_charge(self, amount=1):
        self._charges -= amount

    def update(self, world: IGameWorld):
        # Move bullet towards the target direction
        self.move(self._dir)

        super().update(world)

    def __str__(self):
        return f"Bullet(pos=({self._pos.x, self._pos.y}), dir=({self._dir.x, self._dir.y}))"
