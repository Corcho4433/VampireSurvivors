"""Defines the class "Data Handler" which loads all the items from
    the json file: ./data/items.json
"""

from business.progression.upgrade import Upgrade, UpgradeValue
from business.handlers.interfaces import IDataHandler
from business.handlers.item_data_handler import ItemDataHandler

class DataHandler(IDataHandler):
    """The data handler used in game to build items using data"""

    @staticmethod
    def build_upgrades_for_item(item_name: str):
        item_upgrade_data = ItemDataHandler.get_item_upgrades(item_name)

        upgrades = []
        for item_upgrade in item_upgrade_data:
            try:
                repeat_count = item_upgrade['repeats']
            except KeyError:
                repeat_count = 1

            for _ in range(repeat_count):
                values = []
                for value_object in item_upgrade['values']:
                    values.append(UpgradeValue(value_object['type'], value_object['stat'], value_object['value']))

                upgrades.append(Upgrade(item_upgrade['description'], values))

        return upgrades
