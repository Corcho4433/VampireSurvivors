"""Contains the base classes for all entities in the game."""

import logging
from abc import abstractmethod
from pygame import Vector2

from business.entities.interfaces import ICanMove, IDamageable, IHasPosition, IHasSprite
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite


class Entity(IHasPosition, IHasSprite):
    """Base class for all entities in the game."""

    def __init__(self, pos: Vector2, sprite: Sprite):
        self._pos: Vector2 = pos
        self._sprite: Sprite = sprite
        self._logger = logging.getLogger(self.__class__.__name__)

    def _get_distance_to(self, an_entity: IHasPosition) -> float:
        """Returns the distance to another entity using the Euclidean distance formula.

        Args:
            an_entity (IHasPosition): The entity to calculate the distance to.
        """

        return self.pos.distance_to(an_entity.pos)
        #((self.pos.x - an_entity.pos.x) ** 2 + (self.pos.y - an_entity.pos.y) ** 2) ** 0.5

    @property
    def pos(self) -> Vector2:
        return Vector2(self._pos.x, self._pos.y)

    @property
    def sprite(self) -> Sprite:
        return self._sprite

    @abstractmethod
    def __str__(self):
        """Returns a string representation of the entity."""

    def update(self, world: IGameWorld):
        """Updates the entity."""
        self.sprite.update()


class MovableEntity(Entity, ICanMove):
    """Base class for all entities that can move."""

    def __init__(self, pos: Vector2, speed: float, sprite: Sprite):
        super().__init__(pos, sprite)
        self._pos: Vector2 =  pos
        self._speed: float = speed
        self._sprite: Sprite = sprite

    def move(self, direction: Vector2):
        self._pos += direction * self._speed
        #self._pos_y += direction_y * self._speed
        self._logger.debug(
            "Moving in direction (%.2f, %.2f) with speed %.2f",
            direction.x,
            direction.y,
            self._speed,
        )
        self.sprite.update_pos(self._pos)

    @property
    def speed(self) -> float:
        return self._speed