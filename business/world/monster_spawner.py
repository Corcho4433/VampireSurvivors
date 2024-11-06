"""This module contains the MonsterSpawner class."""

import logging
import random

from settings import FPS

from pygame import Vector2

import settings
from business.entities.monster_factory import MonsterFactory
from business.world.interfaces import IGameWorld, IMonsterSpawner
from business.world.clock import Clock
from business.handlers.cooldown_handler import CooldownHandler

class MonsterSpawner(IMonsterSpawner):
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__clock = Clock()
        self.__final_boss_cooldown : CooldownHandler = CooldownHandler(300)

    def update(self, world: IGameWorld):
        self.spawn_monster(world)

    def spawn_monster(self, world):
        choices = ["default"]
        if self.__clock.time > 30:
            choices.append("fire")

        for _ in range(int(self.__clock.time/180)):
            choices.append("red_ghost")

        amount_by_clock = (self.__clock.time / 240) + 1

        for _ in range(round(amount_by_clock)):
            pos = self.__get_random_position()
            monster = MonsterFactory.create_monster(random.choice(choices), pos)
            world.add_monster(monster)

            self.__logger.debug(f"Spawning {monster} at (%d, %d)", pos.x, pos.y)

        if self.__final_boss_cooldown.is_action_ready():
            boss = MonsterFactory.create_monster("boss", pos)
            world.add_monster(boss)
            self.__final_boss_cooldown.put_on_cooldown()


    def __get_random_position(self):
        return Vector2(random.randint(0, settings.WORLD_WIDTH),
        random.randint(0, settings.WORLD_HEIGHT))
