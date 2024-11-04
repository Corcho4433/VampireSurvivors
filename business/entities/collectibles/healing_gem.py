"""Defines an experience gem, which gives the player experience"""
from pygame import Vector2

from presentation.sprite import HealingGemSprite
from business.entities.collectibles.collectible import Collectible
from business.entities.interfaces import IHealingGem

class HealingGem(Collectible, IHealingGem):
    """Represents an experience gem in the game world."""

    BASE_HEALING = 30

    def __init__(self, pos: Vector2, heal_amount: int=BASE_HEALING):
        super().__init__("healing", pos, HealingGemSprite(pos))
        self._logger.debug("Created %s", self)
        self.__heal_amount = heal_amount

    @property
    def amount(self) -> int:
        return self.__heal_amount

    def __str__(self):
        return f"HealingGem(amount={self.__heal_amount}, pos=({self.pos.x}, {self.pos.y}))"
