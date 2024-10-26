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
    def build_upgrades_for(weapon_name: str):
        upgrades_data = load_file(UPGRADES_ROUTE)
        weapon_upgrade_data = upgrades_data[weapon_name]

        if weapon_upgrade_data:
            upgrades = []
            for weapon_upgrade in weapon_upgrade_data:
                values = []
                for value_object in weapon_upgrade['values']:
                    values.append(UpgradeValue(value_object['type'], value_object['stat'], value_object['value']))

                upgrades.append(Upgrade(weapon_upgrade['description'], values))

            return upgrades
