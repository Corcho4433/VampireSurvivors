"""Defines the class used for the player's inventory"""

from business.progression.interfaces import IInventory, IInventoryItem
from business.world.interfaces import IGameWorld
from business.weapons.weapon_factory import WeaponFactory
from business.progression.item import InventoryItem
from business.progression.perk_factory import PerkFactory

class Inventory(IInventory):
    """A class symbolizing the player's inventory"""

    DEFAULT_LIMIT = 6

    def __init__(self, world: IGameWorld):
        perk_factory = PerkFactory(world)

        self.__items = {}

        self.add_item(perk_factory.create_perk("spinach"))
        self.add_item(perk_factory.create_perk("clover"))
        self.add_item(perk_factory.create_perk("hollow_heart"))
        self.add_item(WeaponFactory(world).create_weapon('gun'))

    @property
    def limit(self) -> int:
        return self.DEFAULT_LIMIT

    @property
    def item_count(self) -> int:
        count = 0
        for _ in range(len(self.__items.keys())):
            count += 1
        return count

    def add_item(self, item: IInventoryItem):
        if self.item_count + 1 > self.limit:
            return

        self.__items[item.name] = item

    def get_item(self, name: str):
        return self.__items[name]

    def get_perks(self):
        items = []

        for _, item in self.__items.items():
            if item.item_type == InventoryItem.TYPES['PERK']:
                items.append(item)

        return items

    def get_weapons(self):
        items = []

        for _, item in self.__items.items():
            if item.item_type == InventoryItem.TYPES['WEAPON']:
                items.append(item)

        return items

    def get_items(self):
        items = []

        for _,item in self.__items.items():
            items.append(item)

        return items