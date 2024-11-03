"""This module contains the MonsterSpawner class."""

import logging
import random

from pygame import Vector2

import settings
from business.world.collectible_factory import CollectibleFactory
from business.world.interfaces import IGameWorld, IChestSpawner

class ChestSpawner(IChestSpawner):
    """Spawns chests in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)

    def update(self, world: IGameWorld):
        self.spawn_chest(world)

    def spawn_chest(self, world):
        pos = self.__get_random_position()
        chest = CollectibleFactory.create_collectible("chest", pos)
        world.add_collectible(chest)
        self.__logger.debug("Spawning chest at (%d, %d)", pos.x, pos.y)

    def __get_random_position(self):
        return Vector2(random.randint(0, settings.WORLD_WIDTH),
        random.randint(0, settings.WORLD_HEIGHT))
