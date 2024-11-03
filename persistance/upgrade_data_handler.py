"""Defines the general class used to parse json into python code

    This class creates objects using the data obtained from the general
    json files in `/data` folder
"""

import json
from persistance.interfaces import IUpgradeDataHandler

UPGRADES_ROUTE = "data/upgrades.json"
SAVE_FILE = "data/last_session.json"

def load_file(route: str):
    """Loads a specific JSON file"""

    with open(route, encoding="utf-8") as data_file:
        return json.load(data_file)


class UpgradeDataHandler(IUpgradeDataHandler):
    """General JSON data parser"""

    @staticmethod
    def get_item_upgrades(item_name: str):
        upgrades_data = load_file(UPGRADES_ROUTE)
        item_upgrade_data = upgrades_data[item_name]

        return item_upgrade_data
