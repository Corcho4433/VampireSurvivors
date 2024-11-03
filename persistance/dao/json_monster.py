"""Defines the class of a monster using JSON file"""

import json
from pygame import Vector2

from business.entities.monster_factory import MonsterFactory
from persistance.interfaces import MonsterDAO
from persistance.json_helpers import create_json_file

class JSONMonsterDAO(MonsterDAO):
    """A Data-Access-Object that handles all monsters in a json file"""

    def __init__(self, json_path: str):
        self.__path = json_path

    def get_all_monsters(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                monsters = []

                for monster_data in data['map_info']['monsters']:
                    pos = monster_data['pos']
                    monster_type = monster_data['type']
                    monster_health = monster_data['health']

                    v2_pos = Vector2(pos[0], pos[1])

                    new_monster = MonsterFactory.create_monster(monster_type, v2_pos)
                    if new_monster.health > monster_health:
                        new_monster.take_damage(new_monster.health - monster_health)

                    monsters.append(new_monster)

                return monsters
        except ValueError:
            create_json_file(self.__path)

            return self.get_all_monsters()

    def __get_full_file_json(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            create_json_file(self.__path)

            return self.__get_full_file_json()

    def create_monster(self, monster):
        try:
            data = self.__get_full_file_json()
            new_monster = {
                "pos": [monster.pos.x, monster.pos.y],
                "type": monster.type,
                "health": monster.health,
            }

            data['map_info']['monsters'].append(new_monster)

            with open(self.__path, 'w', encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4)
        except ValueError:
            create_json_file(self.__path)

            return self.create_monster(monster)
