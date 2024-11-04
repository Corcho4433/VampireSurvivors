"""Defines the class WorldMock used to Mock the behavior of the
    GameWorld class
"""

from business.world.interfaces import IGameWorld

class GameWorldMock(IGameWorld):
    """The game world mock"""

    def add_damage(self, damage: int):
        pass

    @property
    def total_damage(self):
        return 0

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
        pass

    def remove_monster(self, monster):
        pass

    def add_collectible(self, collectible):
        pass

    def remove_collectible(self, collectible):
        pass

    def add_attack(self, attack):
        pass

    def remove_attack(self, attack):
        pass

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
        return []

    @property
    def attacks(self) -> list:
        return []

    @property
    def collectibles(self) -> list:
        return []

    def toggle_pause(self) -> None:
        pass