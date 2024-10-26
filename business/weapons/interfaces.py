"""Defines all the interfaces for the classes used in weapons"""

from abc import ABC, abstractmethod

class IWeaponStats(ABC):
    """Stats for a weapon"""

    @property
    @abstractmethod
    def damage(self):
        """The base damage of the weapon stats"""

    @property
    @abstractmethod
    def speed(self):
        """The base speed of the weapon stats"""

    @property
    @abstractmethod
    def power(self):
        """The amplified power of an attack"""

    @abstractmethod
    def change_stat(self, name: str, new_value: float | int):
        """Changes a statistic to match a new value"""

class IWeaponFactory(ABC):
    """Creates weapons"""

    @abstractmethod
    def create_gun(self, stats: IWeaponStats):
        """Creates a gun using the stats given"""
