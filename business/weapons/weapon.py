"""Defines the root class for a weapon"""

from business.progression.item import InventoryItem
from business.progression.interfaces import IWeapon, IUpgrade, IPlayerStats
from business.weapons.interfaces import IWeaponStats

class Weapon(InventoryItem, IWeapon):
    """A weapon used by the player"""

    def __init__(self, name: str, upgrades: list[IUpgrade], weapon_stats: IWeaponStats, player_stats: IPlayerStats):
        super().__init__(name, upgrades)

        self.__weapon_stats: IWeaponStats = weapon_stats
        self.__player_stats: IPlayerStats = player_stats

    @property
    def damage(self):
        return self.__weapon_stats.damage * self.__player_stats.attack_damage

    def upgrade(self):
        super().upgrade()

        current_level = self.level
        print(current_level)

        if current_level <= len(self.upgrades):
            current_upgrade = self.upgrades[current_level - 1]

            print(current_upgrade)
