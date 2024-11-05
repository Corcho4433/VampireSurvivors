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
        """Upgrades the item by one level"""

    @property
    @abstractmethod
    def level(self):
        """The level of the item

            Returns:
                int: the level of the item
        """

class IInventoryItem(IUpgradeable):
    """An item of the player's inventory"""

    @property
    @abstractmethod
    def name(self):
        """The name of the item"""

    @property
    @abstractmethod
    def item_type(self):
        """The type of the item

            Returns:
                str: "Perk" or "Weapon"
        """

    @abstractmethod
    def get_stat(self, name: str):
        """Gets the value of a stat by the specified name
        
            Args:
                name (str): The name of the stat to search for
        """

class IWeapon(IInventoryItem):
    """A weapon the player can use"""

    @abstractmethod
    def change_stat(self, name: str, new_value: float | int):
        """Changes a statistic to fit a specific number"""

    @abstractmethod
    def attack(self, origin, world, player_stats):
        """Uses the weapon to attack from a certain origin spot"""

    @property
    @abstractmethod
    def cooldown(self):
        """The cooldown handler for teh weapon"""

    @property
    @abstractmethod
    def damage(self):
        """The amount of damage an attack does
        
            Returns:
                int: the damage count
        """

    @property
    @abstractmethod
    def range(self):
        """The range multiplier of the attack's size for the weapon
        
            Returns:
                int: The multiplier
        """

    @property
    @abstractmethod
    def speed(self):
        """The speed of an attack
        
            Returns:
                int: the speed multiplier
        """

    @property
    @abstractmethod
    def power(self):
        """The amplified power of an attack
        
            Returns:
                int: the power amplifier
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

    @property
    @abstractmethod
    def item_count(self):
        """The current amount of items in the inventory
        
            Returns:
                int: The amount of items inside the inventory
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


    @abstractmethod
    def get_weapons(self):
        """Returns all the weapons of the player"""

    @abstractmethod
    def get_perks(self):
        """Returns all the perks of the player"""

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

    @abstractmethod
    def change_stat(self, name: str, value: int):
        """Changes one of the perk's stat values"""


class IPerkFactory(ABC):
    """Creates perks"""

    @staticmethod
    @abstractmethod
    def create_perk(name: str):
        """Creates a perk using a name as base"""


class IItemFactory(ABC):
    """An item factory object that creates items"""

    @staticmethod
    @abstractmethod
    def create_item(name: str):
        """Creates an item given the name of it"""