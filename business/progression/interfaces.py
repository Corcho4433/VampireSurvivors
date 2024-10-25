"""Defines all interfaces for the classes"""

from abc import ABC, abstractmethod

class IInventoryItem(ABC):
    """An item of the player's inventory"""

    @property
    @abstractmethod
    def level(self):
        """The current level of the item
        
            Returns:
                int: Level of the item
        """

    @abstractmethod
    def upgrade(self):
        """Increase the level of the item by 1"""

class IInventory(ABC):
    """The interface for a player's inventory"""

    @property
    @abstractmethod
    def limit(self) -> int:
        """The current max limit of objects that the inventory can have
        
            Returns:
                int: The limit of items
        """

    @abstractmethod
    def get_item(self, name: str) -> IInventoryItem:
        """Gets an item under the inventory by its name
        
            Returns:
                InventoryItem: an item from the user's inventory
        """

    @abstractmethod
    def add_item(self, item: IInventoryItem) -> None:
        """Adds an item to the inventory"""

class IPlayerStats(ABC):
    """The player's stats"""

    @property
    def luck(self) -> int:
        """The player's luck"""

    @property
    def health(self) -> int:
        """The health of the player"""

    @property
    def attack_damage(self) -> int:
        """The damage the player does per attack"""

    @property
    def attack_speed(self) -> int:
        """The speed of the attack"""

    @property
    def movement_speed(self) -> int:
        """The movement speed for each bullet"""

    @property
    def cooldown(self) -> int:
        """The cooldown the player has between each attack"""

class IUpgradeValue(ABC):
    """An upgraded value"""

    @property
    @abstractmethod
    def type(self):
        """The type of operation to do on a stat

            Returns:
                int: Enum of operation to do (1, 2, 3. etc)
        """

    @property
    @abstractmethod
    def stat(self):
        """The type of stat to modify from the weapon
        
            Returns:
                str: The name of the stat of the weapon to modify
        """

    @property
    @abstractmethod
    def value(self):
        """The value of the operation to do on the stat

            Returns:
                int
        """

class IUpgrade(ABC):
    """An upgrade for a weapon"""

    @property
    @abstractmethod
    def description(self) -> str:
        """The description of the upgrade
        
            Returns:
                str: The description of the upgrade
        """

    @property
    @abstractmethod
    def values(self) -> list[IUpgradeValue]:
        """All the values in the upgrade

            Returns:
                list[IUpgradeValue]: The values to upgrade from the weapon/item
        """

class IUpgradePerk(IInventoryItem):
    """A perk that upgrades the player's stats"""
