"""Defines the root class for a weapon"""

from business.progression.item import InventoryItem

class Weapon(InventoryItem):
    """A weapon used by the player"""

    def __init__(self, name: str):
        super().__init__(name)
