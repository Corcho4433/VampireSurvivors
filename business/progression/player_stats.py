"""Defines the class that the player uses as base stats"""

from business.progression.interfaces import IPlayerStats
from business.exceptions import InvalidStatValueException

class PlayerStats(IPlayerStats):
    """The stats for the player"""

    BASE_LUCK = 1
    BASE_HEALTH = 100
    BASE_ATTACK_DAMAGE = 10
    BASE_ATTACK_SPEED = 1
    BASE_SHOOT_COOLDOWN = 2
    BASE_MOVEMENT_SPEED = 1

    def __init__(self):
        self.__luck = self.BASE_LUCK
        self.__health = self.BASE_HEALTH
        self.__cooldown = self.BASE_SHOOT_COOLDOWN
        self.__attack_speed = self.BASE_ATTACK_SPEED
        self.__attack_damage = self.BASE_ATTACK_DAMAGE
        self.__movement_speed = self.BASE_MOVEMENT_SPEED

    @property
    def luck(self):
        return self.__luck

    @luck.setter
    def luck(self, new_luck: int):
        if new_luck < 0 or new_luck > 100:
            raise InvalidStatValueException("Invalid value given for luck")

        self.__luck = new_luck

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health: int):
        if new_health < 0:
            raise InvalidStatValueException("Invalid value given for health")

        self.__attack_damage = new_health

    @property
    def attack_damage(self):
        return self.__attack_damage

    @attack_damage.setter
    def attack_damage(self, new_attack_damage: int):
        if new_attack_damage < 0:
            raise InvalidStatValueException("Invalid value given for attack damage")

        self.__attack_damage = new_attack_damage

    @property
    def attack_speed(self):
        return self.__attack_speed

    @attack_speed.setter
    def attack_speed(self, new_attack_speed: int):
        if new_attack_speed < 0:
            raise InvalidStatValueException("Invalid value given for attack speed")

        self.__attack_speed = new_attack_speed

    @property
    def movement_speed(self):
        return self.__movement_speed

    @movement_speed.setter
    def movement_speed(self, new_movement_speed: int):
        if new_movement_speed < 0:
            raise InvalidStatValueException("Invalid value given for movement speed")

        return self.__movement_speed

    @property
    def cooldown(self):
        return self.__cooldown

    @cooldown.setter
    def cooldown(self, new_cooldown: int):
        if new_cooldown < 0:
            raise InvalidStatValueException("Invalid value given for cooldown")

        self.__cooldown = new_cooldown
