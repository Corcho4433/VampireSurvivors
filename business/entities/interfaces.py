"""This module contains interfaces for the entities in the game."""

from abc import ABC, abstractmethod
from pygame import Vector2

from presentation.sprite import Sprite


class ICanDealDamage(ABC):
    """Interface for entities that can deal damage."""

    @property
    @abstractmethod
    def damage(self) -> int:
        """The amount of damage the entity can deal.

        Returns:
            int: The amount of damage the entity can deal.
        """

class IPickeable(ABC):
    """Interface for entities that can be picked."""

    @property
    @abstractmethod
    def is_picked(self) -> int:
        """Whether the entity has been picked up or not.

        Returns:
            bool: Picked or not picked.
        """

    @abstractmethod
    def pick(self) -> None:
        """Set the entity as picked.
        
        """

class IDamageable(ABC):
    """Interface for entities that can take damage."""

    @property
    @abstractmethod
    def health(self) -> int:
        """The health of the entity.

        Returns:
            int: The health of the entity.
        """

    @abstractmethod
    def take_damage(self, amount: int):
        """Take damage.

        Args:
            amount (int): The amount of damage to take.
        """


class IUpdatable(ABC):
    """Interface for entities that can be updated."""

    @abstractmethod
    def update(self, world):
        """Update the state of the entity."""


class IHasSprite(ABC):
    """Interface for entities that have a sprite."""

    @property
    @abstractmethod
    def sprite(self) -> Sprite:
        """The sprite of the entity.

        Returns:
            Sprite: The sprite of the entity.
        """


class IHasPosition(IHasSprite):
    """Interface for entities that have a position."""

    @property
    @abstractmethod
    def pos(self) -> Vector2:
        """The coordinates of the entity. (x, y)

        Returns:
            vector2: The coordinates of the entity (x, y)
        """


class ICanMove(IHasPosition):
    """Interface for entities that can move."""

    @property
    @abstractmethod
    def speed(self) -> float:
        """The speed of the entity.

        Returns:
            float: The speed of the entity.
        """

    @property
    @abstractmethod
    def original_speed(self) -> float:
        """The original speed of the entity, before any changes
        
            Returns:
                float: The original speed of the entity.
        """

    @abstractmethod
    def change_speed(self, speed: int):
        """Changes the speed of the moving entity"""

    @abstractmethod
    def move(self, direction: tuple[int, int]):
        """Move the entity in the given direction based on its speed.

        This method should update the entity's position and sprite.

        Args:
            direction_x (float): The direction in x-coordinate.
            direction_y (float): The direction in y-coordinate.
        """


class IMonster(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for monster entities."""

    @property
    @abstractmethod
    def type(self):
        """The monster type"""


class IHasCharges:
    """Interface that determines that an object"""

    @property
    @abstractmethod
    def charges_remaining(self):
        """The remaining amount of charges"""

    def use_charge(self, amount: int):
        """Reduces the amount of charges by 1 or amount"""

class IBullet(IUpdatable, ICanMove, IHasCharges, ICanDealDamage):
    """Interface for bullet entities."""

class ICollectible(IUpdatable, IHasPosition, IPickeable):
    """A collectible item"""

    @property
    @abstractmethod
    def type(self):
        """The type of collectible

            Returns:
                str: "ExperienceGem"
        """

class IExperienceGem(ICollectible):
    """Interface for experience gem entities."""

    @property
    @abstractmethod
    def amount(self) -> int:
        """The amount of experience the gem gives.

        Returns:
            int: The amount of experience the gem gives.
        """

class IPlayer(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for the player entity."""

    @abstractmethod
    def apply_perks(self):
        """Applies all the perks the player currently possesses in it's inventory
            and changes all the stats
        """

    @abstractmethod
    def pickup_gem(self, gem: IExperienceGem):
        """Picks up an experience gem.

        Args:
            gem (IExperienceGem): The experience gem to pick up.
        """

    @property
    @abstractmethod
    def stats(self):
        """The stats of the player generalized
        
            Returns:
                PlayerStats: the player stats object
        """

    @property
    @abstractmethod
    def luck(self) -> int:
        """The luck level of the player"""

    @property
    @abstractmethod
    def inventory(self):
        """The player's inventory, holding items/perks

            Returns:
                Inventory: the player's inventory
        """

    @abstractmethod
    def assign_inventory(self, inventory):
        """Assign an inventory object to the player
        
            Args:
                inventory (Inventory): The new player's inventory
        """

    @property
    @abstractmethod
    def level(self) -> int:
        """The level of the player.

        Returns:
            int: The level of the player.
        """

    @property
    @abstractmethod
    def experience(self) -> int:
        """The experience of the player.

        Returns:
            int: The experience of the player.
        """

    @property
    @abstractmethod
    def experience_to_next_level(self) -> int:
        """The experience required to reach the next level.

        Returns:
            int: The experience required to reach the next level.
        """

    @property
    @abstractmethod
    def max_health(self) -> int:
        """The max amount of health the player can have at the moment"""

    @abstractmethod
    def upgrade_item(self, item):
        """Upgrades the selected item level"""

    @abstractmethod
    def assign_world(self, world):
        """Assigns a world to the player

            Args:
                IGameWorld: The world where the player is in
        """

    @abstractmethod
    def give_item(self, item):
        """Gives an item to the player
        
            Args:
                item: The item to add to the player's inventory
        """

class IMonsterFactory(ABC):
    """A monster factory object that creates monsters"""

    @staticmethod
    @abstractmethod
    def create_monster(monster_type: str, pos: Vector2):
        """Creates a monster using the monster type given

            Args:
                monster_type (str): "default"
                pos (Vector2): The position of the monster

            Returns:
                Monster: the monster created
        """