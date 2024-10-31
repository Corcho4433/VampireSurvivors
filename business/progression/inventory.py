"""Defines the class used for the player's inventory"""

from business.progression.interfaces import IInventory, IInventoryItem
from business.world.interfaces import IGameWorld
from business.weapons.weapon_factory import WeaponFactory
from business.weapons.weapon_stats import WeaponStats
from business.progression.item import InventoryItem

class Inventory(IInventory):
    """A class symbolizing the player's inventory"""

    DEFAULT_LIMIT = 6

    def __init__(self, world: IGameWorld):
        arma_stats = WeaponStats()
        arma_inicial = WeaponFactory(world).create_gun(arma_stats)

        self.__items = {arma_inicial.name : arma_inicial}

    @property
    def limit(self) -> int:
        return self.DEFAULT_LIMIT

    @property
    def item_count(self) -> int:
        count = 0
        for _ in range(self.__items.keys()):
            count += 1
        return count

    def add_item(self, item: IInventoryItem):
        if self.item_count + 1 > self.limit:
            return

        self.__items[item.name] = item

    def get_item(self, name: str):
        return self.__items[name]

    def get_weapons(self):
        items = []

        for _, item in self.__items.items():
            if item.item_type == InventoryItem.TYPES['WEAPON']:
                items.append(item)

        return items
