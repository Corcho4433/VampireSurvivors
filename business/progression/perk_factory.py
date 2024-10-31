"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.progression.interfaces import IPerkFactory, IWeaponStats
from business.world.interfaces import IGameWorld
from business.progression.perk import UpgradePerk
from business.weapons.weapon_stats import WeaponStats
from persistance.json_parser import JSONParser

class PerkFactory(IPerkFactory):
    """A perk factory used to create perks of any type"""

    def __init__(self, world: IGameWorld):
        self.__world: IGameWorld = world

    def create_hollow_hearth(self):
        #stats = PerkStats()
        upgrades = JSONParser.build_upgrades_for("hollow_heart")

        return UpgradePerk("Hollow Heart", stats, upgrades)
    
    def create_spinach(self):
        #stats = PerkStats()
        upgrades = JSONParser.build_upgrades_for("spinach")

        return UpgradePerk("Spinach", stats, upgrades)
