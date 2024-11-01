"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.weapons.interfaces import IWeaponFactory
from business.world.interfaces import IGameWorld
from business.weapons.gun import Gun
from business.weapons.whip import Whip
from business.weapons.weapon_stats import WeaponStats
from persistance.json_parser import JSONParser

class WeaponFactory(IWeaponFactory):
    """A weapon factory used to create weapons of any type"""

    def __init__(self, world: IGameWorld):
        self.__world: IGameWorld = world

    def create_weapon(self, name: str):
        match name:
            case 'gun':
                return self.__create_gun()
            case 'railgun':
                return self.__create_gun()
            case 'whip':
                return self.__create_whip()

    def __create_gun(self):
        player_stats = self.__world.player.stats
        stats = WeaponStats()

        return Gun(stats, player_stats, JSONParser.build_upgrades_for('default_gun'))

    def __create_whip(self):
        player_stats = self.__world.player.stats
        stats = WeaponStats()

        return Whip(stats, player_stats, JSONParser.build_upgrades_for('default_whip'))
