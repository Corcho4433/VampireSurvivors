"""Defines the class used by guns"""

from business.weapons.weapon import Weapon
from business.progression.interfaces import IPlayerStats
from business.weapons.interfaces import IWeaponStats
from business.entities.bullet import Bullet

class Gun(Weapon):
    """A gun that shoots bullets"""

    def __init__(self, stats: IWeaponStats, player_stats: IPlayerStats):
        super().__init__("Gun", [], stats, player_stats)

        self.__player_stats = player_stats

    def attack(self, origin, world):
        if not world.monsters:
            return

        # Find the nearest monster

        bullet = Bullet(origin, self.__aim_at_target(origin, world), self.__player_stats.attack_damage)
        world.add_bullet(bullet)

    def __aim_at_target(self, origin, world):
        monster = min(
            world.monsters,
            key=lambda monster: (monster.pos.distance_to(origin)),
        )

        return monster.pos
