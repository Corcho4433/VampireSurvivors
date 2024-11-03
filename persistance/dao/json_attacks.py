"""Defines the DAO for collectible items"""

import json
from pygame import Vector2

from persistance.interfaces import AttackDAO
from persistance.json_helpers import create_json_file

class JSONAttackDao(AttackDAO):
    """A Data-Access-Object that handles all monsters in a json file"""

    def __init__(self, json_path: str):
        self.__path = json_path

    def get_all_attacks(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                attacks = []

                for monster_data in data['map_info']['attacks']:
                    pos = monster_data['pos']
                    attack_type = monster_data['type']
                    v2_pos = Vector2(pos[0], pos[1])

                    #collectible = CollectibleFactory.create_collectible(collectible_type, v2_pos)

                    #collectibles.append(collectible)

                return attacks
        except ValueError:
            create_json_file(self.__path)

            return self.get_all_attacks()

    def __get_full_file_json(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            create_json_file(self.__path)

            return self.__get_full_file_json()

    def clear_attacks(self):
        try:
            data = self.__get_full_file_json()
            data['map_info']['attacks'] = []

            with open(self.__path, 'w', encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4)
        except ValueError:
            create_json_file(self.__path)

            return self.clear_attacks()

    def add_attack(self, attack):
        try:
            data = self.__get_full_file_json()
            new_collectible = {
                "pos": [attack.pos.x, attack.pos.y],
                "type": attack.type,
            }

            data['map_info']['attacks'].append(new_collectible)

            with open(self.__path, 'w', encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4)
        except ValueError:
            create_json_file(self.__path)

            return self.add_attack(attack)
