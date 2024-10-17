"""Module for the ExperienceGem class."""

from pygame import Vector2
from business.entities.entity import Entity
from business.entities.interfaces import IExperienceGem
from presentation.sprite import ExperienceGemSprite


class ExperienceGem(Entity, IExperienceGem):
    """Represents an experience gem in the game world."""

    def __init__(self, pos: Vector2, amount: int):
        super().__init__(pos.x, pos.y, ExperienceGemSprite(pos.x, pos.y))
        self._logger.debug("Created %s", self)

    @property
    def amount(self) -> int:
        pass

    def __str__(self):
        return f"ExperienceGem(amount={self.__amount}, pos=({self.pos.x}, {self.pos.y}))"
