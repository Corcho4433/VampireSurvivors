"""This module contains interfaces for the game world."""

from abc import ABC, abstractmethod

from business.entities.interfaces import IMonster, IPlayer
from business.entities.interfaces import ICollectible


class IGameWorld(ABC):
    """Interface for the game world.

    The game world is the environment in which the game entities exist.
    """

    @abstractmethod
    def add_damage(self, damage: int):
        """Add a damage amount to the total damage of the game"""

    @property
    @abstractmethod
    def total_damage(self):
        """The total damage dealt in the game"""

    @abstractmethod
    def assign_player(self, player, clock_time: int):
        """Assign a player to the world
        
            Args:
                player (Player): The player instance to give the world
                clock_time (int=0): The clock time to start with
        """

    @property
    @abstractmethod
    def clock_seconds(self):
        """The amount of seconds passed since the game started"""

    @property
    @abstractmethod
    def upgrading(self):
        """Whether the upgrading menu is active or not"""

    @abstractmethod
    def set_upgrade_menu_active(self, state: bool):
        """Sets whether or not the upgrade menu is active"""

    @abstractmethod
    def add_monster(self, monster: IMonster):
        """Adds a monster to the world.

        Args:
            monster (IMonster): The monster to add.
        """

    @abstractmethod
    def remove_monster(self, monster: IMonster):
        """Removes a monster from the world.

        Args:
            monster (IMonster): The monster to remove.
        """

    @abstractmethod
    def add_collectible(self, collectible: ICollectible):
        """Adds a collectible to the world.

        Args:
            collectible (IPickable): The collectible to add.
        """

    @abstractmethod
    def remove_collectible(self, collectible: ICollectible):
        """Removes a collectible from the world.

        Args:
            collectible (IPickable): The collectible to remove.
        """

    @abstractmethod
    def add_attack(self, attack):
        """Adds an attack to the world.

        Args:
            attack (IAttack): The attack to add.
        """

    @abstractmethod
    def remove_attack(self, attack):
        """Removes a attack from the world.

        Args:
            attack (IAttack): The attack to remove.
        """

    @abstractmethod
    def update(self):
        """Updates the state of the world and all updatable entities within it."""

    @property
    @abstractmethod
    def player(self) -> IPlayer:
        """Gets the player entity.

        Returns:
            IPlayer: The player entity.
        """

    @property
    @abstractmethod
    def simulation_speed(self) -> int:
        """Gets the current simulation speed
        
        Returns:
            int: The speed of the simulation
        """

    @property
    @abstractmethod
    def monsters(self) -> list[IMonster]:
        """Gets the list of monsters in the world.

        Returns:
            list[IMonster]: A copy of the list of monsters in the world.
        """

    @property
    @abstractmethod
    def attacks(self) -> list:
        """Gets the list of attacks in the world.

        Returns:
            list[IAttack]: A copy of the list of attacks in the world.
        """

    @property
    @abstractmethod
    def collectibles(self) -> list:
        """Gets the list of collectibles in the world.

        Returns:
            list[IPickable]: A copy of the list of collectibles in the world.
        """

    @abstractmethod
    def toggle_pause(self) -> None:
        """Toggles the game pause state from true to false or viceversa"""


class IUpdatable(ABC):
    """Interface for entities that can be updated."""

    @abstractmethod
    def update(self, world: IGameWorld):
        """Updates the state of the entity.

        Args:
            world (IGameWorld): The game world in which the entity exists.
        """

class IChestSpawner(IUpdatable):
    """Interface for a chest spawner.
    
    A chest spawner is responsible for spawning chests in the game world."""

    @abstractmethod
    def spawn_chest(self, world: IGameWorld):
        """Spawns a chest in the game world.

        Args:
            world (IGameWorld): The game world in which to spawn the chest.
        """

class IMonsterSpawner(IUpdatable):
    """Interface for a monster spawner.

    A monster spawner is responsible for spawning monsters in the game world.
    """

    @abstractmethod
    def spawn_monster(self, world: IGameWorld):
        """Spawns a monster in the game world.

        Args:
            world (IGameWorld): The game world in which to spawn the monster.
        """


class ITileMap(ABC):
    """Interface for a tile map.

    A tile map is a grid of tiles that make up the game world.
    Each tile has a value that represents the type of terrain or object at that location.
    """

    @abstractmethod
    def get(self, row, col) -> int:
        """Gets the tile at the specified row and column.

        Args:
            row (int): The row of the tile.
            col (int): The column of the tile.

        Returns:
            int: The tile at the specified row and column.
        """


class ICollectibleFactory(ABC):
    """A gem factory that creates gems from monsters"""

    @staticmethod
    @abstractmethod
    def create_collectible(name: str, pos):
        """Create a gem based on the name given and the position"""

    @staticmethod
    @abstractmethod
    def create_random_gem(monster: IMonster, world: IGameWorld):
        """Creates a gem using the monster as factor"""

class IClock(ABC):
    """The global clock measuring in game time in seconds"""

    @property
    @abstractmethod
    def time(self):
        """The current time of the clock"""

    @abstractmethod
    def count(self):
        """Count the time passed, equal to method update"""

    @abstractmethod
    def set_time(self, new_time: int):
        """Should only be called by data classes
        
            Args:
                new_time (int): The new time of the clock
        """
