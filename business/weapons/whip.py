"""Defines the class used by whips"""

from business.weapons.weapon import Weapon
from business.progression.interfaces import IPlayerStats
from business.weapons.interfaces import IWeaponStats
from business.entities.interfaces import IAttack

class Whip(Weapon):
    """A whip that inflicts melee damage"""

    def __init__(self, stats: IWeaponStats, player_stats: IPlayerStats, upgrades: list=[]): #pylint: disable=W0102
        super().__init__("Whip", upgrades, stats, player_stats)

        self.__player_stats = player_stats

    def attack(self, origin, world):
        if not world.monsters:
            return

        # Find the nearest monster

        bullet = Bullet(origin, self.__aim_at_target(origin, world), self.__player_stats.attack_damage)
        bullet.change_speed((bullet.original_speed + self.power)* self.speed)


    def __aim_at_target(self, origin, world):
        monster = min(
            world.monsters,
            key=lambda monster: (monster.pos.distance_to(origin)),
        )

        return monster.pos
