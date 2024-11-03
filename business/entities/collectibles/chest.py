""""""
import random
from pygame import Vector2

from presentation.sprite import ChestSprite
from business.entities.collectibles.collectible import Collectible
from business.entities.interfaces import IChest, IInventoryItem
from business.progression.perk_factory import PerkFactory
from business.weapons.weapon_factory import WeaponFactory

class Chest(Collectible, IChest):
    """Represents a chest in the game world."""

    def __init__(self, pos: Vector2):
        super().__init__("chest", pos, ChestSprite(pos))
        self._logger.debug("Created %s", self)
        self.__item : IInventoryItem = None
        self.__assign_item()

    def __assign_item(self):
        choice = random.choice([1,2])
        if choice == 1:
            perk = random.choice(["hollow_heart", "clover", "spinach"])
            self.__item = PerkFactory.create_perk(perk)
        elif choice == 2:
            weapon = random.choice(["whip", "gun"])
            self.__item = WeaponFactory.create_weapon(weapon)

    @property
    def item(self):
        return self.__item

    def __str__(self):
        return f"Chest(pos=({self.pos.x}, {self.pos.y}))"
