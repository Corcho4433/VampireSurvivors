"""Module for the ExperienceGem class."""

from pygame import Vector2
from business.entities.entity import Entity
from business.entities.interfaces import ICollectible


class Collectible(Entity, ICollectible):
    """Represents an experience gem in the game world."""

    def __init__(self, collectible_type: str, pos: Vector2, sprite):
        super().__init__(pos, sprite)

        self.__picked = False
        self.__type = collectible_type

    @property
    def is_picked(self) -> bool:
        return self.__picked

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return f"Collectible(pos=({self.pos.x}, {self.pos.y}))"

    def pick(self):
        self.__picked = True
