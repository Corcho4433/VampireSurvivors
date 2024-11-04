"""Defines the general class used to parse json into python code

    This class creates objects using the data obtained from the general
    json files in `/data` folder
"""

import json
from persistance.interfaces import IItemDataHandler

ITEMS_ROUTE = "data/items.json"

def load_file(route: str):
    """Loads a specific JSON file"""

    with open(route, encoding="utf-8") as data_file:
        return json.load(data_file)


class ItemDataHandler(IItemDataHandler):
    """General JSON data parser"""

    @staticmethod
    def get_item_upgrades(item_name: str):
        upgrades_data = load_file(ITEMS_ROUTE)
        item_upgrade_data = upgrades_data[item_name]

        return item_upgrade_data['upgrades']

    @staticmethod
    def get_all_items():
        data = load_file(ITEMS_ROUTE)

        items = []
        for item in enumerate(data):
            item_name = item[1]
            item_data = data[item_name]

            items.append((item_name, item_data['type']))

        return items

    @staticmethod
    def get_item_type(name: str):
        data = load_file(ITEMS_ROUTE)

        try:
            item_data = data[name]

            return item_data['type']
        except KeyError:
            return 0
