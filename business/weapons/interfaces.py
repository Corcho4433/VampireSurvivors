"""Defines all the interfaces for the classes used in weapons"""

from abc import ABC, abstractmethod

class IWeaponStats(ABC):
    """Stats for a weapon"""

    @property
    @abstractmethod
    def damage(self):
        """The base damage of the weapon stats"""

class IWeaponFactory(ABC):
    """Creates weapons"""

    @abstractmethod
    def create_gun(self, stats: IWeaponStats):
        """Creates a gun using the stats given"""
