"""Defines teh class used in the player's inventory"""

from business.progression.interfaces import IInventoryItem, IUpgrade

class InventoryItem(IInventoryItem):
    """An item from the inventory"""

    def __init__(self, name: str, upgrades: list[IUpgrade]):
        self.__name = name
        self.__level = 1
        self.__upgrades = upgrades

    def upgrade(self):
        self.__level += 1

    @property
    def upgrades(self):
        return self.__upgrades

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level
