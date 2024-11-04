"""Defines the class used by whips"""

from business.weapons.weapon import Weapon
from business.progression.interfaces import IPlayerStats
from business.weapons.interfaces import IWeaponStats
from business.weapons.attack_whip import AttackWhip

class Whip(Weapon):
    """A whip that inflicts melee damage"""

    def __init__(self, stats: IWeaponStats, upgrades: list=[]): #pylint: disable=W0102
        super().__init__("whip", upgrades, stats)

    def attack(self, origin, world, player_stats: IPlayerStats):
        if not world.monsters or not self.cooldown_handler.is_action_ready():
            return

        self.cooldown_handler.put_on_cooldown()
        attack = AttackWhip(origin, self.damage * player_stats.attack_damage, self.range)

        world.add_attack(attack)
