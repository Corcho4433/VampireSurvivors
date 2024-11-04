"""Defines the root class for a weapon"""

from business.progression.item import InventoryItem
from business.progression.interfaces import IWeapon, IUpgrade
from business.weapons.interfaces import IWeaponStats
from business.handlers.cooldown_handler import CooldownHandler

class Weapon(InventoryItem, IWeapon):
    """A weapon used by the player"""

    def __init__(self, name: str, upgrades: list[IUpgrade], weapon_stats: IWeaponStats):
        super().__init__(name, InventoryItem.TYPES['WEAPON'], upgrades)

        self.__weapon_stats: IWeaponStats = weapon_stats
        self.__cooldown = CooldownHandler(self.__weapon_stats.cooldown)

    @property
    def cooldown(self):
        return self.__cooldown

    @property
    def damage(self):
        return self.__weapon_stats.damage

    @property
    def speed(self):
        return self.__weapon_stats.speed

    @property
    def power(self):
        return self.__weapon_stats.power

    def change_stat(self, name: str, new_value: float | int):
        self.__weapon_stats.change_stat(name, new_value)

        self.__cooldown.change_time(self.__weapon_stats.cooldown)

    def upgrade(self):
        super().upgrade()

        current_level = self.level

        if current_level <= len(self.upgrades):
            current_upgrade: IUpgrade = self.upgrades[current_level - 2]

            current_upgrade.apply(self)
