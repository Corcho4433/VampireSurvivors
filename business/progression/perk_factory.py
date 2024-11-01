"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.progression.interfaces import IPerkFactory
from business.world.interfaces import IGameWorld
from business.progression.perk import Perk
from business.progression.player_stats import PlayerStats
from persistance.json_parser import JSONParser

class PerkFactory(IPerkFactory):
    """A perk factory used to create perks of any type"""

    def __init__(self, world: IGameWorld):
        self.__world: IGameWorld = world

    def create_perk(self, name: str):
        match name:
            case 'hollow_heart':
                return self.__create_hollow_heart()
            case 'clover':
                return self.__create_clover()
            case 'spinach':
                return self.__create_spinach()

    def __create_hollow_heart(self) -> Perk:
        stats = PlayerStats(health=1.2)
        upgrades = JSONParser.build_upgrades_for("hollow_heart")

        return Perk("Hollow Heart", stats, upgrades)

    def __create_spinach(self) -> Perk:
        stats = PlayerStats(attack_damage=1.2)
        upgrades = JSONParser.build_upgrades_for("spinach")

        return Perk("Spinach", stats, upgrades)

    def __create_clover(self) -> Perk:
        stats = PlayerStats(luck=1.2)
        upgrades = JSONParser.build_upgrades_for("clover")

        return Perk("Clover", stats, upgrades)
