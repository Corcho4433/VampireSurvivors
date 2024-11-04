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
        self.__cooldown_handler = CooldownHandler(self.__weapon_stats.cooldown)

    @property
    def cooldown_handler(self):
        """The cooldown handler for the weapon"""

        return self.__cooldown_handler

    @property
    def damage(self):
        return self.__weapon_stats.damage

    @property
    def cooldown(self):
        return self.__weapon_stats.cooldown

    @property
    def speed(self):
        return self.__weapon_stats.speed

    @property
    def power(self):
        return self.__weapon_stats.power

    @property
    def range(self):
        return self.__weapon_stats.range

    def change_stat(self, name: str, new_value: float | int):
        self.__weapon_stats.change_stat(name, new_value)

        self.__cooldown_handler.change_time(self.__weapon_stats.cooldown)
