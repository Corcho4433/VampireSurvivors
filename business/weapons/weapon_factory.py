"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.weapons.interfaces import IWeaponFactory
from business.weapons.gun import Gun
from business.weapons.whip import Whip
from business.weapons.weapon_stats import WeaponStats
from business.handlers.data_handler import DataHandler

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

    @staticmethod
    def __create_gun():
        stats = WeaponStats()

        return Gun(stats, DataHandler.build_upgrades_for_item('gun'))

    @staticmethod
    def __create_whip():
        stats = WeaponStats()

        return Whip(stats, DataHandler.build_upgrades_for_item('whip'))
