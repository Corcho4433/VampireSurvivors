"""Defines the class used for the player's inventory"""

from business.progression.interfaces import IInventory

class Inventory(IInventory):
    """A class symbolizing the player's inventory"""

    DEFAULT_LIMIT = 6

    def __init__(self):
        self.__items = {}

    @property
    def limit(self) -> int:
        return self.DEFAULT_LIMIT

    def add_item(self, item):
        self.__items[item.name] = item

    def get_item(self, name: str):
        return self.__items[name]
