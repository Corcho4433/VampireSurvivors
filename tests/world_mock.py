"""Defines the class WorldMock used to Mock the behavior of the
    GameWorld class
"""

from business.world.interfaces import IGameWorld

class GameWorldMock(IGameWorld):
    """The game world mock"""

    def __init__(self):
        self.__attacks = []
        self.__monsters = []
        self.__total_damage = 0

    def add_damage(self, damage: int):
        self.__total_damage += damage

    @property
    def total_damage(self):
        return self.__total_damage

    def assign_player(self, player, clock_time: int):
        pass

    @property
    def clock_seconds(self):
        return 0

    @property
    def upgrading(self):
        return False

    def set_upgrade_menu_active(self, state: bool):
        pass

    def add_monster(self, monster):
        self.__monsters.append(monster)

    def remove_monster(self, monster):
        self.__monsters.append(monster)

    def add_collectible(self, collectible):
        pass

    def remove_collectible(self, collectible):
        pass

    def add_attack(self, attack):
        self.__attacks.append(attack)

    def remove_attack(self, attack):
        self.__attacks.remove(attack)

    def update(self):
        pass

    @property
    def player(self):
        return

    @property
    def simulation_speed(self) -> int:
        return 1

    @property
    def monsters(self) -> list:
        return self.__monsters[:]

    @property
    def attacks(self) -> list:
        return self.__attacks[:]

    @property
    def collectibles(self) -> list:
        return []

    def toggle_pause(self) -> None:
        pass