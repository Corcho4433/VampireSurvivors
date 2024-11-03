"""Defines all the interfaces for the handlers"""

from abc import ABC, abstractmethod

class IDataHandler(ABC):
    """"""

    @staticmethod
    @abstractmethod
    def build_upgrades_for_item(item_name: str):
        """Gets all the upgrades linked to certain item name
        
            Returns:
                list[Upgrade]: List of all the upgrades

        """

    @staticmethod
    @abstractmethod
    def build_monsters_from_last_save_file():
        """Builds all the monster objects using the last session saved data
        
            Returns:
                list[Monster]: List of all the monsters
        """