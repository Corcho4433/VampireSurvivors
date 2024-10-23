"""Module for the ExperienceGem class."""

from pygame import Vector2
from business.entities.entity import Entity
from business.entities.interfaces import IExperienceGem
from presentation.sprite import ExperienceGemSprite


class ExperienceGem(Entity, IExperienceGem):
    """Represents an experience gem in the game world."""

    BASE_EXPERIENCE = 1

    def __init__(self, pos: Vector2, exp_amount: int=BASE_EXPERIENCE):
        super().__init__(pos, ExperienceGemSprite(pos))
        self._logger.debug("Created %s", self)
        self.__exp_amount = exp_amount
        self.__picked = False

    @property
    def is_picked(self) -> bool:
        return self.__picked

    @property
    def amount(self) -> int:
        return self.__exp_amount

    def __str__(self):
        return f"ExperienceGem(amount={self.__amount}, pos=({self.pos.x}, {self.pos.y}))"

    def pick(self):
        self.__picked = True