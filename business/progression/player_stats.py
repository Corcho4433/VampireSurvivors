"""Defines the class that the player uses as base stats"""

from business.progression.interfaces import IPlayerStats
from business.exceptions import InvalidStatValueException

class PlayerStats(IPlayerStats):
    """The stats for the player"""

    BASE_LUCK = 1
    BASE_HEALTH = 1
    BASE_ATTACK_DAMAGE = 1
    BASE_ATTACK_SPEED = 1
    BASE_ATTACK_COOLDOWN = 2
    BASE_MOVEMENT_SPEED = 1

    def __init__(self, health: int=BASE_HEALTH,
                 attack_damage: int=BASE_ATTACK_DAMAGE,
                 movement_speed: int=BASE_MOVEMENT_SPEED,
                 luck: int=BASE_LUCK,
                 cooldown: int=BASE_ATTACK_COOLDOWN,
                 attack_speed: int=BASE_ATTACK_SPEED):
        self.__luck = luck
        self.__health = health
        self.__cooldown = cooldown
        self.__attack_speed = attack_speed
        self.__attack_damage = attack_damage
        self.__movement_speed = movement_speed

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

        self.__health = new_health

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


    def __mul__(self, other_player_stats: 'PlayerStats'):
        if isinstance(other_player_stats, PlayerStats):
            return PlayerStats(
                self.health * other_player_stats.health,
                self.attack_damage * other_player_stats.attack_damage,
                self.movement_speed * other_player_stats.movement_speed,
                self.luck * other_player_stats.luck,
                self.cooldown * other_player_stats.cooldown,
                self.attack_speed * other_player_stats.attack_speed,
            )
        elif type(other_player_stats) == int:
            return PlayerStats(self.health * other_player_stats,
                               self.attack_damage * other_player_stats,
                               self.movement_speed * other_player_stats,
                               self.luck * other_player_stats,
                               self.cooldown * other_player_stats,
                               self.attack_speed * other_player_stats,)