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
