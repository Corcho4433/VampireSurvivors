"""Module for the CollisionHandler class."""

from typing import List

from business.entities.interfaces import IBullet, IExperienceGem, IHasSprite, IMonster, IPlayer, IMeleeAttack, IDistanceAttack, IChest, IHealingGem
from business.world.interfaces import IGameWorld


class CollisionHandler:
    """Handles collisions between entities in the game world."""

    @staticmethod
    def __collides_with(an_entity: IHasSprite, another_entity: IHasSprite):
        return an_entity.sprite.rect.colliderect(another_entity.sprite.rect)

    @staticmethod
    def __handle_attacks(world):
        attacks: List[IBullet] = world.attacks
        monsters: List[IMonster] = world.monsters

        bullet_attack_masks = {attack.sprite: attack.sprite.mask for attack in attacks if isinstance(attack, IDistanceAttack)}
        monster_masks = {monster.sprite: monster.sprite.mask for monster in monsters}

        for attack in attacks:
            if isinstance(attack, IMeleeAttack):
                attack.process_attack(world)

        for attack_sprite, attack_mask in bullet_attack_masks.items():
            for monster_sprite, monster_mask in monster_masks.items():
                # Check for overlap using masks

                if attack_mask.overlap(monster_mask, (monster_sprite.rect.x - attack_sprite.rect.x, monster_sprite.rect.y - attack_sprite.rect.y)):
                    attack = next((b for b in attacks if b.sprite == attack_sprite), None)
                    monster = next((m for m in monsters if m.sprite == monster_sprite), None)

                    if attack and monster:
                        monster.take_damage(attack.damage)  # Monster takes damage from the bullet
                        world.add_damage(attack.damage)

                        if isinstance(attack, IDistanceAttack):
                            attack.use_charge()


        #for attack in attacks:
        #    for monster in monsters:
        #        if CollisionHandler.__collides_with(attack, monster):
        #            monster.take_damage(attack.damage)
        #            if isinstance(attack, IDistanceAttack):
        #                attack.use_charge()

    @staticmethod
    def __handle_monsters(monsters: List[IMonster], player: IPlayer):
        pass

    @staticmethod
    def __handle_collectibles(collectibles: List[IExperienceGem], player: IPlayer):
        for collectible in collectibles:
            if CollisionHandler.__collides_with(collectible, player):
                if isinstance(collectible, IExperienceGem) or isinstance(collectible, IHealingGem):
                    player.pickup_gem(collectible)
                    collectible.pick()
                if isinstance(collectible, IChest):
                    print(collectible)
                    player.give_item(collectible.item)
                    player.apply_perks(heal=False)
                    collectible.pick()

    @staticmethod
    def handle_collisions(world: IGameWorld):
        """Handles collisions between entities in the game world.

        Args:
            world (IGameWorld): The game world.
        """
        CollisionHandler.__handle_attacks(world)
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
