"""Defines the class used for the weapon's stats"""

from business.weapons.interfaces import IWeaponStats
from business.exceptions import InvalidStatValueException, InvalidStatNameException

class WeaponStats(IWeaponStats):
    """The stats of a weapon used internally"""

    BASE_DAMAGE = 1
    BASE_SPEED = 1
    BASE_POWER = 0
    BASE_COOLDOWN = 10

    def __init__(self, damage=BASE_DAMAGE, speed=BASE_SPEED, power=BASE_DAMAGE, cooldown=BASE_COOLDOWN):
        self.__damage = damage
        self.__speed = speed
        self.__power = power
        self.__cooldown = cooldown

    @property
    def cooldown(self):
        return self.__cooldown

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
            case 'cooldown':
                self.__cooldown = new_value
            case _:
                raise InvalidStatNameException
