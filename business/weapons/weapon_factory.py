"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.weapons.interfaces import IWeaponFactory
from business.weapons.gun import Gun
from business.weapons.whip import Whip
from business.weapons.weapon_stats import WeaponStats
from business.handlers.data_handler import DataHandler
from business.exceptions import InvalidWeaponName

class WeaponFactory(IWeaponFactory):
    """A weapon factory used to create weapons of any type"""

    @staticmethod
    def create_weapon(name: str):
        match name:
            case 'gun':
                return WeaponFactory.__create_gun()
            case 'railgun':
                return WeaponFactory.__create_gun()
            case 'whip':
                return WeaponFactory.__create_whip()
            case _:
                raise InvalidWeaponName

    @staticmethod
    def __create_gun():
        stats = WeaponStats(damage=1, cooldown=1)

        return Gun(stats, DataHandler.build_upgrades_for_item('gun'))

    @staticmethod
    def __create_whip():
        stats = WeaponStats(damage=3, cooldown=2)

        return Whip(stats, DataHandler.build_upgrades_for_item('whip'))
