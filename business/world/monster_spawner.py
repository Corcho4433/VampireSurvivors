"""This module contains the MonsterSpawner class."""

import logging
import random

from pygame import Vector2

import settings
from business.entities.monster_factory import MonsterFactory
from business.world.interfaces import IGameWorld, IMonsterSpawner


class MonsterSpawner(IMonsterSpawner):
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)

    def update(self, world: IGameWorld):
        self.spawn_monster(world)

    def spawn_monster(self, world):
        choice = random.choice(["default", "red_ghost"])
        match choice:
            case "default":
                return self.__spawn_default_monster(world)
            case "red_ghost":
                return self.__spawn_red_ghost(world)

    def __get_random_position(self):
        return Vector2(random.randint(0, settings.WORLD_WIDTH), random.randint(0, settings.WORLD_HEIGHT))

    def __spawn_default_monster(self, world: IGameWorld):
        pos = self.__get_random_position()
        monster = MonsterFactory.create_monster('default', pos)
        world.add_monster(monster)
        self.__logger.debug("Spawning monster at (%d, %d)", pos.x, pos.y)

    def __spawn_red_ghost(self, world: IGameWorld):
        pos = self.__get_random_position()
        monster = MonsterFactory.create_monster('red_ghost', pos)
        world.add_monster(monster)
        self.__logger.debug("Spawning ghost at (%d, %d)", pos.x, pos.y)
