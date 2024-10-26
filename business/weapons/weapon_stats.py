"""Defines the class used for the weapon's stats"""

from business.weapons.interfaces import IWeaponStats
from business.exceptions import InvalidStatValueException, InvalidStatNameException

class WeaponStats(IWeaponStats):
    """The stats of a weapon used internally"""

    def __init__(self):
        self.__damage = 1
        self.__speed = 1
        self.__power = 0

    @property
    def damage(self):
        return self.__damage

    @property
    def speed(self):
        return self.__speed

    @property
    def power(self):
        return self.__power

    def change_stat(self, name: str, new_value: int | float):
        if new_value < 0:
            raise InvalidStatValueException(f"Invalid value given to stat: {name}")

        match name:
            case 'damage':
                self.__damage = new_value
            case 'speed':
                self.__speed = new_value
            case 'power':
                self.__power = new_value
            case _:
                raise InvalidStatNameException
