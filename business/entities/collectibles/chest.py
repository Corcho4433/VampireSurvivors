""""""
import random
from pygame import Vector2

from presentation.sprite import ChestSprite
from business.entities.collectibles.collectible import Collectible
from business.entities.interfaces import IChest, IInventoryItem
from business.progression.item_factory import ItemFactory

from business.handlers.item_data_handler import ItemDataHandler

class Chest(Collectible, IChest):
    """Represents a chest in the game world."""

    def __init__(self, pos: Vector2):
        super().__init__("chest", pos, ChestSprite(pos))
        self._logger.debug("Created %s", self)
        self.__item : IInventoryItem = None
        self.__assign_item()

    def __assign_item(self):
        item_selected = random.choice(ItemDataHandler.get_all_items())

        self.__item = ItemFactory.create_item(item_selected[0])

    @property
    def item(self):
        return self.__item

    def __str__(self):
        return f"Chest(pos=({self.pos.x}, {self.pos.y}))"
