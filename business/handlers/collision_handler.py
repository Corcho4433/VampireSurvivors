"""Module for the CollisionHandler class."""

from typing import List

from business.entities.interfaces import IBullet, IExperienceGem, IHasSprite, IMonster, IPlayer, IMeleeAttack, IDistanceAttack, IChest
from business.world.interfaces import IGameWorld


class CollisionHandler:
    """Handles collisions between entities in the game world."""

    @staticmethod
    def __collides_with(an_entity: IHasSprite, another_entity: IHasSprite):
        return an_entity.sprite.rect.colliderect(another_entity.sprite.rect)

    @staticmethod
    def __handle_attacks(attacks: List[IBullet], monsters: List[IMonster]):
        for attack in attacks:
            for monster in monsters:
                if CollisionHandler.__collides_with(attack, monster):
                    monster.take_damage(attack.damage)
                    if isinstance(attack, IDistanceAttack):
                        attack.use_charge()

    @staticmethod
    def __handle_monsters(monsters: List[IMonster], player: IPlayer):
        pass

    @staticmethod
    def __handle_collectibles(collectibles: List[IExperienceGem], player: IPlayer):
        for collectible in collectibles:
            if CollisionHandler.__collides_with(collectible, player):
                if isinstance(collectible, IExperienceGem):
                    player.pickup_gem(collectible)
                    collectible.pick()
                if isinstance(collectible, IChest):
                    player.give_item(collectible.item)
                    print(f"se le dio el item {collectible.item.name}")
                    player.apply_perks()
                    print(f"se aplico el item {collectible.item.name}")
                    collectible.pick()

    @staticmethod
    def handle_collisions(world: IGameWorld):
        """Handles collisions between entities in the game world.

        Args:
            world (IGameWorld): The game world.
        """
        CollisionHandler.__handle_attacks(world.attacks, world.monsters)
        CollisionHandler.__handle_monsters(world.monsters, world.player)
        CollisionHandler.__handle_collectibles(world.collectibles, world.player)

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
