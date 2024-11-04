"""Defines all the interfaces for the persistance layer"""

from abc import ABC, abstractmethod

class IItemDataHandler(ABC):
    """General JSON data parser"""

    @staticmethod
    @abstractmethod
    def get_item_upgrades(item_name: str):
        """Gets the data for an item's upgrades"""

    @staticmethod
    @abstractmethod
    def get_all_items():
        """A list of all the items in-game"""

    @staticmethod
    @abstractmethod
    def get_item_type(name: str):
        """The type of a given item"""

class MonsterDAO(ABC):
    """A monster Data-Access-Object used to save data for monsters"""

    @abstractmethod
    def get_all_monsters(self):
        """Get all the monsters in the DAO data"""

    @abstractmethod
    def clear_monsters(self):
        """Clears the DAO monster object"""

    @abstractmethod
    def add_monster(self, monster):
        """Add a monster to the DAO data"""

class CollectibleDAO(ABC):
    """A collectible Data-Access-Object used to save data for collectibles"""

    @abstractmethod
    def get_all_collectibles(self):
        """Get all the collectibles in the DAO data"""

    @abstractmethod
    def clear_collectibles(self):
        """Clears the DAO collectibles object"""

    @abstractmethod
    def add_collectible(self, collectible):
        """Add a collectible to the DAO data"""


class AttackDAO(ABC):
    """An attack Data-Access-Object used to save data for attacks"""

    @abstractmethod
    def get_all_attacks(self):
        """Get all the attacks in the DAO data"""

    @abstractmethod
    def clear_attacks(self):
        """Clears the DAO attacks object"""

    @abstractmethod
    def add_attack(self, attack):
        """Add an attack to the DAO data"""



class PlayerDAO(ABC):
    """A player Data-Access-Object used to save data for the player"""

    @abstractmethod
    def get_player(self):
        """Get the player from the DAO data"""

    @abstractmethod
    def get_time(self):
        """Get the time of the last session"""

    @abstractmethod
    def add_player(self, player):
        """Add the player to the DAO data"""

class InventoryDAO(ABC):
    """A player Data-Access-Object used to save data for the player"""

    @abstractmethod
    def get_inventory(self):
        """Gets the inventory object"""   

    @abstractmethod
    def clear_inventory(self):
        """Clears the DAO inventory object"""

    @abstractmethod
    def add_item(self, item):
        """Add an item to the DAO data"""
