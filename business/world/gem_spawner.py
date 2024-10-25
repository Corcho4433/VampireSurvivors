"""Spawner encargado de generar gemas."""

import logging
import settings
from random import randint

from business.world.interfaces import IMonster, IGameWorld
from business.entities.experience_gem import ExperienceGem
from business.world.interfaces import IGemFactory

class ExperienceGemFactory(IGemFactory):
    """Creates gems that the enemies drop using the enemy"""

    def __init__(self) -> None:
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Created %s", self)

    def create_gem(self, monster: IMonster, world: IGameWorld):
        luck_stat = world.player.luck

        minimum_threshold = ((100 - settings.MINIMUM_GEM_DROP_CHANCE) * (luck_stat - 1)/100) + settings.MINIMUM_GEM_DROP_CHANCE
        chance = randint(0, 100)

        if chance < minimum_threshold:
            gem = ExperienceGem(monster.pos)
            world.add_experience_gem(gem)
