"""Defines teh class used in the player's inventory"""

from business.progression.interfaces import IInventoryItem

class InventoryItem(IInventoryItem):
    def __init__(self, name: str):
        self.__name = name
        self.__level = 1

    def upgrade(self):
        self.__level += 1

    @property
    def level(self):
        return self.__level
