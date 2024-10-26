"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.weapons.interfaces import IWeaponFactory, IWeaponStats
from business.world.interfaces import IGameWorld
from business.weapons.gun import Gun
from business.weapons.weapon_stats import WeaponStats
from persistance.json_parser import JSONParser

class WeaponFactory(IWeaponFactory):
    """A weapon factory used to create weapons of any type"""

    def __init__(self, world: IGameWorld):
        self.__world: IGameWorld = world

    def create_gun(self, stats: IWeaponStats=WeaponStats()):
        player_stats = self.__world.player.stats

        return Gun(stats, player_stats, JSONParser.build_upgrades_for('default_gun'))
