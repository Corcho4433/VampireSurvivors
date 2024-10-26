"""Defines all the interfaces for the persistance layer"""

from abc import ABC, abstractmethod

class IJSONParser(ABC):
    """General JSON data parser"""

    @staticmethod
    @abstractmethod
    def build_upgrades_for(weapon_name: str):
        """Builds an upgrade object from a weapon's name"""
