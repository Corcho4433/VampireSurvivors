"""
    Defines the JSON DAO class for the inventory
"""

import json

from business.progression.perk_factory import PerkFactory
from business.weapons.weapon_factory import WeaponFactory
from business.progression.item import InventoryItem

from business.progression.inventory import Inventory
from persistance.interfaces import InventoryDAO
from persistance.json_helpers import create_json_file

class JSONInventoryDAO(InventoryDAO):
    """Data-Access-Object for the inventory"""

    def __init__(self, json_path: str):
        self.__path = json_path

    def get_inventory(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)

                inventory = data['player']['inventory']
                inventory_object = Inventory()

                for item in inventory:
                    item_type = item['type']
                    level = item['level']
                    name = item['name']

                    if item_type == InventoryItem.TYPES['WEAPON']:
                        new_item = WeaponFactory.create_weapon(name)
                    elif item_type == InventoryItem.TYPES['PERK']:
                        new_item = PerkFactory.create_perk(name)

                    if new_item is None: #pylint: disable=E0606
                        continue

                    if level > new_item.level:
                        for _ in range(level - new_item.level):
                            new_item.upgrade()

                    inventory_object.add_item(new_item)

                return inventory_object
        except ValueError:
            create_json_file(self.__path)

            return self.get_inventory()

    def __get_full_file_json(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            create_json_file(self.__path)

            return self.__get_full_file_json()

    def add_item(self, item: InventoryItem):
        try:
            data = self.__get_full_file_json()
            new_item = {
                "type": item.item_type,
                "name": item.name,
                "level": item.level,
            }

            data['player']['inventory'].append(new_item)

            with open(self.__path, 'w', encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4)
        except ValueError:
            create_json_file(self.__path)

            return self.add_item(item)
