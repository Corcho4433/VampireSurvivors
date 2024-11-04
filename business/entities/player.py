"""Player entity module."""

import pygame
from pygame import Vector2

import settings

from business.entities.entity import MovableEntity
from business.entities.interfaces import ICanDealDamage, IDamageable, IPlayer
from business.world.interfaces import IGameWorld
from business.progression.inventory import Inventory
from business.progression.player_stats import PlayerStats
from business.progression.interfaces import IInventoryItem
from business.entities.collectibles.experience_gem import ExperienceGem
from business.entities.collectibles.healing_gem import HealingGem
from business.handlers.position_handler import PositionHandler
from presentation.sprite import PlayerSprite

class Player(MovableEntity, IPlayer, IDamageable, ICanDealDamage):
    """Player entity.

        The player is the main character of the game. 
        It can move around the game world and shoot at monsters.
    """

    def __init__(self, pos: pygame.Vector2, level=1, experience=0):
        if not PositionHandler.is_position_within_boundaries(pos):
            self.move_to_center()

        super().__init__(pos, 300, PlayerSprite(pos))

        self.__stats = PlayerStats(health=100)
        self.__world: IGameWorld = None
        self.__inventory : Inventory = None
        self.__experience = experience
        self.__max_health = self.__stats.health
        self.__level = level
        self._logger.debug("Created %s", self)

    def assign_inventory(self, inventory):
        self.__inventory = inventory

    def __str__(self):
        return f"Player(hp={self.__stats.health}, xp={self.__experience}, lvl={self.__level}, pos=({self._pos.x}, {self._pos.y}))" #pylint: disable=C0301

    @property
    def experience(self):
        return self.__experience

    @property
    def inventory(self):
        return self.__inventory

    @property
    def experience_to_next_level(self):
        return round(self.__level ** settings.EXPERIENCE_PER_LEVEL_RATIO)

    @property
    def level(self):
        return self.__level

    @property
    def damage(self):
        return self.__stats.attack_damage

    @property
    def luck(self):
        return self.__stats.luck

    @property
    def health(self) -> int:
        #print(self.__stats.health)
        return self.__stats.health

    @property
    def max_health(self) -> int:
        return self.__max_health

    @property
    def stats(self) -> PlayerStats:
        return self.__stats

    def upgrade_item(self, item: IInventoryItem):
        for inventory_item in self.__inventory.get_weapons():
            if inventory_item == item:
                inventory_item.upgrade()

    def take_damage(self, amount):
        self.__stats.health = max(0, self.__stats.health - amount)

        self.sprite.take_damage()

    def pickup_gem(self, gem):
        if isinstance(gem, ExperienceGem):
            self.__gain_experience(gem.amount)
        if isinstance(gem, HealingGem):
            self.__heal_from(gem.amount)

    def __gain_experience(self, amount: int):
        self.__experience += amount
        while self.__experience >= self.experience_to_next_level:
            self.__experience -= self.experience_to_next_level
            self.__level += 1
            self.__world.set_upgrade_menu_active(True)

    def __heal_from(self, amount: int):
        new_health = self.health + amount
        self.__stats.health = min(new_health, self.max_health)

    def __attack_at_nearest_enemy(self, world: IGameWorld):
        for weapon in self.__inventory.get_weapons():
            weapon.attack(self.pos, world, self.stats)

    def apply_perks(self, heal: bool):
        current_health = self.__stats.health
        self.__stats = PlayerStats(health=100)

        perks = self.__inventory.get_perks()
        for perk in perks:
            self.__stats = self.__stats * perk.stats

        self.__max_health = self.__stats.health
        if not heal:
            self.__stats.health = current_health

    def assign_world(self, world: IGameWorld):
        self.__world = world
        self.apply_perks(heal=True)

    def give_item(self, item: IInventoryItem):
        self.__inventory.add_item(item)

    def move(self, direction):
        if not PositionHandler.is_position_within_boundaries(self.pos + (direction * self.__stats.movement_speed) * (1/settings.FPS) * 2):
            return

        super().move(direction * self.__stats.movement_speed)

        if direction.x < 0:
            self.sprite.flip(True)
        elif direction.x > 0:
            self.sprite.flip(False)

    def update(self, world: IGameWorld):
        super().update(world)

        if not PositionHandler.is_position_within_boundaries(self.pos):
            self.move_to_center()

        self.__attack_at_nearest_enemy(world)
