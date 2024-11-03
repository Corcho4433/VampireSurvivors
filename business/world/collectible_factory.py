"""Spawner encargado de generar gemas."""

from random import randint
import settings

from business.world.interfaces import IMonster, IGameWorld
from business.entities.collectibles.experience_gem import ExperienceGem
from business.entities.collectibles.chest import Chest
from business.world.interfaces import ICollectibleFactory

class CollectibleFactory(ICollectibleFactory):
    """Creates gems that the enemies drop using the enemy"""

    @staticmethod
    def create_collectible(name: str, pos):
        match name:
            case "experience":
                return ExperienceGem(pos)
            case "chest":
                return Chest(pos)

    @staticmethod
    def create_random_gem(monster: IMonster, world: IGameWorld):
        luck_stat = world.player.luck

        minimum_threshold = ((100 - settings.MINIMUM_GEM_DROP_CHANCE) * (luck_stat - 1)/100) + settings.MINIMUM_GEM_DROP_CHANCE
        chance = randint(0, 100)

        if chance < minimum_threshold:
            gem = CollectibleFactory.create_collectible('experience', monster.pos)
            world.add_collectible(gem)
