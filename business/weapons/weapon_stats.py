"""Defines the class used for the weapon's stats"""

from business.weapons.interfaces import IWeaponStats

class WeaponStats(IWeaponStats):
    """The stats of a weapon used internally"""

    def __init__(self):
        self.__damage = 1

    @property
    def damage(self):
        return self.__damage
