"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.progression.interfaces import IPerkFactory
from business.world.interfaces import IGameWorld
from business.progression.perk import UpgradePerk
from business.progression.player_stats import PlayerStats
from persistance.json_parser import JSONParser

class PerkFactory(IPerkFactory):
    """A perk factory used to create perks of any type"""

    def __init__(self, world: IGameWorld):
        self.__world: IGameWorld = world

    def create_hollow_hearth(self):
        stats = PlayerStats()
        upgrades = JSONParser.build_upgrades_for("hollow_heart")

        return UpgradePerk("Hollow Heart", stats, upgrades)

    def create_spinach(self):
        stats = PlayerStats()
        upgrades = JSONParser.build_upgrades_for("spinach")

        return UpgradePerk("Spinach", stats, upgrades)

    def create_clover(self):
        stats = PlayerStats()
        upgrades = JSONParser.build_upgrades_for("clover")

        return UpgradePerk("Clover", stats, upgrades)
