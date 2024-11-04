"""Defines the class used by guns"""

from business.weapons.weapon import Weapon
from business.progression.interfaces import IPlayerStats
from business.weapons.interfaces import IWeaponStats
from business.entities.bullet import Bullet

class Gun(Weapon):
    """A gun that shoots bullets"""

    def __init__(self, stats: IWeaponStats, upgrades: list=[]): #pylint: disable=W0102
        super().__init__("gun", upgrades, stats)

    def attack(self, origin, world, player_stats: IPlayerStats):
        if not world.monsters or not self.cooldown_handler.is_action_ready():
            return

        # Find the nearest monster
        self.cooldown_handler.put_on_cooldown()
        bullet = Bullet(origin, self.__aim_at_target(origin, world), self.damage * player_stats.attack_damage)
        bullet.change_speed((bullet.original_speed + self.power) * self.speed)

        world.add_attack(bullet)

    def __aim_at_target(self, origin, world):
        monster = min(
            world.monsters,
            key=lambda monster: (monster.pos.distance_to(origin)),
        )

        return monster.pos
