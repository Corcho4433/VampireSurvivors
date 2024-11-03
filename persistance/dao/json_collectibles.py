"""Defines the DAO for collectible items"""

import json
from pygame import Vector2

from business.world.collectible_factory import CollectibleFactory
from persistance.interfaces import CollectibleDAO
from persistance.json_helpers import create_json_file

class JSONCollectibleDAO(CollectibleDAO):
    """A Data-Access-Object that handles all monsters in a json file"""

    def __init__(self, json_path: str):
        self.__path = json_path

    def get_all_collectibles(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                collectibles = []

                for monster_data in data['map_info']['collectibles']:
                    pos = monster_data['pos']
                    collectible_type = monster_data['type']
                    v2_pos = Vector2(pos[0], pos[1])

                    collectible = CollectibleFactory.create_collectible(collectible_type, v2_pos)

                    collectibles.append(collectible)

                return collectibles
        except ValueError:
            create_json_file(self.__path)

            return self.get_all_collectibles()

    def __get_full_file_json(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            create_json_file(self.__path)

            return self.__get_full_file_json()

    def clear_collectibles(self):
        try:
            data = self.__get_full_file_json()
            data['map_info']['collectibles'] = []

            with open(self.__path, 'w', encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4)
        except ValueError:
            create_json_file(self.__path)

            return self.clear_collectibles()

    def add_collectible(self, collectible):
        try:
            data = self.__get_full_file_json()
            new_collectible = {
                "pos": [collectible.pos.x, collectible.pos.y],
                "type": collectible.type,
            }

            data['map_info']['collectibles'].append(new_collectible)

            with open(self.__path, 'w', encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4)
        except ValueError:
            create_json_file(self.__path)

            return self.add_collectible(collectible)
