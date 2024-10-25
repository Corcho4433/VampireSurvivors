"""Module for the CollisionHandler class."""

from typing import List

from business.entities.interfaces import IBullet, IExperienceGem, IHasSprite, IMonster, IPlayer
from business.world.interfaces import IGameWorld


class CollisionHandler:
    """Handles collisions between entities in the game world."""

    @staticmethod
    def __collides_with(an_entity: IHasSprite, another_entity: IHasSprite):
        return an_entity.sprite.rect.colliderect(another_entity.sprite.rect)

    @staticmethod
    def __handle_bullets(bullets: List[IBullet], monsters: List[IMonster]):
        for bullet in bullets:
            for monster in monsters:
                if CollisionHandler.__collides_with(bullet, monster):
                    monster.take_damage(bullet.damage)
                    bullet.use_charge()

    @staticmethod
    def __handle_monsters(monsters: List[IMonster], player: IPlayer):
        pass

    @staticmethod
    def __handle_gems(gems: List[IExperienceGem], player: IPlayer, world: IGameWorld):
        for gem in gems:
            if CollisionHandler.__collides_with(gem, player):
                player.pickup_gem(gem)
                gem.pick()

    @staticmethod
    def handle_collisions(world: IGameWorld):
        """Handles collisions between entities in the game world.

        Args:
            world (IGameWorld): The game world.
        """
        CollisionHandler.__handle_bullets(world.bullets, world.monsters)
        CollisionHandler.__handle_monsters(world.monsters, world.player)
        CollisionHandler.__handle_gems(world.experience_gems, world.player, world)

    @staticmethod
    def get_monster_colliding_pairs(world: IGameWorld) -> list[tuple[IMonster, IMonster]]:
        """Gets all the colliding pairs of monsters

        Args:
            world (IGameWorld): The world the collisions are in

        Return:
            list[tuple[IMonster, IMonster]]: The monsters colliding
        """

        colliding_pairs = []
        for i in range(len(world.monsters) - 1):
            current_entity = world.monsters[i]
            next_entity = world.monsters[i + 1]

            if CollisionHandler.__collides_with(current_entity, next_entity):
                colliding_pairs.append((current_entity, next_entity))

        return colliding_pairs
