"""Defines all the interfaces for the persistance layer"""

from abc import ABC, abstractmethod

class IUpgradeDataHandler(ABC):
    """General JSON data parser"""

    @staticmethod
    @abstractmethod
    def get_item_upgrades(item_name: str):
        """Gets the data for an item's upgrades"""

class MonsterDAO(ABC):
    """A monster Data-Access-Object used to save data for monsters"""

    @abstractmethod
    def get_all_monsters(self):
        """Get all the monsters in the DAO data"""

    @abstractmethod
    def create_monster(self, monster):
        """Add a monster to the DAO data"""

class PlayerDAO(ABC):
    """A player Data-Access-Object used to save data for the player"""

    @abstractmethod
    def get_player(self):
        """Get the player from the DAO data"""

    @abstractmethod
    def add_player(self, player):
        """Add the player to the DAO data"""

class InventoryDAO(ABC):
    """A player Data-Access-Object used to save data for the player"""

    @abstractmethod
    def get_inventory(self):
        """Gets the inventory object"""   

    @abstractmethod
    def add_item(self, item):
        """Add an item to the DAO data"""
