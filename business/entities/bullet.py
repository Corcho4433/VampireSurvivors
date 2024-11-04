"""Module for a bullet entity that moves towards a target direction."""

import math

from pygame import Vector2
from business.entities.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite

class Bullet(MovableEntity, IBullet):
    """A bullet that moves towards a target direction."""

    def __init__(self, source, enemy_pos, damage: int):
        super().__init__(source, 600, BulletSprite(enemy_pos))
        self._logger.debug("Created %s", self)
        self._dir =  self.__calculate_direction(source, enemy_pos)
        self._charges = 1 # que se determine la cantidad internamente
        self.__damage = damage

    def __calculate_direction(self, source, enemy_pos):
        direction = -(source - enemy_pos)
        mag = math.hypot(direction.x, direction.y)

        if mag != 0:
            return Vector2(direction.x / mag, direction.y / mag)

        return Vector2(0, 0)

    @property
    def charges_remaining(self) -> int:
        return self._charges

    @property
    def damage(self):
        print("bullet damage:", self.__damage)
        return self.__damage

    def use_charge(self, amount=1):
        self._charges -= amount

    def update(self, world: IGameWorld):
        # Move bullet towards the target direction
        direction = self._dir * world.simulation_speed

        self.move(direction)

        super().update(world)

    def __str__(self):
        return f"Bullet(pos=({self._pos.x, self._pos.y}), dir=({self._dir.x, self._dir.y}))"
