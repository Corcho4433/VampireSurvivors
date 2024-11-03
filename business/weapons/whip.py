"""Defines the class used by whips"""
from pygame import Vector2
from business.weapons.weapon import Weapon
from business.progression.interfaces import IPlayerStats
from business.weapons.interfaces import IWeaponStats, IAttack
from business.weapons.hitbox import Hitbox

class Whip(Weapon):
    """A whip that inflicts melee damage"""

    def __init__(self, stats: IWeaponStats, upgrades: list=[]): #pylint: disable=W0102
        super().__init__("whip", upgrades, stats)

    def attack(self, origin, world, player_stats: IPlayerStats):
        if not world.monsters:
            return

        # Find the nearest monster
        #attack = Attack(origin, self.__aim_at_target(origin, world), self.__player_stats.attack_damage)
        #bullet.change_speed((bullet.original_speed + self.power)* self.speed)
