"""Defines a base upgrade for any weapon"""

from business.progression.interfaces import IUpgrade, IUpgradeValue

class Upgrade(IUpgrade):
    """An upgrade for the weapon"""

    MULTIPLY = 1
    ADD = 2
    SUBTRACT = 3
    DIVIDE = 4
    POWER = 5

    def __init__(self, data: dict):
        self.__values = data.values
        self.__description = data.description

    @property
    def values(self) -> list[IUpgradeValue]:
        return self.__values

    @property
    def description(self):
        return self.__description
