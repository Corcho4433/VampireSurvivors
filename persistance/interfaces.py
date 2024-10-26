"""Defines all the interfaces for the persistance layer"""

from abc import ABC, abstractmethod

class IJSONParser(ABC):
    """General JSON data parser"""

    @staticmethod
    @abstractmethod
    def build_upgrade_from(data: str):
        """Builds an upgrade object from data"""
