"""Defines an experience gem, which gives the player experience"""
from pygame import Vector2

from presentation.sprite import ExperienceGemSprite
from business.entities.collectibles.collectible import Collectible
from business.entities.interfaces import IExperienceGem

class ExperienceGem(Collectible, IExperienceGem):
    """Represents an experience gem in the game world."""

    BASE_EXPERIENCE = 1

    def __init__(self, pos: Vector2, exp_amount: int=BASE_EXPERIENCE):
        super().__init__("experience", pos, ExperienceGemSprite(pos))
        self._logger.debug("Created %s", self)
        self.__exp_amount = exp_amount

    @property
    def amount(self) -> int:
        return self.__exp_amount

    def __str__(self):
        return f"ExperienceGem(amount={self.__exp_amount}, pos=({self.pos.x}, {self.pos.y}))"
