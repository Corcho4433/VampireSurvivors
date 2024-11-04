"""Defines the class used in the player's inventory"""

from business.progression.item import InventoryItem
from business.progression.interfaces import IUpgradePerk, IUpgrade, IPlayerStats
from business.exceptions import InvalidStatValueException

class Perk(InventoryItem, IUpgradePerk):
    """An item from the inventory"""

    def __init__(self, name: str, base_stats: IPlayerStats, upgrades: list[IUpgrade]):
        super().__init__(name, InventoryItem.TYPES['PERK'], upgrades)

        self.__player_stats: IPlayerStats = base_stats

    def change_stat(self, name: str, value: int):
        if value < 0:
            raise InvalidStatValueException

        match name:
            case 'luck':
                self.__player_stats.luck = value
            case 'health':
                self.__player_stats.health = value
            case 'cooldown':
                self.__player_stats.cooldown = value
            case 'attack_speed':
                self.__player_stats.attack_speed = value
            case 'attack_damage':
                self.__player_stats.attack_damage = value
            case 'movement_speed':
                self.__player_stats.movement_speed = value
                print(self.__player_stats.movement_speed, value)

    @property
    def stats(self):
        return self.__player_stats

    def get_stat(self, name: str):
        if hasattr(self.stats, name):
            return getattr(self.stats, name)
