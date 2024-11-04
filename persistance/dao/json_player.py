"""Defines the class of a monster using JSON file"""

import json
from pygame import Vector2

from business.entities.player import Player
from business.world.clock import Clock
from persistance.interfaces import PlayerDAO
from persistance.json_helpers import create_json_file

class JSONPlayerDAO(PlayerDAO):
    """A Data-Access-Object that handles all monsters in a json file"""

    def __init__(self, json_path: str):
        self.__path = json_path

    def get_player(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                player_data = data['player']

                experience = player_data['experience']
                level = player_data['level']
                pos = player_data['pos']

                v2_pos = Vector2(pos[0], pos[1])

                player_object = Player(v2_pos, level, experience)

                return player_object
        except ValueError:
            create_json_file(self.__path)

            return self.get_player()

    def get_time(self) -> int:
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                player_data = data['player']

                return player_data['time']
        except ValueError:
            create_json_file(self.__path)

            return self.get_player()

    def __get_full_file_json(self):
        try:
            with open(self.__path, 'r', encoding="utf-8") as data_file:
                data = json.load(data_file)
                return data
        except ValueError:
            create_json_file(self.__path)

            return self.__get_full_file_json()

    def add_player(self, player):
        try:
            data = self.__get_full_file_json()

            data['player']['level'] = player.level
            data['player']['experience'] = player.experience
            data['player']['pos'] = [player.pos.x, player.pos.y]
            data['player']['time'] = Clock().time

            with open(self.__path, 'w', encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4)
        except ValueError:
            create_json_file(self.__path)

            return self.add_player(player)
