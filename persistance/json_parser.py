"""Defines the general class used to parse json into python code

    This class creates objects using the data obtained from the general
    json files in `/data` folder
"""

import json
from persistance.interfaces import IJSONParser
from business.progression.upgrade import Upgrade, UpgradeValue

UPGRADES_ROUTE = "data/upgrades.json"

def load_file(route: str):
    """Loads a specific JSON file"""

    with open(route, encoding="utf-8") as data_file:
        return json.load(data_file)


class JSONParser(IJSONParser):
    """General JSON data parser"""

    @staticmethod
    def build_upgrades_for(item_name: str):
        upgrades_data = load_file(UPGRADES_ROUTE)
        item_upgrade_data = upgrades_data[item_name]

        if item_upgrade_data:
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
