"""This module contains the implementation of the game world."""

import random
import settings

from business.entities.interfaces import IAttack, IBullet, IPickeable, IMonster, IPlayer
from business.world.interfaces import IGameWorld, IMonsterSpawner, ITileMap, IChestSpawner
from business.handlers.cooldown_handler import CooldownHandler
from business.world.collectible_factory import CollectibleFactory
#from business.weapons.weapon_factory import WeaponFactory
from business.world.clock import Clock

from presentation.interfaces import IDisplay

class GameWorld(IGameWorld):
    """Represents the game world."""
    DEFAULT_MONSTER_SPAWN_TIME = 4

    def __init__(self, monster_spawner: IMonsterSpawner, chest_spawner : IChestSpawner, tile_map: ITileMap, display: IDisplay):
        # Initialize the player and lists for monsters, bullets and gems
        self.__player: IPlayer = None
        self.__monsters: list[IMonster] = []
        self.__attacks: list[IAttack] = []
        self.__collectibles: list[IPickeable] = []
        self.__clock = Clock()
        self.__clock.set_time(0)

        self.__monster_spawner_cooldown: CooldownHandler = CooldownHandler(self.DEFAULT_MONSTER_SPAWN_TIME)
        self.__chest_spawner_cooldown: CooldownHandler = CooldownHandler(random.randint(40,70))
        self.__world_simulation_speed: int = 1
        self.__display: IDisplay = display
        self.__upgrading: bool = False
        self.__total_damage = 0
        self.__time_dead = 0

        # Initialize the tile map
        self.tile_map: ITileMap = tile_map

        # Initialize the monster spawner
        self.__monster_spawner: IMonsterSpawner = monster_spawner

        # Initialize the chest spawner
        self.__chest_spawner : IChestSpawner = chest_spawner

    def add_damage(self, damage: int):
        self.__total_damage += damage

    @property
    def total_damage(self):
        return round(self.__total_damage)

    def assign_player(self, player: IPlayer, clock_time: int=0):
        self.__player = player
        self.__clock.set_time(clock_time)
        self.__display.get_menu('HUD').update_inventory()

    @property
    def clock_seconds(self):
        return self.__clock.time

    def update(self):
        if self.player.health <= 0:
            self.__time_dead += 1/settings.FPS
            factor = min((self.__time_dead/1.5), 1)

            if self.__time_dead > 1.5 and not self.__display.get_menu("GameOver").active:
                self.__display.get_menu("GameOver").set_active(True)
            else:
                self.__display.get_menu("GameOver").set_bg_visibility(factor)

            self.__world_simulation_speed = self.__world_simulation_speed - self.__world_simulation_speed * factor

            return

        self.player.update(self)

        for monster in self.monsters:
            monster.update(self)

        for attack in self.attacks:
            attack.update(self)

        for collectible in self.collectibles:
            collectible.update(self)

        if self.__world_simulation_speed > 0:
            # when game is running
            self.__clock.count()

            if self.__monster_spawner_cooldown.is_action_ready():
                reduced_spawn_time = min(
                    (self.clock_seconds / 360) * self.DEFAULT_MONSTER_SPAWN_TIME,
                    self.DEFAULT_MONSTER_SPAWN_TIME - 0.06)

                self.__monster_spawner_cooldown.put_on_cooldown()
                self.__monster_spawner_cooldown.change_time(self.DEFAULT_MONSTER_SPAWN_TIME - reduced_spawn_time)

                self.__monster_spawner.update(self)

            if self.__chest_spawner_cooldown.is_action_ready():
                self.__chest_spawner_cooldown.put_on_cooldown()

                self.__chest_spawner_cooldown.change_time(random.randint(40,70))
                self.__chest_spawner.update(self)

    def set_upgrade_menu_active(self, state: bool):
        self.__upgrading = state
        self.__display.get_menu('Upgrade').set_active(state)

        if state:
            self.__pause()
        else:
            self.__display.get_menu('HUD').update_inventory()
            self.__resume()

    @property
    def upgrading(self):
        return self.__upgrading

    def add_monster(self, monster: IMonster):
        self.__monsters.append(monster)

    def remove_monster(self, monster: IMonster):
        if monster in self.__monsters:
            self.__monsters.remove(monster)

        CollectibleFactory.create_random_gem(monster, self)
        del monster

    def add_collectible(self, collectible: IPickeable):
        self.__collectibles.append(collectible)

    def remove_collectible(self, collectible: IPickeable):
        self.__collectibles.remove(collectible)
        self.__display.get_menu('HUD').update_inventory()

        del collectible

    def add_attack(self, attack: IAttack):
        self.__attacks.append(attack)

    def remove_attack(self, attack: IAttack):
        self.__attacks.remove(attack)

        del attack

    def __pause(self):
        self.__world_simulation_speed = 0

    def __resume(self):
        self.__world_simulation_speed = 1

    def toggle_pause(self):
        if self.__upgrading:
            return

        if self.__world_simulation_speed > 0:
            self.__display.get_menu("Pause").set_active(True)
            self.__pause()
        else:
            self.__display.get_menu("Pause").set_active(False)
            self.__resume()


    @property
    def player(self) -> IPlayer:
        return self.__player

    @property
    def simulation_speed(self):
        return self.__world_simulation_speed

    @property
    def monsters(self) -> list[IMonster]:
        return self.__monsters[:]

    @property
    def attacks(self) -> list[IBullet]:
        return self.__attacks[:]

    @property
    def collectibles(self) -> list[IPickeable]:
        return self.__collectibles[:]
