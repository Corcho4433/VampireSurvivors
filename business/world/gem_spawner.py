"""Spawner encargado de generar gemas."""

import logging

from business.world.interfaces import IMonster, IGameWorld
from business.entities.experience_gem import ExperienceGem

class ExperienceGemFactory:
    def __init__(self) -> None:
        self.__logger = logging.getLogger(__name__)
        self.__logger.debug("Created %s", self)

    def create_gem(self, monster: IMonster, world: IGameWorld):
        gem = ExperienceGem(monster.pos)
        world.add_experience_gem(gem)