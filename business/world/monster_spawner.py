"""This module contains the MonsterSpawner class."""

import logging
import random

from pygame import Vector2

import settings
from business.entities.monster import Monster
from business.world.interfaces import IGameWorld, IMonsterSpawner
from presentation.sprite import MonsterSprite


class MonsterSpawner(IMonsterSpawner):
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)

    def update(self, world: IGameWorld):
        self.spawn_monster(world)

    def spawn_monster(self, world: IGameWorld):
        pos = Vector2(random.randint(0, settings.WORLD_WIDTH), random.randint(0, settings.WORLD_HEIGHT))

        monster = Monster(pos, MonsterSprite(pos))
        world.add_monster(monster)
        self.__logger.debug("Spawning monster at (%d, %d)", pos.x, pos.y)
