"""Defines the static class "ItemFactory" which creates both Perks & Weapons
    using the name as the key
"""

from business.weapons.weapon_factory import WeaponFactory
from business.progression.interfaces import IItemFactory
from business.progression.perk_factory import PerkFactory

from business.handlers.item_data_handler import ItemDataHandler

class ItemFactory(IItemFactory):
    """A static class that creates items"""

    @staticmethod
    def create_item(name: str):
        item_type = ItemDataHandler.get_item_type(name)

        match item_type:
            case 1:
                return WeaponFactory.create_weapon(name)
            case 2:
                return PerkFactory.create_perk(name)
