"""Defines a factory to create weapons such as Gun/Sword, etc."""

from business.progression.interfaces import IPerkFactory
from business.progression.perk import Perk
from business.progression.player_stats import PlayerStats
from business.handlers.data_handler import DataHandler

class PerkFactory(IPerkFactory):
    """A perk factory used to create perks of any type"""

    @staticmethod
    def create_perk(name: str):
        match name:
            case 'hollow_heart':
                return PerkFactory.__create_hollow_heart()
            case 'clover':
                return PerkFactory.__create_clover()
            case 'spinach':
                return PerkFactory.__create_spinach()

    @staticmethod
    def __create_hollow_heart() -> Perk:
        stats = PlayerStats(health=1.2)
        upgrades = DataHandler.build_upgrades_for_item("hollow_heart")

        return Perk("Hollow Heart", stats, upgrades)

    @staticmethod
    def __create_spinach() -> Perk:
        stats = PlayerStats(attack_damage=1.2)
        upgrades = DataHandler.build_upgrades_for_item("spinach")

        return Perk("Spinach", stats, upgrades)

    @staticmethod
    def __create_clover() -> Perk:
        stats = PlayerStats(luck=1.2)
        upgrades = DataHandler.build_upgrades_for_item("clover")

        return Perk("Clover", stats, upgrades)
