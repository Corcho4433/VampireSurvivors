"""This module contains the MonsterSpawner class."""

import logging
import random

from pygame import Vector2

import settings
from business.entities.monster_factory import MonsterFactory
from business.world.interfaces import IGameWorld, IMonsterSpawner
from business.world.clock import Clock

class MonsterSpawner(IMonsterSpawner):
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__clock = Clock()
        self.__final_boss_flag = 0

    def update(self, world: IGameWorld):
        self.spawn_monster(world)

    def spawn_monster(self, world):
        choices = ["default"]
        for _ in range(int(self.__clock.time/180)):
            choices.append("red_ghost")
        for _ in range(int(self.__clock.time/300)):
            self.__final_boss_flag += 1
        pos = self.__get_random_position()
        monster = MonsterFactory.create_monster(random.choice(choices), pos)
        world.add_monster(monster)
        if self.__final_boss_flag == 1:
            boss = MonsterFactory.create_monster("boss", pos)
            world.add_monster(boss)
            self.__final_boss_flag = 0
        self.__logger.debug(f"Spawning {monster} at (%d, %d)", pos.x, pos.y)

    def __get_random_position(self):
        return Vector2(random.randint(0, settings.WORLD_WIDTH),
        random.randint(0, settings.WORLD_HEIGHT))
