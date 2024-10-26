"""Defines all interfaces for the classes"""

from abc import ABC, abstractmethod

class IUpgradeable(ABC):
    """An upgradeable item with a level count"""

    @property
    @abstractmethod
    def upgrades(self):
        """The upgrades for the item"""

    @abstractmethod
    def upgrade(self):
        """Upgrades the weapon by one level"""

    @property
    @abstractmethod
    def level(self):
        """The level of the weapon

            Returns:
                int: the level of the weapon
        """

class IInventoryItem(IUpgradeable):
    """An item of the player's inventory"""

    @property
    @abstractmethod
    def name(self):
        """The name of the item"""

class IWeapon(IInventoryItem):
    """A weapon the player can use"""

    @abstractmethod
    def attack(self, origin, world):
        """Uses the weapon to attack from a certain origin spot"""

    @property
    @abstractmethod
    def damage(self):
        """The amount of damage an attack does
        
            Returns:
                int: the damage count
        """

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

    @abstractmethod
    def apply(self, item: IInventoryItem):
        """Applies the upgrade onto an inventory item
        
            Args:
                InventoryItem: item to upgrade
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

