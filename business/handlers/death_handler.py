"""Module that contains the DeathHandler class."""

#from business.entities.experience_gem import ExperienceGem
from business.exceptions import DeadPlayerException
from business.world.interfaces import IGameWorld
from business.handlers.position_handler import PositionHandler


class DeathHandler:
    """Class that handles entity deaths."""

    @staticmethod
    def __is_entity_within_world_boundaries(entity):
        return PositionHandler.is_position_within_boundaries(entity.pos)

    @staticmethod
    def check_deaths(world: IGameWorld):
        """Check if any entities have died and remove them from the game world.

        Args:
            world (IGameWorld): The game world to check for dead entities.
        """
        for attack in world.attacks:
            if attack.charges_remaining <= 0:
                world.remove_attack(attack)
            if not DeathHandler.__is_entity_within_world_boundaries(attack):
                world.remove_attack(attack)

        for monster in world.monsters:
            if monster.health <= 0:
                world.remove_monster(monster)
            if not DeathHandler.__is_entity_within_world_boundaries(monster):
                world.remove_monster(monster)

        for collectible in world.collectibles:
            if collectible.is_picked:
                world.remove_collectible(collectible)
            if not DeathHandler.__is_entity_within_world_boundaries(collectible):
                world.remove_collectible(collectible)

        if world.player.health <= 0:
            raise DeadPlayerException