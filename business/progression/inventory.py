"""Defines the class used for the player's inventory"""

from business.progression.interfaces import IInventory, IInventoryItem
from business.progression.item import InventoryItem

class Inventory(IInventory):
    """A class symbolizing the player's inventory"""

    DEFAULT_LIMIT = 6

    def __init__(self):
        self.__items = {}

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
        try:
            if self.get_item(item.name) is None:
                self.__items[item.name] = item
            else:
                item.upgrade()
                self.__items[item.name] = item
        except KeyError:
            self.__items[item.name] = item
        except AttributeError as exception_error_text:
            print("Error when adding item", exception_error_text)

    def get_item(self, name: str):
        try:
            return self.__items[name]
        except KeyError:
            return None

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
