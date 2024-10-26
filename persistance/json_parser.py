"""Defines the general class used to parse json into python code

    This class creates objects using the data obtained from the general
    json files in `/data` folder
"""

import json
from persistance.interfaces import IJSONParser
#from business.progression.upgrade import Upgrade

UPGRADES_ROUTE = "data/upgrades.json"

def load_file(route: str):
    """Loads a specific JSON file"""

    with open(route) as data_file:
        return json.load(data_file)


class JSONParser(IJSONParser):
    """General JSON data parser"""

    @staticmethod
    def build_upgrade_from(data: str):
        upgrades_data = load_file(UPGRADES_ROUTE)
        print("hi hello?")
        print(upgrades_data)

        #return Upgrade(data)
