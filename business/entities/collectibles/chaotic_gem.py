"""Defines an experience gem, which gives the player experience"""
from pygame import Vector2

from presentation.sprite import ChaoticGemSprite
from business.entities.collectibles.collectible import Collectible
from business.entities.interfaces import IChaoticGem
from business.handlers.cooldown_handler import CooldownHandler

class ChaoticGem(Collectible, IChaoticGem):
    """Represents a super powerful experience gem in the game world."""

    def __init__(self, pos: Vector2):
        super().__init__("chaos", pos, ChaoticGemSprite(pos))
        self._logger.debug("Created %s", self)
        self.__timer = CooldownHandler(10)
        self.__timer.put_on_cooldown()
        self.__picked = False

    @property
    def is_picked(self):
        return self.__timer.is_action_ready() or self.__picked
    
    def pick(self):
        self.__picked = True

    def __str__(self):
        return f"ChaoticGem(amount={self.__exp_amount}, pos=({self.pos.x}, {self.pos.y}))"
