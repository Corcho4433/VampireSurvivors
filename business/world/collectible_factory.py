"""Spawner encargado de generar gemas."""

from random import randint
import settings

from business.world.interfaces import IMonster, IGameWorld
from business.entities.collectibles.experience_gem import ExperienceGem
from business.entities.collectibles.healing_gem import HealingGem
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
            case "healing":
                return HealingGem(pos)

    @staticmethod
    def create_random_gem(monster: IMonster, world: IGameWorld):
        luck_stat = world.player.luck

        minimum_threshold = settings.MINIMUM_GEM_DROP_CHANCE + luck_stat
        print(minimum_threshold, luck_stat)
        chance = randint(0, 100)

        if chance < minimum_threshold:
            choice = randint(0, 100)
            if 0 <= choice <= 70: 
                gem = CollectibleFactory.create_collectible('experience', monster.pos)
            else:
                gem = CollectibleFactory.create_collectible('healing', monster.pos)

            world.add_collectible(gem)
