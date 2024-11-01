"""This module contains the implementation of the game world."""

import settings

from business.entities.interfaces import IBullet, IExperienceGem, IMonster, IPlayer
from business.world.interfaces import IGameWorld, IMonsterSpawner, ITileMap
from business.handlers.cooldown_handler import CooldownHandler
from business.world.gem_spawner import ExperienceGemFactory
from business.weapons.weapon_factory import WeaponFactory
from presentation.interfaces import IDisplay
from business.world.clock import Clock

class GameWorld(IGameWorld):
    """Represents the game world."""
    DEFAULT_MONSTER_SPAWN_TIME = 0.6

    def __init__(self, spawner: IMonsterSpawner, tile_map: ITileMap, player: IPlayer, display: IDisplay):
        # Initialize the player and lists for monsters, bullets and gems
        self.__player: IPlayer = player
        self.__monsters: list[IMonster] = []
        self.__bullets: list[IBullet] = []
        self.__experience_gems: list[IExperienceGem] = []
        self.__monster_spawner_cooldown: CooldownHandler = CooldownHandler(self.DEFAULT_MONSTER_SPAWN_TIME)
        self.__world_simulation_speed: int = 1
        self.__gem_factory = ExperienceGemFactory()
        self.__weapon_factory = WeaponFactory(self)
        self.__display: IDisplay = display
        self.__upgrading: bool = False
        self.__clock = Clock()

        self.__player.assign_world(self)

        # Initialize the tile map
        self.tile_map: ITileMap = tile_map

        # Initialize the monster spawner
        self.__monster_spawner: IMonsterSpawner = spawner

        #self.__player.give_weapon(self.__weapon_factory.create_gun())

    @property
    def clock_seconds(self):
        return self.__clock.time

    def update(self):
        self.player.update(self)

        for monster in self.monsters:
            monster.update(self)

        for bullet in self.bullets:
            bullet.update(self)

        for gem in self.experience_gems:
            gem.update(self)

        if self.__world_simulation_speed > 0:
            # when game is running
            self.__clock.count()

            if self.__monster_spawner_cooldown.is_action_ready():
                self.__monster_spawner_cooldown.put_on_cooldown()

                self.__monster_spawner.update(self)

    def set_upgrade_menu_active(self, state: bool):
        self.__upgrading = state
        self.__display.get_menu('Upgrade').set_active(state)

        if state:
            self.__pause()
        else:
            self.__resume()

    @property
    def upgrading(self):
        return self.__upgrading

    def add_monster(self, monster: IMonster):
        self.__monsters.append(monster)

    def remove_monster(self, monster: IMonster):
        self.__monsters.remove(monster)
        self.__gem_factory.create_gem(monster, self)

    def add_experience_gem(self, gem: IExperienceGem):
        self.__experience_gems.append(gem)

    def remove_experience_gem(self, gem: IExperienceGem):
        self.__experience_gems.remove(gem)

    def add_bullet(self, bullet: IBullet):
        self.__bullets.append(bullet)

    def remove_bullet(self, bullet: IBullet):
        self.__bullets.remove(bullet)

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
    def bullets(self) -> list[IBullet]:
        return self.__bullets[:]

    @property
    def experience_gems(self) -> list[IExperienceGem]:
        return self.__experience_gems[:]
