"""Defines teh class used in the player's inventory"""

from business.progression.interfaces import IInventoryItem, IUpgrade

class InventoryItem(IInventoryItem):
    """An item belonging in the inventory"""

    TYPES = {
        'WEAPON': 1,
        'PERK': 2,
    }

    def __init__(self, name: str, item_type: str, upgrades: list[IUpgrade]):
        self.__name = name
        self.__type = item_type
        self.__level = 1
        self.__upgrades = upgrades

    def upgrade(self):
        next_upgrade = self.get_next_upgrade()

        print(next_upgrade)
        if next_upgrade:
            next_upgrade.apply(self)

        self.__level += 1

    @property
    def upgrades(self):
        return self.__upgrades

    @property
    def item_type(self) -> str:
        return self.__type

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level
    
    def get_stat(self, name: str):
        if hasattr(self, name):
            return getattr(self, name)
        
        return

    def get_next_upgrade(self):
        if self.level > len(self.upgrades):
            return

        return self.upgrades[self.level - 1]
