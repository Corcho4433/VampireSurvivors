"""Defines the class used in the player's inventory"""

from business.progression.item import InventoryItem
from business.progression.interfaces import IUpgradePerk, IUpgrade

class UpgradePerk(InventoryItem, IUpgradePerk):
    """An item from the inventory"""

    def __init__(self):
        pass

    @property
    def upgrades(self):
        return self.__upgrades

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level
